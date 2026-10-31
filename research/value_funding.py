"""ORD dividend *purchasing-power envelope*, not a currency or investment model.

USD is an external numeraire used to ask what REAL donated income might buy
at assumed metal prices. The output is neither a dollar-pegged token nor an
entitlement; there is NO committed fund, price feed, verified reserve, custody,
trading liquidity, legal title or predictable investment return.

Python standard library only. All inputs are integer quantities, and all
arithmetic uses Decimal to avoid rounding fictitious fractional reserve claims.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

INPUT = Path(__file__).with_name("value_funding_inputs.json")
BPS = Decimal(10000)
GRAMS_PER_TONNE = Decimal(1_000_000)


def _natural(value: object, allow_zero: bool = False) -> Decimal:
    if type(value) is not int or value < (0 if allow_zero else 1):
        raise ValueError("expected a nonnegative or positive integer input")
    return Decimal(value)


def _basis_points(value: object, *, allow_full: bool = False) -> Decimal:
    v = _natural(value, allow_zero=True)
    if v >= BPS and not (allow_full and v == BPS):
        raise ValueError("basis points must be less than 10000")
    return v / BPS


def _fmt(v: Decimal, precision: str = "0.000") -> str:
    return str(v.quantize(Decimal(precision), rounding=ROUND_HALF_UP))


def model(inputs: dict) -> dict:
    """Report sensitivity and reverse requirement without claiming deliverability."""
    if not isinstance(inputs, dict) or inputs.get("schema_version") != 1:
        raise ValueError("unsupported research input schema")
    if inputs.get("metal") != "Cu":
        raise ValueError("current validated scenario covers copper only")
    population = _natural(inputs["world_population_assumed"])
    mine_output = _natural(inputs["world_2025_mine_copper_content_tonnes"])
    admin_fixed = _natural(inputs["custody_and_admin_fixed_usd"], allow_zero=True)
    operating = _basis_points(inputs["operating_cost_basis_points_of_funding"])
    premium = _basis_points(inputs["acquisition_premium_basis_points"])
    retained = _basis_points(inputs["fraction_of_acquired_claims_retained_as_buffer_basis_points"])
    assumed_yield = _basis_points(inputs["illustrative_realized_endowment_yield_basis_points"])
    target = _natural(inputs["annual_reference_income_goal_usd_per_person"])
    lot = _natural(inputs["wholesale_lot_tonnes"])

    budgets = inputs["annual_funding_budgets_usd"]
    quotations = inputs["illustrative_quote_usd_per_tonne"]
    if (not isinstance(budgets, list) or not budgets
            or not isinstance(quotations, list) or not quotations
            or len(set(budgets)) != len(budgets)
            or len(set(quotations)) != len(quotations)):
        raise ValueError("nonempty unique quote and funding scenarios required")
    budgets = [_natural(x) for x in budgets]
    quotations = [_natural(x) for x in quotations]

    scenarios = []
    for price in quotations:
        for budget in budgets:
            operating_cost = budget * operating
            after_cost = max(Decimal(0), budget - admin_fixed - operating_cost)
            # The model assumes full settlement at a STATIC quoted price; it
            # does not model the demand's impact on that quote.
            assumed_acquired_tonnes = after_cost / (price * (1 + premium))
            retained_claim_tonnes = assumed_acquired_tonnes * retained
            distributable_tonnes = assumed_acquired_tonnes - retained_claim_tonnes
            grams_each = distributable_tonnes * GRAMS_PER_TONNE / population
            base_reference_value_each = distributable_tonnes * price / population
            fraction_of_annual_mine_output = assumed_acquired_tonnes / mine_output
            recipients_per_wholesale_lot = (
                lot * GRAMS_PER_TONNE / grams_each
                if grams_each > 0 else None
            )
            scenarios.append({
                "budget_usd_assumed": int(budget),
                "price_usd_per_tonne_ASSUMED_NOT_OBSERVED": int(price),
                "assumed_cash_operating_cost_usd": _fmt(admin_fixed + operating_cost, "0.00"),
                "hypothetical_metal_purchase_tonnes": _fmt(assumed_acquired_tonnes, "0.000000"),
                "retained_metal_claims_tonnes": _fmt(retained_claim_tonnes, "0.000000"),
                "hypothetical_distributable_tonnes": _fmt(distributable_tonnes, "0.000000"),
                "grams_per_person_before_real_delivery_cost": _fmt(grams_each, "0.000000"),
                "reference_usd_value_per_person_NOT_PAYMENT": _fmt(base_reference_value_each, "0.000"),
                "purchase_mass_as_percent_of_2025_world_mine_output": _fmt(
                    fraction_of_annual_mine_output * 100, "0.000"
                ),
                "population_claims_per_wholesale_lot_equivalent": (
                    _fmt(recipients_per_wholesale_lot, "0") if recipients_per_wholesale_lot else None
                ),
                "actual_assets_or_income_committed": False,
                "physical_acquisition_at_this_quote_verified": False,
                "legal_title_verified": False,
                "physical_retail_redemption_cost_included": False,
            })

    # Reverse calculation: what annual settled *external* cash inflow would
    # be needed before purchase to deliver a benchmark price-equivalent metal
    # amount, after modelled costs and a retained metal-claims buffer?
    # All quantities are independent of the price at which that cash converts
    # into metal, *if* both sale and purchase quote move proportionally.
    required_gross_annual_budget = (
        ((population * target) * (1 + premium) / (1 - retained)) + admin_fixed
    ) / (1 - operating)
    required_capital_at_assumed_yield = (
        required_gross_annual_budget / assumed_yield if assumed_yield > 0 else None
    )
    return {
        "status": "HYPOTHETICAL_UNFUNDED",
        "currency_is_external_reporting_numeraire_only": True,
        "world_population_assumed": int(population),
        "metal": "Cu",
        "world_2025_mine_output_copper_content_tonnes": int(mine_output),
        "reference_target_usd_per_person_per_year_NOT_PROMISED": int(target),
        "annual_cash_income_required_before_costs_usd": _fmt(required_gross_annual_budget, "0.00"),
        "hypothetical_endowment_principal_at_assumed_realized_yield_usd": (
            _fmt(required_capital_at_assumed_yield, "0.00")
            if required_capital_at_assumed_yield is not None else None
        ),
        "endowment_is_pledged_or_exists": False,
        "endowment_return_guaranteed": False,
        "model_omits_price_impact_and_legal_or_delivery_verification": True,
        "sources": inputs.get("sources", []),
        "scenarios": scenarios,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, default=INPUT)
    args = parser.parse_args()
    print(json.dumps(model(json.loads(args.inputs.read_text(encoding="utf-8"))),
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
