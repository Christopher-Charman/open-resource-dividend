"""Only substantive assurance boundaries: report consistency, cutoff, omissions."""

import copy
import json
import unittest
from pathlib import Path

from attestation_cutoff_reconciler import ReconciliationError, reconcile

FILE = Path(__file__).resolve().parent / "observations" / "paxg_kpmg_2026_09_30.json"


def snapshot():
    return json.loads(FILE.read_text(encoding="utf-8"))


class SeptemberAttestationTests(unittest.TestCase):
    def test_actual_four_network_report_consistent_but_not_chain_verified(self):
        out = reconcile(snapshot())
        self.assertTrue(out["report_internal_arithmetic_reconciles"])
        self.assertEqual(out["reported_total_liabilities_tokens"], "435306")
        self.assertEqual(out["reported_gold_assets_fine_troy_ounces"], "435306")
        self.assertEqual(out["reported_other_network_tokens"], {
            "Solana": "2560", "Robinhood": "5", "Base": "235",
        })
        self.assertEqual(out["ethereum_cutoff_last_block"], 26092843)
        self.assertFalse(out["cutoff_supply_observed_independently_on_each_network"])
        self.assertFalse(out["legal_title_or_unencumbered_reserves_verified_by_this_tool"])
        self.assertIsNone(out["source_pdf_hash_locally_reverified"])

    def test_omitted_network_or_inflated_reserves_does_not_pass(self):
        inp = snapshot()
        inp["report"]["chains"] = inp["report"]["chains"][:3]
        with self.assertRaises(ReconciliationError):
            reconcile(inp)
        inp = snapshot()
        inp["report"]["reported_redemption_assets_fine_troy_oz"] = "500000"
        with self.assertRaises(ReconciliationError):
            reconcile(inp)
        inp = snapshot()
        inp["report"]["chains"][1]["tokens"] = "0"
        with self.assertRaises(ReconciliationError):
            reconcile(inp)

    def test_wrong_cutoff_or_unverified_manually_entered_observations_rejected(self):
        inp = snapshot()
        inp["public_chain_header_evidence"]["cutoff_next_block"]["timestamp_utc"] = "2026-09-30T20:59:59+00:00"
        with self.assertRaises(ReconciliationError):
            reconcile(inp)
        inp = snapshot()
        inp["independent_cutoff_token_supply"] = {"Ethereum": "432506"}
        with self.assertRaises(ReconciliationError):
            reconcile(inp)


if __name__ == "__main__":
    unittest.main()
