"""One verified boundary and two genuinely different failure modes."""

import copy
import json
import unittest
from pathlib import Path
from unittest.mock import patch

from attestation_cutoff_reconciler import ReconciliationError
from paxg_attestation_ethereum_check import check_live_ethereum

HERE = Path(__file__).resolve().parent
REPORT = HERE / "observations" / "paxg_kpmg_2026_09_30.json"
OBSERVED = HERE / "observations" / "paxg_ethereum_block_26092843.json"


def records():
    return json.loads(REPORT.read_text()), json.loads(OBSERVED.read_text())


class HistoricalEthereumTests(unittest.TestCase):
    def test_report_whole_token_figures_vs_real_pinned_snapshot(self):
        report, observation = records()
        with patch("paxg_attestation_ethereum_check.observe", return_value=observation):
            result = check_live_ethereum(report)
        self.assertEqual(result["historical_ethereum_supply_paxg"], "432505.935219")
        self.assertEqual(result["observed_minus_report_in_tokens"], "-0.064781")
        self.assertTrue(result["compatible_with_hypothetical_nearest_whole_reporting"])
        self.assertFalse(result["report_uses_nearest_whole_rounding_independently_established"])
        self.assertFalse(result["all_four_networks_independently_reconciled"])

    def test_wrong_block_hash_cannot_be_reconciled(self):
        report, observation = records()
        wrong = copy.deepcopy(observation)
        wrong["block_hash"] = "0x" + "f"*64
        with patch("paxg_attestation_ethereum_check.observe", return_value=wrong):
            with self.assertRaises(ReconciliationError):
                check_live_ethereum(report)

    def test_material_shortfall_is_not_silently_rounded_away(self):
        report, observation = records()
        changed = copy.deepcopy(observation)
        changed["supply_token_units"] = "432499.5"
        with patch("paxg_attestation_ethereum_check.observe", return_value=changed):
            result = check_live_ethereum(report)
        self.assertFalse(result["compatible_with_hypothetical_nearest_whole_reporting"])
        self.assertEqual(result["conclusion"], "ETHEREUM_DISCREPANCY_REQUIRES_INVESTIGATION")


if __name__ == "__main__":
    unittest.main()
