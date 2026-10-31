"""Targeted tests: semantic overclaim, inconsistent provider records and status."""

import copy
import json
import unittest
from pathlib import Path

from provider_transfer_evidence import TransferEvidenceError, assess

FIXTURE = Path(__file__).resolve().parent / "scenarios" / "paxos_transfer_records.json"


def example():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


class TransferEvidenceTests(unittest.TestCase):
    def test_completed_pair_is_not_independently_verified_title(self):
        record = example()
        result = assess(record["intent"], record["transfers"])
        self.assertEqual(result["assessment"], "SUPPLIED_PROVIDER_RECORDS_RECONCILE")
        self.assertTrue(result["observed_in_input"]["paired_completed"])
        self.assertFalse(result["provider_records_independently_retrieved"])
        self.assertFalse(result["underlying_commodity_title_assigned_or_verified"])
        self.assertFalse(result["destination_balance_independently_read_back"])
        self.assertTrue(result["no_live_transfer_attempted"])

    def test_pending_credit_and_missing_credit_are_not_completed(self):
        record = example()
        record["transfers"][1]["status"] = "PENDING"
        result = assess(record["intent"], record["transfers"])
        self.assertEqual(result["assessment"], "RECORDS_INCOMPLETE_OR_NOT_COMPLETED")
        record["transfers"] = record["transfers"][:1]
        result = assess(record["intent"], record["transfers"])
        self.assertFalse(result["observed_in_input"]["paired_completed"])

    def test_ref_group_asset_and_amount_must_not_mismatch(self):
        record = example()
        for field, wrong in (
            ("group_id", "different-group"),
            ("asset", "USDP"),
            ("amount", "0.25"),
            ("profile_id", "other-person"),
        ):
            altered = copy.deepcopy(record)
            altered["transfers"][1][field] = wrong
            with self.subTest(field=field), self.assertRaises(TransferEvidenceError):
                assess(altered["intent"], altered["transfers"])
        altered = copy.deepcopy(record)
        altered["transfers"][0]["ref_id"] = "unrelated-request"
        with self.assertRaises(TransferEvidenceError):
            assess(altered["intent"], altered["transfers"])

    def test_deny_duplicate_records_and_invalid_quantities(self):
        record = example()
        record["transfers"].append(copy.deepcopy(record["transfers"][0]))
        with self.assertRaises(TransferEvidenceError):
            assess(record["intent"], record["transfers"])
        record = example()
        record["transfers"][0]["amount"] = "NaN"
        with self.assertRaises(TransferEvidenceError):
            assess(record["intent"], record["transfers"])


if __name__ == "__main__":
    unittest.main()
