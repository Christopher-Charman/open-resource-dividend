"""Reproducible multi-period ORD funding *thought experiment*, not real finance.

All balances are abstract integer units of a single metal. Contributions
represent *assumed* verified and unencumbered metal delivered to custody.
The script deliberately exposes unfunded dividends, cost arrears and changes
in recipient populations; it makes no prediction of commodity prices, AI
productivity, real eligibility, market liquidity or actual endowment yields.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from replay_audit import assert_matches_snapshot
from stock_flow import METALS, FundingError, StockFlow

DEFAULT = Path(__file__).resolve().parent / "scenarios" / "volatile_copper.json"


def _integer(value: object, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise FundingError(f"expected integer >= {minimum}")
    return value


def _exact_keys(data: object, keys: set[str]) -> dict:
    if not isinstance(data, dict) or set(data) != keys:
        raise FundingError("scenario has missing or unexpected fields")
    return data


def simulate(config: dict) -> dict:
    """Simulate transfers from a funded pool; dividends never mint claims."""
    config = _exact_keys(config, {
        "name", "metal", "initial_endowment_units", "target_per_person_units", "periods"
    })
    if not isinstance(config["name"], str) or not config["name"].strip():
        raise FundingError("scenario name must be nonempty")
    metal = config["metal"]
    if metal not in METALS:
        raise FundingError("unsupported metal class")
    initial = _integer(config["initial_endowment_units"])
    target = _integer(config["target_per_person_units"], 1)
    periods = config["periods"]
    if not isinstance(periods, list) or not periods:
        raise FundingError("periods must be a nonempty list")

    model = StockFlow()
    if initial:
        model.deposit_assumed_verified("source", metal, initial, "SYNTH-INITIAL")
        model.transfer("source", "pool", metal, initial)

    records = []
    used_labels: set[str] = set()
    cost_arrears = 0
    cumulative_allocation = 0
    cumulative_contribution = initial
    cumulative_cost_paid = 0
    for period in periods:
        period = _exact_keys(period, {
            "label", "recipients", "contribution_units", "operating_cost_units", "buffer_units"
        })
        label = period["label"]
        if not isinstance(label, str) or not label.strip() or label in used_labels:
            raise FundingError("period labels must be unique nonempty strings")
        used_labels.add(label)
        people = _integer(period["recipients"], 1)
        contributions = _integer(period["contribution_units"])
        new_costs = _integer(period["operating_cost_units"])
        buffer_units = _integer(period["buffer_units"])
        if contributions:
            model.deposit_assumed_verified(
                "source", metal, contributions, f"SYNTH-DEPOSIT-{label}"
            )
            model.transfer("source", "pool", metal, contributions)
        cumulative_contribution += contributions

        due = new_costs + cost_arrears
        costs_paid = min(due, model.accounts["pool"][metal])
        if costs_paid:
            model.transfer("pool", "operations", metal, costs_paid)
        cost_arrears = due - costs_paid
        cumulative_cost_paid += costs_paid

        available = max(0, model.accounts["pool"][metal] - buffer_units)
        per_person = min(target, available // people) if cost_arrears == 0 else 0
        distributed = per_person * people
        if per_person:
            model.dividend(
                "pool", [f"person-{i:05d}" for i in range(people)],
                metal, per_person, retained_buffer=buffer_units
            )
        audit = assert_matches_snapshot(model.events, model.reserves, model.accounts)
        cumulative_allocation += distributed
        records.append({
            "period": label,
            "eligible_people_assumed": people,
            "new_fully_delivered_metal_assumed": contributions,
            "costs_due_including_arrears": due,
            "costs_paid_in_claims": costs_paid,
            "cost_arrears_not_backed_by_claims": cost_arrears,
            "retained_buffer_target": buffer_units,
            "per_person_target": target,
            "per_person_paid": per_person,
            "total_distributed": distributed,
            "unmet_target_units": people * (target - per_person),
            "pool_after_period": model.accounts["pool"][metal],
            "assumed_reserves_after_period": model.reserves[metal],
            "outstanding_claims_after_period": audit["outstanding_claims"][metal],
            "event_root": audit["event_root"],
        })

    return {
        "name": config["name"],
        "metal": metal,
        "synthetic_not_real_assets": True,
        "no_external_reserve_attestation": True,
        "cumulative_contributed_units": cumulative_contribution,
        "cumulative_distributed_units": cumulative_allocation,
        "cumulative_paid_operating_units": cumulative_cost_paid,
        "remaining_unpaid_cost_units": cost_arrears,
        "fund_remaining_units": model.accounts["pool"][metal],
        "total_outstanding_units": model.reserves[metal],
        "periods": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "scenario", nargs="?", type=Path, default=DEFAULT,
        help="path to a non-financial JSON scenario (default: volatile copper)"
    )
    args = parser.parse_args()
    print(json.dumps(simulate(json.loads(
        args.scenario.read_text(encoding="utf-8")
    )), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
