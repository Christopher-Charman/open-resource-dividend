"""Focused tests: budget conservation, market mass stress, and input limits."""

import json
import unittest
from decimal import Decimal
from pathlib import Path

from value_funding import model

INPUT = Path(__file__).with_name("value_funding_inputs.json")


class ValueFundingTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads(INPUT.read_text(encoding="utf-8"))

    def test_no_claims_without_income_or_real_title(self):
        report = model(self.config)
        self.assertEqual(report["status"], "HYPOTHETICAL_UNFUNDED")
        self.assertFalse(report["endowment_is_pledged_or_exists"])
        for row in report["scenarios"]:
            self.assertFalse(row["actual_assets_or_income_committed"])
            self.assertFalse(row["physical_acquisition_at_this_quote_verified"])
            self.assertFalse(row["legal_title_verified"])
            self.assertLess(
                Decimal(row["reference_usd_value_per_person_NOT_PAYMENT"]),
                Decimal(row["budget_usd_assumed"]) / self.config["world_population_assumed"]
            )

    def test_static_price_stress_exposes_large_metal_demand(self):
        report = model(self.config)
        rows = report["scenarios"]
        self.assertEqual(len(rows), 9)
        middle = next(row for row in rows if row["budget_usd_assumed"] == 100000000000
                      and row["price_usd_per_tonne_ASSUMED_NOT_OBSERVED"] == 14000)
        self.assertGreater(
            Decimal(middle["purchase_mass_as_percent_of_2025_world_mine_output"]), 25
        )
        high = next(row for row in rows if row["budget_usd_assumed"] == 1000000000000
                    and row["price_usd_per_tonne_ASSUMED_NOT_OBSERVED"] == 14000)
        self.assertGreater(
            Decimal(high["purchase_mass_as_percent_of_2025_world_mine_output"]), 100
        )
        self.assertGreater(
            Decimal(report["annual_cash_income_required_before_costs_usd"]), 830000000000
        )
        self.assertGreater(
            Decimal(report["hypothetical_endowment_principal_at_assumed_realized_yield_usd"]),
            20000000000000
        )

    def test_rejects_absurd_price_and_unfundable_fraction(self):
        self.config["illustrative_quote_usd_per_tonne"] = [0]
        with self.assertRaises(ValueError):
            model(self.config)
        self.config["illustrative_quote_usd_per_tonne"] = [14000]
        self.config["fraction_of_acquired_claims_retained_as_buffer_basis_points"] = 10000
        with self.assertRaises(ValueError):
            model(self.config)


if __name__ == "__main__":
    unittest.main()
