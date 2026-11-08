"""Two assurance-boundary checks; neither asserts physical ownership."""

import unittest

from compare_books import AssuranceInputError, compare_books
from stock_flow import StockFlow


def baseline():
    model = StockFlow()
    model.deposit_assumed_verified("Frank", "Cu", 10, "SYNTHETIC-DEPOSIT")
    return model.events


def inventory(quantity):
    return {
        "declared_evidence_source": "SYNTHETIC",
        "lots": [{"id": "LOT-A", "metal": "Cu", "quantity": quantity, "encumbered": False}],
    }


class CompareBooksTests(unittest.TestCase):
    def test_valid_hash_chain_cannot_hide_missing_physical_inventory(self):
        report = compare_books(
            baseline(), inventory(8), {"Au": 0, "Ag": 0, "Cu": 0}
        )
        self.assertFalse(report["mathematical_coverage_of_declared_inventory"])
        self.assertEqual(report["uncovered_by_declared_inventory"]["Cu"], 2)
        self.assertEqual(report["audit_conclusion"], "UNVERIFIED_PHYSICAL_AND_LEGAL_BACKING")

    def test_encumbered_metal_is_disclosed_but_never_counted_as_backing(self):
        # A nominally sufficient gross stock is not sufficient collateral
        # when part of the inventory is pledged or otherwise encumbered.
        lots = inventory(8)
        lots["lots"].append({
            "id": "PLEDGED-LOT", "metal": "Cu",
            "quantity": 5, "encumbered": True,
        })
        report = compare_books(
            baseline(), lots, {"Au": 0, "Ag": 0, "Cu": 0}
        )
        self.assertEqual(report["declared_gross_lot_quantities"]["Cu"], 13)
        self.assertEqual(report["declared_encumbered_lot_quantities_excluded"]["Cu"], 5)
        self.assertEqual(report["declared_unencumbered_lot_quantities"]["Cu"], 8)
        self.assertEqual(report["uncovered_by_declared_inventory"]["Cu"], 2)
        self.assertFalse(report["mathematical_coverage_of_declared_inventory"])
        self.assertFalse(report["physical_assets_independently_verified"])

    def test_arithmetic_coverage_never_certifies_audits_or_extra_claims(self):
        report = compare_books(
            baseline(), inventory(10), {"Au": 0, "Ag": 0, "Cu": 0}
        )
        self.assertTrue(report["mathematical_coverage_of_declared_inventory"])
        self.assertFalse(report["physical_assets_independently_verified"])
        self.assertFalse(report["liability_completeness_verified"])
        other = compare_books(
            baseline(), inventory(10), {"Au": 0, "Ag": 0, "Cu": 3}
        )
        self.assertEqual(other["uncovered_by_declared_inventory"]["Cu"], 3)
        duplicate = inventory(10)
        duplicate["lots"].append(dict(duplicate["lots"][0]))
        with self.assertRaises(AssuranceInputError):
            compare_books(baseline(), duplicate, {"Au": 0, "Ag": 0, "Cu": 0})


if __name__ == "__main__":
    unittest.main()
