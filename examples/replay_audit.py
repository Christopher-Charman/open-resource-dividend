"""Independent replay of the ORD educational event log (not physical reserve proof).

This reconstructs all *assumed* reserves and claims from events, validates each
transaction and checks canonical SHA-256 links. Without an external trusted
checkpoint, the complete history can still be rewritten and rehashed. No
consensus, identity, custody, legal title, cryptographic signatures or actual
metal is represented here.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

METALS = ("Au", "Ag", "Cu")
GENESIS = "0" * 64


class ReplayError(ValueError):
    """Malformed or inconsistent illustrative event history."""


def _positive_integer(value: object) -> int:
    if type(value) is not int or value <= 0:
        raise ReplayError("quantity must be a positive integer")
    return value


def _name(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ReplayError("identifier must be a nonempty string")
    return value


def _nonnegative_integer(value: object) -> int:
    if type(value) is not int or value < 0:
        raise ReplayError("buffer must be a nonnegative integer")
    return value


def _details(value: object, expected: set[str]) -> dict:
    if not isinstance(value, dict) or set(value) != expected:
        raise ReplayError("unexpected transaction details schema")
    return value


def replay_events(events: list[dict]) -> dict:
    """Return an independently derived toy balance sheet from a complete log."""
    if not isinstance(events, list):
        raise ReplayError("events must be a list")
    reserves = dict.fromkeys(METALS, 0)
    balances = defaultdict(lambda: dict.fromkeys(METALS, 0))
    identifiers: set[str] = set()
    previous = GENESIS

    for sequence, event in enumerate(events, start=1):
        if not isinstance(event, dict) or set(event) != {
            "sequence", "previous", "kind", "metal", "details", "digest"
        }:
            raise ReplayError("unexpected event schema")
        if type(event["sequence"]) is not int or event["sequence"] != sequence:
            raise ReplayError("event sequence discontinuity")
        if event["previous"] != previous:
            raise ReplayError("previous digest does not match")
        try:
            canonical = json.dumps(
                {key: value for key, value in event.items() if key != "digest"},
                sort_keys=True, separators=(",", ":"), allow_nan=False,
            )
        except (TypeError, ValueError) as exc:
            raise ReplayError("event cannot be canonically encoded") from exc
        digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        if event["digest"] != digest:
            raise ReplayError("event digest does not match")
        previous = digest

        metal = event["metal"]
        if metal not in METALS:
            raise ReplayError("unsupported metal class")
        kind = event["kind"]
        d = event["details"]

        if kind == "assumed_deposit":
            d = _details(d, {"owner", "quantity", "evidence_id"})
            owner = _name(d["owner"])
            qty = _positive_integer(d["quantity"])
            eid = _name(d["evidence_id"])
            if eid in identifiers:
                raise ReplayError("duplicate deposit/delivery identifier")
            identifiers.add(eid)
            reserves[metal] += qty
            balances[owner][metal] += qty

        elif kind == "transfer":
            d = _details(d, {"from", "to", "quantity"})
            sender, recipient = _name(d["from"]), _name(d["to"])
            qty = _positive_integer(d["quantity"])
            if sender == recipient or balances[sender][metal] < qty:
                raise ReplayError("self-transfer or overspend")
            balances[sender][metal] -= qty
            balances[recipient][metal] += qty

        elif kind == "funded_distribution":
            d = _details(d, {
                "pool", "recipients", "per_person", "total", "retained_buffer"
            })
            pool = _name(d["pool"])
            recipients = d["recipients"]
            if not isinstance(recipients, list) or not recipients:
                raise ReplayError("recipients must be a nonempty list")
            if any(not isinstance(person, str) or not person.strip() for person in recipients):
                raise ReplayError("recipient identifier is invalid")
            if len(set(recipients)) != len(recipients) or pool in recipients:
                raise ReplayError("duplicate recipient or pool included")
            per_person = _positive_integer(d["per_person"])
            total = _positive_integer(d["total"])
            buffer = _nonnegative_integer(d["retained_buffer"])
            if total != per_person * len(recipients):
                raise ReplayError("incorrect distribution total")
            if balances[pool][metal] - total < buffer:
                raise ReplayError("unfunded distribution or violated buffer")
            balances[pool][metal] -= total
            for person in recipients:
                balances[person][metal] += per_person

        elif kind == "assumed_delivered_redemption":
            d = _details(d, {"holder", "quantity", "delivery_id"})
            holder = _name(d["holder"])
            qty = _positive_integer(d["quantity"])
            did = _name(d["delivery_id"])
            if did in identifiers:
                raise ReplayError("duplicate deposit/delivery identifier")
            if balances[holder][metal] < qty or reserves[metal] < qty:
                raise ReplayError("redemption exceeds existing claims or reserves")
            identifiers.add(did)
            balances[holder][metal] -= qty
            reserves[metal] -= qty
        else:
            raise ReplayError("unrecognised event kind")

        if any(
            sum(account[m] for account in balances.values()) != reserves[m]
            for m in METALS
        ):
            raise ReplayError("assumed reserves and claims do not reconcile")

    return {
        "assumed_reserves": reserves,
        "outstanding_claims": {
            metal: sum(account[metal] for account in balances.values())
            for metal in METALS
        },
        "balances": {name: dict(values) for name, values in sorted(balances.items())},
        "event_count": len(events),
        "event_root": previous,
        "independent_external_anchor": False,
    }


def assert_matches_snapshot(events: list[dict], reserves: dict, accounts: dict) -> dict:
    """Detect a claimed in-memory balance sheet that differs from replay."""
    result = replay_events(events)
    if result["assumed_reserves"] != reserves:
        raise ReplayError("reserve snapshot differs from journal replay")
    normalized = {
        name: {metal: account.get(metal, 0) for metal in METALS}
        for name, account in accounts.items()
    }
    if result["balances"] != normalized:
        raise ReplayError("account snapshot differs from journal replay")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--events", type=Path, help="JSON list of illustrative events")
    args = parser.parse_args()
    if args.events is None:
        from stock_flow import StockFlow

        model = StockFlow()
        model.deposit_assumed_verified("donor", "Cu", 20, "SIM-CU-1")
        model.transfer("donor", "pool", "Cu", 20)
        model.dividend("pool", ["Frank", "Bob"], "Cu", 5)
        events = model.events
    else:
        events = json.loads(args.events.read_text(encoding="utf-8"))
    print(json.dumps(replay_events(events), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
