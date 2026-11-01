"""Focused Base-chain independent-state and no-unwarranted-Robinhood claims."""

import copy
import json
import unittest
from pathlib import Path
from unittest.mock import patch

from paxg_chain_observer import ObservationError
from paxg_other_evm_cutoff import observe_chain

EVIDENCE = Path(__file__).resolve().parent / "observations" / "paxg_remaining_networks_20260930.json"
HOSTS = ("https://source-one.example", "https://source-two.example")


def test_rpc(endpoint, method, params):
    state = json.loads(EVIDENCE.read_text())["Base"]
    if method == "eth_chainId":
        return "0x2105"
    if method == "eth_getBlockByNumber":
        number = int(params[0], 16)
        if number == state["prior_block"]:
            return {"number": hex(number), "timestamp": hex(1790801999), "hash": state["prior_hash"]}
        return {"number": hex(number), "timestamp": hex(1790802001), "hash": state["next_hash"]}
    if method == "eth_call":
        if params[0]["data"] == "0x18160ddd":
            return "0x" + format(int(state["contract_supply_atomic"]), "064x")
        return "0x" + format(state["decimals"], "064x")
    if method == "eth_getCode":
        return "0x60006001"
    raise AssertionError(method)


class MultiChainCutoffTests(unittest.TestCase):
    def test_base_record_consistent_and_does_not_claim_physical_backing(self):
        with patch("paxg_other_evm_cutoff.read_rpc", side_effect=test_rpc):
            x = observe_chain("Base", HOSTS)
        self.assertEqual(x["token_supply_exact"], "235.0015")
        self.assertEqual(x["difference_to_displayed_tokens"], "0.0015")
        self.assertTrue(x["compatible_with_hypothetical_nearest_whole_rounding"])
        self.assertFalse(x["report_rounding_policy_confirmed"])
        self.assertFalse(x["all_four_networks_verified"])
        self.assertFalse(x["independent_bullion_or_legal_title_proven"])

    def test_rejects_disagreeing_provider_supply_and_cutoff(self):
        def bad_supply(endpoint, method, params):
            if endpoint == HOSTS[1] and method == "eth_call" and params[0]["data"] == "0x18160ddd":
                return "0x" + format(200 * 10**18, "064x")
            return test_rpc(endpoint, method, params)
        with patch("paxg_other_evm_cutoff.read_rpc", side_effect=bad_supply):
            with self.assertRaises(ObservationError):
                observe_chain("Base", HOSTS)
        def bad_cutoff(endpoint, method, params):
            if method == "eth_getBlockByNumber" and int(params[0], 16) == 52006327:
                x = test_rpc(endpoint, method, params)
                x["timestamp"] = hex(1790801999)
                return x
            return test_rpc(endpoint, method, params)
        with patch("paxg_other_evm_cutoff.read_rpc", side_effect=bad_cutoff):
            with self.assertRaises(ObservationError):
                observe_chain("Base", HOSTS)

    def test_robinhood_rejects_fake_independence_and_has_real_archive_routes(self):
        from paxg_other_evm_cutoff import CONFIG
        self.assertEqual(
            {__import__("urllib.parse", fromlist=["urlsplit"]).urlsplit(u).hostname
             for u in CONFIG["Robinhood"]["nodes"]},
            {"robinhood.rpc.pinax.network", "robinhood.drpc.org"},
        )
        with self.assertRaises(ObservationError):
            observe_chain("Robinhood", (HOSTS[0], HOSTS[0]))


if __name__ == "__main__":
    unittest.main()
