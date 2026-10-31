"""Regression tests for independent replay of the synthetic event journal."""

import copy
import hashlib
import json
import unittest

from replay_audit import ReplayError, assert_matches_snapshot, replay_events
from stock_flow import StockFlow


def sample():
    model = StockFlow()
    model.deposit_assumed_verified("donor", "Cu", 30, "SIMULATED-DEPOSIT-1")
    model.transfer("donor", "pool", "Cu", 30)
    model.dividend("pool", ["Frank", "Bob"], "Cu", 10, retained_buffer=10)
    model.transfer("Frank", "Bob", "Cu", 3)
    model.redeem_assumed_delivered("Frank", "Cu", 2, "SIMULATED-DELIVERY-1")
    return model


def rehash(events):
    """Attacker can rewrite an unanchored history; economic replay still checks rules."""
    previous = "0" * 64
    for event in events:
        event["previous"] = previous
        data = {key: value for key, value in event.items() if key != "digest"}
        event["digest"] = hashlib.sha256(
            json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        previous = event["digest"]


class ReplayTests(unittest.TestCase):
    def test_independent_state_reconstruction(self):
        model = sample()
        result = assert_matches_snapshot(
            model.events, model.reserves, model.accounts
        )
        self.assertEqual(result["assumed_reserves"]["Cu"], 28)
        self.assertEqual(result["outstanding_claims"]["Cu"], 28)
        self.assertEqual(result["balances"]["Frank"]["Cu"], 5)
        self.assertFalse(result["independent_external_anchor"])

    def test_rejects_modified_event_digest(self):
        events = copy.deepcopy(sample().events)
        events[0]["details"]["quantity"] = 300
        with self.assertRaises(ReplayError):
            replay_events(events)

    def test_rejects_rehashed_economic_fraud(self):
        events = copy.deepcopy(sample().events)
        # Even with repaired hashes, Bob cannot redeem more claims than held.
        events[-1]["details"]["holder"] = "Frank"
        events[-1]["details"]["quantity"] = 31
        rehash(events)
        with self.assertRaises(ReplayError):
            replay_events(events)

    def test_rejects_snapshot_drift(self):
        model = sample()
        model.accounts["Bob"]["Cu"] += 1
        with self.assertRaises(ReplayError):
            assert_matches_snapshot(model.events, model.reserves, model.accounts)


if __name__ == "__main__":
    unittest.main()
