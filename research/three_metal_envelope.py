"""Three-metal global mine-flow thought experiment, NOT a fund or reserves.

The metal values and mines are independent sources with different units and
methodologies. Entire mine production is owned by others; nobody has offered
a percentage to ORD. USD prices are synthetic scenario inputs, NOT a peg,
guaranteed liquidation price, observed spot quotation or trade execution.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

INPUT = Path(__file__).with_name("three_metal_inputs.json")
TROY_GRAMS = Decimal("31.1034768")
GRAMS_PER_TONNE = Decimal(1_000_000)
BPS = Decimal(10_000)


def _decimal(value: object) -> Decimal:
    # All published quantitative inputs are decimal strings, not floats.
    if not isinstance(value, str):
        raise ValueError("expected a decimal input string")
    try:
        result = Decimal(value)
    except Exception as exc:
        raise ValueError("invalid decimal string") from exc
    if not result.is_finite() or result <= 0:
        raise ValueError("expected positive finite quantity")
    return result


def _fmt(x: Decimal, template: str = "0.000000") -> str:
    return str(x.quantize(Decimal(template), rounding=ROUND_HALF_UP))


def compare(config: dict) -> dict:
    if config.get("schema_version") != 1:
        raise ValueError("unknown research input schema")
    population = config["assumed_population"]
    if type(population) is not int or population <= 0:
        raise ValueError("population must be a positive integer")
    pop = Decimal(population)
    shares = config["hypothetical_fraction_of_2025_world_mine_flow_basis_points"]
    if not isinstance(shares, list) or not shares or len(set(shares)) != len(shares):
        raise ValueError("fractions must be a nonempty unique list")
    metals = config["metals"]
    if not isinstance(metals, list) or [x["symbol"] for x in metals] != ["Au", "Ag", "Cu"]:
        raise ValueError("three independently specified metals required")
    rows=[]
    all_production_value=Decimal(0)
    normalized=[]
    for x in metals:
        symbol=x["symbol"]
        if symbol == "Ag":
            tonnes = _decimal(x["mine_2025_million_troy_ounces"]) * Decimal(1_000_000) * TROY_GRAMS / GRAMS_PER_TONNE
        else:
            tonnes = _decimal(x["mine_2025_metric_tonnes"])
        if symbol in ("Au","Ag"):
            reference_value = tonnes * GRAMS_PER_TONNE / TROY_GRAMS * _decimal(
                x["price_usd_per_troy_ounce_ASSUMED"]
            )
        else:
            reference_value = tonnes * _decimal(x["price_usd_per_metric_tonne_ASSUMED"])
        all_production_value += reference_value
        normalized.append((symbol, tonnes, reference_value, x["source_production"]))

    for fraction_bps in shares:
        if type(fraction_bps) is not int or not 0 < fraction_bps <= 10_000:
            raise ValueError("fraction bps must be 1..10000")
        share=Decimal(fraction_bps)/BPS
        per_metal=[]
        for symbol, tonnes, gross_value, source in normalized:
            grams_per_person = tonnes * share * GRAMS_PER_TONNE / pop
            dollars_each = gross_value * share / pop
            per_metal.append({
                "metal": symbol,
                "annual_mine_tonnes_2025":_fmt(tonnes,"0.000"),
                "hypothetical_allocated_grams_per_person":_fmt(grams_per_person,"0.000000000"),
                "hypothetical_reference_usd_per_person":_fmt(dollars_each,"0.000000"),
                "source": source,
                "actual_metal_pledged":False,
                "warehouse_grade_and_title_verified":False
            })
        rows.append({
            "hypothetical_mine_flow_share_percent":_fmt(share * 100,"0.00"),
            "three_metals_hypothetical_usd_per_person_before_costs":_fmt(
                all_production_value*share/pop,"0.000000"
            ),
            "separate_metals":per_metal,
        })
    target=config["illustrative_annual_reference_value_per_person_usd"]
    if type(target) is not int or target <= 0:
        raise ValueError("reference target must be positive")
    fraction_of_annual_mine_value_needed = pop * target / all_production_value
    return {
        "status":"HYPOTHETICAL_UNOWNED",
        "population_assumed":population,
        "annual_mine_value_at_assumed_prices_usd":_fmt(all_production_value,"0.00"),
        "annual_mine_value_per_person_at_100pct_hypothetical_flow_usd":_fmt(
            all_production_value/pop,"0.000"
        ),
        "percent_of_combined_mine_flow_value_for_reference_target":_fmt(
            fraction_of_annual_mine_value_needed*100,"0.000"
        ),
        "benchmark_reference_usd_per_person_NOT_PROMISED":target,
        "gold_total_above_ground_stock_2025_tonnes_NOT_AVAILABLE":config["metals"][0].get(
            "above_ground_2025_stock_metric_tonnes_NOT_AVAILABLE"
        ),
        "reserve_or_income_owned_by_ord":False,
        "all_metals_legally_accessible_at_synthetic_quote":False,
        "source_and_assumptions":config["source_date_scope"],
        "rows":rows,
    }


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--inputs",type=Path,default=INPUT)
    args=p.parse_args()
    data=json.loads(args.inputs.read_text(encoding="utf-8"))
    print(json.dumps(compare(data),indent=2,sort_keys=True))


if __name__=="__main__":
    main()
