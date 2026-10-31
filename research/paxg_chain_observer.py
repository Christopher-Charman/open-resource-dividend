"""Read-only two-RPC PAXG ERC-20 supply verifier (research, not reserves proof).

Public Ethereum state can be independently corroborated across two nodes at
the SAME FINALIZED block. No wallet, auth, API key, private data or transactions.
Only five fixed read-only JSON-RPC methods are ever sent. No web3 dependency.
PAXG proxy and methods are grounded in the issuer's official public repo.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from decimal import Decimal
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

PAXG_ETHEREUM = "0x45804880De22913dAFE09f4980848ECE6EcbAf78"
DEFAULT_NODES = ("https://ethereum-rpc.publicnode.com", "https://eth.nodely.dev")
PAXG_REPO = "https://github.com/paxosglobal/paxos-gold-contract"
HEX32 = re.compile(r"^0x[0-9a-fA-F]{64}$")
CODE = re.compile(r"^0x(?:[0-9a-fA-F]{2})+$")
READ_METHODS = {"eth_chainId", "eth_getBlockByNumber", "eth_call", "eth_getCode"}


class ObservationError(ValueError):
    """Independent read failed; do not publish a pass or infer any reserves."""


def _node_url(url: str) -> str:
    parts = urlsplit(url)
    if (parts.scheme != "https" or not parts.hostname or parts.username
            or parts.password or parts.fragment or parts.query):
        raise ObservationError("RPC must be a plain HTTPS URL without credentials")
    return url


def read_rpc(endpoint: str, method: str, params: list) -> object:
    """A fixed read-only allowlist; never submit or sign transactions."""
    if method not in READ_METHODS:
        raise ObservationError("unsupported or effectful RPC method")
    data = json.dumps(
        {"jsonrpc": "2.0", "id": 17, "method": method, "params": params},
        separators=(",", ":"),
    ).encode("utf-8")
    req = Request(
        _node_url(endpoint), data=data, method="POST",
        headers={"Content-Type": "application/json",
                 "User-Agent": "ORD open read-only research"},
    )
    try:
        with urlopen(req, timeout=18) as response:
            result = json.load(response)
    except (OSError, ValueError) as exc:
        raise ObservationError("RPC transport or parse failure: " + type(exc).__name__) from exc
    if (not isinstance(result, dict) or result.get("jsonrpc") != "2.0"
            or result.get("id") != 17 or "error" in result or "result" not in result):
        raise ObservationError("invalid or error RPC response")
    return result["result"]


def _hex_uint(value: object) -> int:
    if not isinstance(value, str) or not value.startswith("0x"):
        raise ObservationError("invalid hexadecimal integer response")
    try:
        n = int(value[2:], 16)
    except ValueError as exc:
        raise ObservationError("malformed hexadecimal response") from exc
    if n < 0:
        raise ObservationError("negative quantity")
    return n


def _word(value: object) -> int:
    if not isinstance(value, str) or HEX32.fullmatch(value) is None:
        raise ObservationError("invalid 32-byte ABI return word")
    return int(value, 16)


def observe(nodes: tuple[str, str] = DEFAULT_NODES, block: int | None = None) -> dict:
    """Match chain, block hash, ERC-20 totalSupply/decimals and deployed bytecode.

    The first node chooses its finalized block unless a historical height is
    provided. The second node MUST serve that exact height. Any mismatch fails.
    """
    if len(nodes) != 2 or len(set(nodes)) != 2 or any(not isinstance(x, str) for x in nodes):
        raise ObservationError("two distinct HTTPS RPC services required")
    for url in nodes:
        _node_url(url)
    if urlsplit(nodes[0]).hostname == urlsplit(nodes[1]).hostname:
        raise ObservationError("independent RPC hostnames required")
    if block is not None and (type(block) is not int or block < 1):
        raise ObservationError("block must be a positive integer")

    tag = hex(block) if block is not None else "finalized"
    lead = read_rpc(nodes[0], "eth_getBlockByNumber", [tag, False])
    if not isinstance(lead, dict) or not isinstance(lead.get("hash"), str):
        raise ObservationError("missing first block metadata")
    height = _hex_uint(lead.get("number"))
    if block is not None and height != block:
        raise ObservationError("first node returned a different block height")
    if HEX32.fullmatch(lead["hash"]) is None:
        raise ObservationError("invalid first block hash")
    timestamp = _hex_uint(lead.get("timestamp"))
    fixed = hex(height)
    responses = []
    for endpoint in nodes:
        if read_rpc(endpoint, "eth_chainId", []) != "0x1":
            raise ObservationError("not Ethereum mainnet")
        row = read_rpc(endpoint, "eth_getBlockByNumber", [fixed, False])
        if not isinstance(row, dict) or (row.get("hash") != lead["hash"]
                or _hex_uint(row.get("number")) != height
                or _hex_uint(row.get("timestamp")) != timestamp):
            raise ObservationError("independent nodes disagree on fixed block")
        total = _word(read_rpc(
            endpoint, "eth_call", [{"to": PAXG_ETHEREUM, "data": "0x18160ddd"}, fixed]
        ))
        decimals = _word(read_rpc(
            endpoint, "eth_call", [{"to": PAXG_ETHEREUM, "data": "0x313ce567"}, fixed]
        ))
        if decimals > 36:
            raise ObservationError("unreasonable ERC-20 decimal precision")
        code = read_rpc(endpoint, "eth_getCode", [PAXG_ETHEREUM, fixed])
        if not isinstance(code, str) or CODE.fullmatch(code) is None:
            raise ObservationError("no valid bytecode at contract address")
        code_hash = hashlib.sha256(bytes.fromhex(code[2:])).hexdigest()
        responses.append({
            "rpc_host": urlsplit(endpoint).hostname,
            "total_supply_atomic_units": str(total),
            "decimals": decimals,
            "code_sha256": code_hash,
            "code_size_bytes": (len(code) - 2) // 2,
        })
    signature = lambda row: (
        row["total_supply_atomic_units"], row["decimals"],
        row["code_sha256"], row["code_size_bytes"]
    )
    if signature(responses[0]) != signature(responses[1]):
        raise ObservationError("RPC providers disagree on supply, precision or code")
    first = responses[0]
    supply = Decimal(first["total_supply_atomic_units"]) / (Decimal(10) ** first["decimals"])
    return {
        "scope": "PUBLIC_ETHEREUM_CHAIN_STATE_ONLY",
        "observed_utc": datetime.now(timezone.utc).isoformat(),
        "ethereum_chain_id": 1,
        "block_number": height,
        "block_hash": lead["hash"],
        "block_timestamp_utc": datetime.fromtimestamp(timestamp, timezone.utc).isoformat(),
        "contract_address": PAXG_ETHEREUM,
        "contract_reference": PAXG_REPO,
        "supply_token_units": format(supply, "f"),
        "node_agreement": True,
        "node_observations": responses,
        "physical_reserves_verified": False,
        "legal_title_verified": False,
        "all_liabilities_verified": False,
        "individual_bar_allocation_verified": False,
        "asset_redemption_verified": False,
        "no_transaction_or_wallet_access": True,
        "warning": "Chain state is NOT evidence of commodity custody, legal ownership or complete obligations.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--block", type=int, help="fixed historical block (requires two archive-capable nodes)")
    parser.add_argument("--rpc-a", default=DEFAULT_NODES[0])
    parser.add_argument("--rpc-b", default=DEFAULT_NODES[1])
    args = parser.parse_args()
    print(json.dumps(observe((args.rpc_a, args.rpc_b), args.block), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
