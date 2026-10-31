"""Focused tests of the illustrative accounting model; no hosted CI needed."""

import unittest

from stock_flow import FundingError, StockFlow, demonstration


class ConservationTests(unittest.TestCase):
    def test_complete_exchange_example(self):
        summary = demonstration()
        self.assertEqual(summary["assumed_copper_reserve_units"], 998)
        self.assertEqual(summary["outstanding_copper_claim_units"], 998)
        self.assertEqual(summary["fund_copper_claim_units"], 100)
        self.assertEqual(summary["frank_copper_claim_units"], 4)
        self.assertEqual(summary["bob_copper_claim_units"], 7)

    def test_no_unfunded_payout_or_duplicate_deposit(self):
        ledger = StockFlow()
        ledger.deposit_assumed_verified("Alice", "Ag", 12, "RECEIPT-A")
        with self.assertRaises(FundingError):
            ledger.deposit_assumed_verified("Alice", "Ag", 12, "RECEIPT-A")
        ledger.transfer("Alice", "pool", "Ag", 12)
        with self.assertRaises(FundingError):
            ledger.dividend("pool", ["A", "B"], "Ag", 7)
        self.assertEqual(ledger.accounts["pool"]["Ag"], 12)
        ledger.verify()

    def test_redemption_extinguishes_claim_and_detects_log_tamper(self):
        ledger = StockFlow()
        ledger.deposit_assumed_verified("Alice", "Au", 6, "RECEIPT-A")
        ledger.redeem_assumed_delivered("Alice", "Au", 2, "DELIVERY-A")
        self.assertEqual(ledger.reserves["Au"], 4)
        self.assertEqual(ledger.accounts["Alice"]["Au"], 4)
        ledger.events[0]["details"]["quantity"] = 600
        with self.assertRaises(AssertionError):
            ledger.verify()


if __name__ == "__main__":
    unittest.main()
