"""Focused conservation and provenance checks for three-metal upper envelope."""

import json
import unittest
from decimal import Decimal
from pathlib import Path

from three_metal_envelope import compare

SOURCE = Path(__file__).with_name("three_metal_inputs.json")


class ThreeMetalTests(unittest.TestCase):
    def test_fractional_production_value_is_not_declared_as_backing(self):
        report = compare(json.loads(SOURCE.read_text(encoding="utf-8")))
        self.assertFalse(report["reserve_or_income_owned_by_ord"])
        self.assertFalse(report["all_metals_legally_accessible_at_synthetic_quote"])
        self.assertEqual([r["hypothetical_mine_flow_share_percent"] for r in report["rows"]],
                         ["1.00","10.00"])
        a,b = report["rows"]
        self.assertEqual([x["metal"] for x in a["separate_metals"]],["Au","Ag","Cu"])
        self.assertTrue(all(not x["actual_metal_pledged"] for x in a["separate_metals"]))
        self.assertLess(
            abs(Decimal(b["three_metals_hypothetical_usd_per_person_before_costs"])
              - 10*Decimal(a["three_metals_hypothetical_usd_per_person_before_costs"])),
            Decimal("0.00001")
        )

    def test_price_and_ownership_assumptions_remain_explicit(self):
        config=json.loads(SOURCE.read_text(encoding="utf-8"))
        report=compare(config)
        self.assertGreater(
            Decimal(report["percent_of_combined_mine_flow_value_for_reference_target"]),90
        )
        self.assertLess(
            Decimal(report["percent_of_combined_mine_flow_value_for_reference_target"]),110
        )
        config["metals"][1]["mine_2025_million_troy_ounces"]="NaN"
        with self.assertRaises(ValueError):
            compare(config)


if __name__=="__main__":
    unittest.main()
