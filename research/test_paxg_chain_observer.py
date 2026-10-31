"""Only core invariants: same fixed block, independent supply and read-only RPC."""

import unittest
from unittest.mock import patch

from paxg_chain_observer import ObservationError, observe, read_rpc

HOSTS = ("https://node-a.example", "https://node-b.example")
HASH = "0x" + "a" * 64
BLOCK = {"hash": HASH, "number": "0x64", "timestamp": "0x66"}
SUPPLY = "0x" + format(125 * 10**18, "064x")
PRECISION = "0x" + format(18, "064x")


def fake_rpc(endpoint, method, params):
    if method == "eth_chainId":
        return "0x1"
    if method == "eth_getBlockByNumber":
        return BLOCK
    if method == "eth_getCode":
        return "0x60006001"
    if method == "eth_call":
        return PRECISION if params[0]["data"] == "0x313ce567" else SUPPLY
    raise AssertionError("unexpected RPC method " + method)


class PublicSupplyTests(unittest.TestCase):
    def test_two_nodes_agree_and_no_commodity_proof(self):
        with patch("paxg_chain_observer.read_rpc", side_effect=fake_rpc):
            result = observe(HOSTS, 100)
        self.assertEqual(result["supply_token_units"], "125")
        self.assertTrue(result["node_agreement"])
        self.assertEqual(result["block_number"], 100)
        self.assertFalse(result["physical_reserves_verified"])
        self.assertFalse(result["legal_title_verified"])
        self.assertFalse(result["all_liabilities_verified"])
        self.assertTrue(result["no_transaction_or_wallet_access"])

    def test_conflicting_supply_is_rejected_not_averaged(self):
        def conflicting(endpoint, method, params):
            if endpoint == HOSTS[1] and method == "eth_call" and params[0]["data"] == "0x18160ddd":
                return "0x" + format(126 * 10**18, "064x")
            return fake_rpc(endpoint, method, params)

        with patch("paxg_chain_observer.read_rpc", side_effect=conflicting):
            with self.assertRaisesRegex(ObservationError, "disagree"):
                observe(HOSTS, 100)

    def test_rejects_same_node_or_transaction_method(self):
        with self.assertRaises(ObservationError):
            observe((HOSTS[0], HOSTS[0]), 100)
        with self.assertRaises(ObservationError):
            read_rpc(HOSTS[0], "eth_sendRawTransaction", ["0xdeadbeef"])


if __name__ == "__main__":
    unittest.main()
