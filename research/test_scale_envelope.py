"""Two focused unit checks for the source-labelled scale-envelope arithmetic."""

import json
import unittest
from decimal import Decimal
from pathlib import Path

from scale_envelope import calculate

SOURCE = Path(__file__).with_name("scale_inputs.json")


class ScaleEnvelopeTests(unittest.TestCase):
    def test_2025_copper_flow_and_population_bound(self):
        config = json.loads(SOURCE.read_text(encoding="utf-8"))
        report = calculate(config)
        one_percent = report["hypothetical_fraction_rows"][1]
        self.assertEqual(one_percent["hypothetical_world_output_share_percent"], "1.00")
        self.assertEqual(one_percent["hypothetical_metal_tonnes"], "236653.000")
        self.assertEqual(one_percent["grams_per_person_before_all_costs"], "28.512410")
        target = report["inverse_target_rows"][2]
        self.assertEqual(target["required_copper_tonnes_per_year"], "8300000.000")
        self.assertTrue(Decimal(target["share_of_reported_2025_world_mine_output_percent"]) > 35)
        self.assertIsNone(one_percent["actual_available_to_ord_tonnes"])
        self.assertFalse(report["base_case_assumptions"]["world_output_available_to_ord"])

    def test_inputs_must_not_hide_invalid_percentages_or_people(self):
        config = json.loads(SOURCE.read_text(encoding="utf-8"))
        config["hypothetical_contributed_share_basis_points"] = [10001]
        with self.assertRaises(ValueError):
            calculate(config)
        config["hypothetical_contributed_share_basis_points"] = [100]
        config["world_population_2026_assumption"] = True
        with self.assertRaises(ValueError):
            calculate(config)


if __name__ == "__main__":
    unittest.main()
