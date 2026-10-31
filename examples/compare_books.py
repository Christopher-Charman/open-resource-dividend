"""Dual-book audit demonstration: independent claimed metal vs synthetic ledger.

This compares *declared* inventory and all *known* obligations to an
independently replayed event history. It NEVER establishes actual metal,
legal title, complete liabilities, auditor independence or physical redemption.
A pass of accounting arithmetic is not a reserve audit or solvency proof.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from replay_audit import replay_events, ReplayError

METALS = ("Au", "Ag", "Cu")


class AssuranceInputError(ValueError):
    """Unsupported or internally inconsistent evidence representation."""


def _quantities(value: object, *, positive: bool = False) -> dict[str, int]:
    if not isinstance(value, dict) or set(value) != set(METALS):
        raise AssuranceInputError("all metals must be present, separately stated")
    for number in value.values():
        if type(number) is not int or number < int(positive):
            raise AssuranceInputError("metal quantities must be integers >= 0")
    return value


def compare_books(journal_events: list[dict], inventory: dict, extra_liabilities: dict) -> dict:
    """Reconcile records from distinct inputs; attestations remain unverified."""
    try:
        journal = replay_events(journal_events)
    except (ReplayError, TypeError, ValueError) as exc:
        raise AssuranceInputError("invalid or uneconomic synthetic event journal") from exc
    if not isinstance(inventory, dict) or set(inventory) != {"lots", "declared_evidence_source"}:
        raise AssuranceInputError("inventory requires lots and declared evidence source")
    if inventory["declared_evidence_source"] not in ("SYNTHETIC", "UNVERIFIED"):
        raise AssuranceInputError("no self-asserted verified/audited status is accepted")

    lots = inventory["lots"]
    if not isinstance(lots, list):
        raise AssuranceInputError("lots must be a list")
    seen = set()
    declared = dict.fromkeys(METALS, 0)
    for lot in lots:
        if not isinstance(lot, dict) or set(lot) != {"id", "metal", "quantity", "encumbered"}:
            raise AssuranceInputError("lot schema mismatch")
        name, metal, quantity, encumbered = (lot[k] for k in ("id", "metal", "quantity", "encumbered"))
        if not isinstance(name, str) or not name.strip() or name in seen:
            raise AssuranceInputError("duplicate or empty lot identifier")
        seen.add(name)
        if metal not in METALS or type(quantity) is not int or quantity <= 0 or type(encumbered) is not bool:
            raise AssuranceInputError("invalid metal, lot quantity or encumbrance flag")
        if not encumbered:
            declared[metal] += quantity

    additional = _quantities(extra_liabilities)
    claims = journal["outstanding_claims"]
    combined = {m: claims[m] + additional[m] for m in METALS}
    deficits = {m: max(0, combined[m] - declared[m]) for m in METALS}
    return {
        "mathematical_coverage_of_declared_inventory": all(v == 0 for v in deficits.values()),
        "declared_unencumbered_lot_quantities": declared,
        "replayed_claim_liabilities": claims,
        "declared_other_liabilities": additional,
        "total_declared_liabilities": combined,
        "uncovered_by_declared_inventory": deficits,
        "journal_event_digest": journal["event_root"],
        "physical_assets_independently_verified": False,
        "legal_title_independently_verified": False,
        "liability_completeness_verified": False,
        "witnessed_append_only_history_verified": False,
        "audit_conclusion": "UNVERIFIED_PHYSICAL_AND_LEGAL_BACKING",
        "warning": "Declared lots and obligations can be fabricated or incomplete. "
                   "Arithmetic coverage is NOT proof of reserves.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, help="hypothetical inventory JSON")
    parser.add_argument("--events", type=Path, help="synthetic journal JSON")
    parser.add_argument("--other-liabilities", type=Path, help="metal-quantity map JSON")
    args = parser.parse_args()
    if any((args.inventory, args.events, args.other_liabilities)) and not all(
        (args.inventory, args.events, args.other_liabilities)
    ):
        parser.error("supply all three input paths or none")
    if args.inventory:
        inventory = json.loads(args.inventory.read_text(encoding="utf-8"))
        events = json.loads(args.events.read_text(encoding="utf-8"))
        other = json.loads(args.other_liabilities.read_text(encoding="utf-8"))
    else:
        from stock_flow import StockFlow

        example = StockFlow()
        example.deposit_assumed_verified("Frank", "Cu", 10, "SIM-DEPOSIT")
        events = example.events
        inventory = {
            "declared_evidence_source": "SYNTHETIC",
            "lots": [{"id": "SIM-LOT-1", "metal": "Cu", "quantity": 8, "encumbered": False}]
        }
        other = {"Au": 0, "Ag": 0, "Cu": 0}
    print(json.dumps(compare_books(events, inventory, other), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
