"""Three scenario tests: meaningful numerical checks without test duplication."""

import copy
import json
import unittest
from pathlib import Path

from funding_scenarios import simulate
from stock_flow import FundingError

SAMPLE = Path(__file__).resolve().parent / "scenarios" / "volatile_copper.json"


class FundingScenarioTests(unittest.TestCase):
    def test_volatile_funding_exposes_unmet_allocations(self):
        report = simulate(json.loads(SAMPLE.read_text(encoding="utf-8")))
        self.assertEqual(
            [p["per_person_paid"] for p in report["periods"]], [9, 0, 1, 9]
        )
        self.assertEqual(report["cumulative_contributed_units"], 2100)
        self.assertEqual(report["cumulative_distributed_units"], 1890)
        self.assertEqual(report["cumulative_paid_operating_units"], 40)
        self.assertEqual(report["fund_remaining_units"], 170)
        self.assertEqual(report["total_outstanding_units"], 2100)
        self.assertTrue(all(
            p["assumed_reserves_after_period"] == p["outstanding_claims_after_period"]
            for p in report["periods"]
        ))

    def test_shortfall_is_explicit_and_arrears_roll_forward(self):
        data = {
            "name": "No initial funding", "metal": "Ag",
            "initial_endowment_units": 0, "target_per_person_units": 10,
            "periods": [
                {"label": "A", "recipients": 2, "contribution_units": 0,
                 "operating_cost_units": 5, "buffer_units": 0},
                {"label": "B", "recipients": 2, "contribution_units": 20,
                 "operating_cost_units": 0, "buffer_units": 0},
            ],
        }
        report = simulate(data)
        self.assertEqual(report["periods"][0]["per_person_paid"], 0)
        self.assertEqual(report["periods"][0]["cost_arrears_not_backed_by_claims"], 5)
        self.assertEqual(report["periods"][1]["costs_paid_in_claims"], 5)
        self.assertEqual(report["periods"][1]["per_person_paid"], 7)
        self.assertEqual(report["fund_remaining_units"], 1)
        self.assertEqual(report["remaining_unpaid_cost_units"], 0)

    def test_bad_funding_inputs_are_rejected(self):
        sample = json.loads(SAMPLE.read_text(encoding="utf-8"))
        bad = copy.deepcopy(sample)
        bad["periods"][1]["contribution_units"] = -1
        with self.assertRaises(FundingError):
            simulate(bad)
        bad = copy.deepcopy(sample)
        bad["periods"][0]["recipients"] = True
        with self.assertRaises(FundingError):
            simulate(bad)
        bad = copy.deepcopy(sample)
        bad["periods"][1]["label"] = bad["periods"][0]["label"]
        with self.assertRaises(FundingError):
            simulate(bad)


if __name__ == "__main__":
    unittest.main()
