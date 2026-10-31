"""Three focused tests for issuer-neutral claims (not a financial system)."""

import copy
import json
import unittest
from pathlib import Path

from issuer_neutral_distribution import ManifestError, evaluate

FIXTURE = Path(__file__).resolve().parent / "scenarios" / "issuer_neutral.json"
CU = "SYN-CU-VAULT-A"
AU = "SYN-AU-VAULT-B"


def sample():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


class IssuerNeutralResearchTests(unittest.TestCase):
    def test_funded_two_issuer_example_and_no_ord_mint(self):
        result = evaluate(sample())
        self.assertFalse(result["ord_issued_new_claims"])
        self.assertFalse(result["transfer_ownership_or_authority_signatures_verified"])
        self.assertFalse(result["cross_issuer_fungibility_assumed"])
        self.assertEqual(result["assets"][CU]["post_assumed_liabilities"], 995)
        self.assertEqual(result["assets"][AU]["post_assumed_liabilities"], 120)
        self.assertEqual(result["assets"][CU]["declared_arithmetic_deficit"], 0)
        self.assertFalse(result["assets"][CU]["physical_reserves_verified"])
        pairs = {(x["asset_id"], x["account"]): x["units"] for x in result["ending_balances"]}
        self.assertEqual(pairs[(CU, "Frank")], 16)
        self.assertEqual(pairs[(CU, "Bob")], 9)
        self.assertEqual(pairs[(AU, "Frank")], 8)
        self.assertEqual(pairs[(CU, "universal-fund")], 30)

    def test_rejects_unfunded_or_cross_issuer_substitution(self):
        source = sample()
        unfunded = copy.deepcopy(source)
        unfunded["events"][2]["units_each"] = 31  # 3*31 exceeds contributed 90
        with self.assertRaises(ManifestError):
            evaluate(unfunded)
        wrong_asset = copy.deepcopy(source)
        wrong_asset["events"][2]["asset_id"] = AU  # fund has only 24 Au units
        with self.assertRaises(ManifestError):
            evaluate(wrong_asset)
        minted = copy.deepcopy(source)
        minted["events"].append({"type": "ord_mint", "asset_id": CU, "units": 999})
        with self.assertRaises(ManifestError):
            evaluate(minted)
        # An alternate asset ID cannot count the same declared title twice.
        duplicated = copy.deepcopy(source)
        twin = dict(duplicated["assets"][0])
        twin["asset_id"] = "SYN-SECOND-ID-SAME-COLLATERAL"
        duplicated["assets"].append(twin)
        with self.assertRaises(ManifestError):
            evaluate(duplicated)

    def test_pending_redemption_is_a_liability_and_no_duplicate_resolution(self):
        waiting = sample()
        waiting["events"] = waiting["events"][:7]
        result = evaluate(waiting)
        self.assertEqual(result["assets"][AU]["post_assumed_liabilities"], 120)
        self.assertEqual(result["assets"][AU]["locked_pending_claim_units"], 2)
        self.assertEqual(result["open_redemption_requests"]["synthetic-gold-redemption-1"]["units"], 2)
        duplicate = sample()
        duplicate["events"].append({
            "type": "cancel_redemption",
            "request_id": "synthetic-copper-redemption-1",
        })
        with self.assertRaises(ManifestError):
            evaluate(duplicate)


if __name__ == "__main__":
    unittest.main()
