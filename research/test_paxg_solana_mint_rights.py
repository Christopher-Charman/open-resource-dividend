"""Three substantive independent-RPC protections for live Solana mint evidence."""

import copy
import unittest
from unittest.mock import patch

from paxg_solana_mint_rights import GENESIS, MINT, TOKEN_2022, MintEvidenceError, evaluate, rpc

NODES = ("https://first.example", "https://second.example")


def fixture(url, method, params):
    if method == "getGenesisHash":
        return GENESIS
    if method == "getTokenSupply":
        return {"context": {"slot": 463894814}, "value": {
            "amount": "3215284434", "decimals": 6, "uiAmountString": "3215.284434"
        }}
    if method == "getAccountInfo":
        return {"context": {"slot": 463894814}, "value": {
            "owner": TOKEN_2022, "data": {"parsed": {"type": "mint", "info": {
                "decimals": 6, "supply": "3215284434",
                "mintAuthority": "mint-authority", "freezeAuthority": "freeze-authority",
                "extensions": [
                    {"extension": "permanentDelegate", "state": {"delegate": "delegator"}},
                    {"extension": "transferHook", "state": {"authority": "delegator", "programId": None}},
                ],
            }}},
        }}
    raise AssertionError(method)


class SolanaMintResearchTests(unittest.TestCase):
    def test_shared_current_state_is_not_historic_backing(self):
        with patch("paxg_solana_mint_rights.rpc", side_effect=fixture):
            result = evaluate(NODES)
        self.assertEqual(result["current_supply"], "3215.284434")
        self.assertEqual(result["observations"][0]["permanent_delegate"], "delegator")
        self.assertTrue(result["two_operator_agreement"])
        self.assertFalse(result["historical_2026_09_30_supply_independently_observed"])
        self.assertFalse(result["physical_reserves_or_legal_title_verified"])

    def test_rejects_controller_disagreement(self):
        def changed(url, method, params):
            result = fixture(url, method, params)
            if url == NODES[1] and method == "getAccountInfo":
                result = copy.deepcopy(result)
                result["value"]["data"]["parsed"]["info"]["extensions"][0]["state"]["delegate"] = "different"
            return result
        with patch("paxg_solana_mint_rights.rpc", side_effect=changed):
            with self.assertRaises(MintEvidenceError):
                evaluate(NODES)

    def test_refuses_effectful_rpc_and_duplicate_provider(self):
        with self.assertRaises(MintEvidenceError):
            evaluate((NODES[0], NODES[0]))
        with self.assertRaises(MintEvidenceError):
            rpc(NODES[0], "sendTransaction", ["base64-payload"])


if __name__ == "__main__":
    unittest.main()
