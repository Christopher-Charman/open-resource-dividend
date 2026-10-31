"""Commodity flow envelope: reproducible arithmetic, NOT ORD's available reserves.

A fraction of world copper *mine production* is a counterfactual economic
scenario. Nothing in this program implies that any producer has contributed
metal, that mined output is refined/deliverable or that anyone owns it.
No external Python packages, network, real money or token operations.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

DEFAULT_INPUT = Path(__file__).with_name("scale_inputs.json")
TEN_THOUSAND = Decimal(10000)
GRAMS_PER_TONNE = Decimal(1_000_000)


def _natural(value: object) -> int:
    if type(value) is not int or value <= 0:
        raise ValueError("expected a strictly positive integer")
    return value


def _render(value: Decimal, places: str = "0.000") -> str:
    return str(value.quantize(Decimal(places), rounding=ROUND_HALF_UP))


def calculate(config: dict) -> dict:
    """Compute a scale envelope without assuming any commodity is donated."""
    if not isinstance(config, dict) or config.get("schema_version") != 1:
        raise ValueError("unknown research data schema")
    production = Decimal(_natural(config["world_copper_mine_production_2025_tonnes"]))
    population = Decimal(_natural(config["world_population_2026_assumption"]))
    lot = Decimal(_natural(config["lme_grade_a_copper_lot_tonnes"]))
    shares = config["hypothetical_contributed_share_basis_points"]
    targets = config["illustrative_annual_per_person_target_grams"]
    if (
        not isinstance(shares, list) or not shares
        or not isinstance(targets, list) or not targets
        or len(set(shares)) != len(shares) or len(set(targets)) != len(targets)
    ):
        raise ValueError("shares and targets must be nonempty unique integer lists")
    rows = []
    for share in shares:
        if type(share) is not int or share <= 0 or share > 10000:
            raise ValueError("share bps must be within 1..10000")
        assumed_metal_tonnes = production * Decimal(share) / TEN_THOUSAND
        grams_each = assumed_metal_tonnes * GRAMS_PER_TONNE / population
        rows.append({
            "hypothetical_world_output_share_percent": _render(Decimal(share) / 100, "0.00"),
            "hypothetical_metal_tonnes": _render(assumed_metal_tonnes),
            "grams_per_person_before_all_costs": _render(grams_each, "0.000000"),
            "fractional_lme_lot_equivalents": _render(assumed_metal_tonnes / lot),
            "assumed_unencumbered_custody_verified": False,
            "actual_available_to_ord_tonnes": None,
        })
    inverse = []
    for target in targets:
        goal = Decimal(_natural(target))
        required_tonnes = goal * population / GRAMS_PER_TONNE
        required_share = required_tonnes / production * Decimal(100)
        inverse.append({
            "annual_target_grams_per_person": target,
            "required_copper_tonnes_per_year": _render(required_tonnes),
            "share_of_reported_2025_world_mine_output_percent": _render(required_share, "0.0000"),
            "hypothetical_only": True,
        })
    return {
        "units": "tonnes copper content and grams/person/year; not currency, income, custody or price",
        "reference_date": config["snapshot_date"],
        "source_notes": config["source_notes"],
        "baseline_world_mined_copper_tonnes_2025": int(production),
        "baseline_population_round_assumption": int(population),
        "base_case_assumptions": {
            "world_output_available_to_ord": False,
            "fraction_has_to_be_voluntarily_legally_contributed": True,
            "mine_output_is_not_grade_a_refined_delivery": True,
            "processing_and_all_costs_included": False,
            "sustainable_periodic_metal_income_proved": False,
        },
        "hypothetical_fraction_rows": rows,
        "inverse_target_rows": inverse,
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--inputs", type=Path, default=DEFAULT_INPUT)
    p.add_argument("--output", type=Path, default=None, help="optional JSON output to a local file")
    args = p.parse_args()
    result = calculate(json.loads(args.inputs.read_text(encoding="utf-8")))
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
