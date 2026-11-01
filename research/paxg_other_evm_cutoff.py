"""Independent historical ERC-20 observation for PAXG on non-Ethereum EVM chains.

This is read-only chain-state evidence, NOT independent bullion custody, title,
redemption or all-network solvency evidence. Only fixed allowlisted RPC methods
are used. Supply is matched at the accountant's precise UTC report cutoff.
Python stdlib only; no wallets, passwords or installed chain SDK.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from urllib.parse import urlsplit

from paxg_chain_observer import ObservationError, read_rpc

CUTOFF = datetime.fromisoformat("2026-09-30T21:00:00+00:00")
CONFIG = {
    "Base": {
        "chain_id": 8453,
        "contract": "0xe904AEA5E1b110c9174728fA2efFc8aeD19E98Ef",
        "prior_block": 52006326,
        "reported_whole_tokens": "235",
        "nodes": ("https://base-mainnet.g.alchemy.com/public", "https://base.drpc.org"),
    },
    "Robinhood": {
        "chain_id": 4663,
        "contract": "0x121BbE58fe4684057FB66d2dd535A19e16B4f66F",
        "prior_block": 76821239,
        "reported_whole_tokens": "5",
        # Three independent public operators were observed agreeing on
        # historic block, supply, decimals and code at this exact cutoff.
        # Use two of them by default; Pocket can independently cross-check.
        "nodes": ("https://robinhood.rpc.pinax.network", "https://robinhood.drpc.org"),
    },
}


def parse_block(value: object, height: int) -> dict:
    if not isinstance(value, dict) or int(value["number"], 16) != height:
        raise ObservationError("invalid or incorrect block header")
    h = value["hash"]
    if not isinstance(h, str) or len(h) != 66 or not h.startswith("0x"):
        raise ObservationError("invalid block hash")
    timestamp = datetime.fromtimestamp(int(value["timestamp"], 16), timezone.utc)
    return {"height": height, "hash": h, "timestamp": timestamp}


def observe_chain(chain: str, nodes: tuple[str, str] | None = None) -> dict:
    if chain not in CONFIG:
        raise ObservationError("unsupported reported EVM network")
    cfg = CONFIG[chain]
    endpoints = cfg["nodes"] if nodes is None else nodes
    if (endpoints is None or len(endpoints) != 2 or
        len(set(urlsplit(u).hostname for u in endpoints)) != 2):
        raise ObservationError("two separate independently operated RPC hosts required")
    reference = None
    results = []
    for url in endpoints:
        chain_id = int(read_rpc(url, "eth_chainId", []), 16)
        if chain_id != cfg["chain_id"]:
            raise ObservationError("wrong EVM chain ID")
        height = cfg["prior_block"]
        prev = parse_block(read_rpc(url, "eth_getBlockByNumber", [hex(height), False]), height)
        after = parse_block(read_rpc(url, "eth_getBlockByNumber", [hex(height + 1), False]), height + 1)
        if not (prev["timestamp"] < CUTOFF <= after["timestamp"]):
            raise ObservationError("blocks do not bracket accountant report cutoff")
        if reference is None:
            reference = (prev["hash"], after["hash"], prev["timestamp"], after["timestamp"])
        elif reference != (prev["hash"], after["hash"], prev["timestamp"], after["timestamp"]):
            raise ObservationError("RPC operators disagree on cutoff blocks")
        raw_supply = read_rpc(
            url, "eth_call", [{"to": cfg["contract"], "data": "0x18160ddd"}, hex(height)]
        )
        raw_decimals = read_rpc(
            url, "eth_call", [{"to": cfg["contract"], "data": "0x313ce567"}, hex(height)]
        )
        if (not isinstance(raw_supply, str) or len(raw_supply) != 66
            or not isinstance(raw_decimals, str) or len(raw_decimals) != 66):
            raise ObservationError("invalid ABI return length")
        supply = int(raw_supply, 16)
        decimals = int(raw_decimals, 16)
        if decimals > 36:
            raise ObservationError("invalid decimals value")
        code = read_rpc(url, "eth_getCode", [cfg["contract"], hex(height)])
        if not isinstance(code, str) or not code.startswith("0x") or len(code) <= 2:
            raise ObservationError("missing contract code")
        try:
            code_hash = hashlib.sha256(bytes.fromhex(code[2:])).hexdigest()
        except ValueError as exc:
            raise ObservationError("invalid contract bytecode") from exc
        results.append({
            "host": urlsplit(url).hostname,
            "supply_atomic": str(supply), "decimals": decimals,
            "code_size_bytes": (len(code) - 2) // 2, "code_sha256": code_hash,
        })

    comparable = lambda r: (r["supply_atomic"], r["decimals"], r["code_size_bytes"], r["code_sha256"])
    if comparable(results[0]) != comparable(results[1]):
        raise ObservationError("independent nodes disagreed on contract state")
    actual = Decimal(results[0]["supply_atomic"]) / 10 ** results[0]["decimals"]
    displayed = Decimal(cfg["reported_whole_tokens"])
    return {
        "scope": "INDEPENDENT_EVM_TOKEN_SUPPLY_AT_KPMG_CUTOFF_ONLY",
        "chain": chain,
        "chain_id": cfg["chain_id"],
        "token_address": cfg["contract"],
        "cutoff_utc": CUTOFF.isoformat(),
        "prior_block": cfg["prior_block"],
        "prior_hash": reference[0],
        "prior_timestamp_utc": reference[2].isoformat(),
        "next_block": cfg["prior_block"] + 1,
        "next_hash": reference[1],
        "next_timestamp_utc": reference[3].isoformat(),
        "token_supply_exact": format(actual, "f"),
        "reported_whole_tokens": format(displayed, "f"),
        "difference_to_displayed_tokens": format(actual - displayed, "f"),
        "compatible_with_hypothetical_nearest_whole_rounding": (
            actual.quantize(Decimal("1"), rounding=ROUND_HALF_UP) == displayed
        ),
        "report_rounding_policy_confirmed": False,
        "two_operator_state_agreement": True,
        "rpc_observations": results,
        "independent_bullion_or_legal_title_proven": False,
        "all_four_networks_verified": False,
        "no_wallet_or_transaction_access": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chain", choices=sorted(CONFIG), default="Base")
    parser.add_argument("--rpc-a")
    parser.add_argument("--rpc-b")
    args = parser.parse_args()
    if bool(args.rpc_a) != bool(args.rpc_b):
        parser.error("provide both independent RPC endpoints or neither")
    urls = (args.rpc_a, args.rpc_b) if args.rpc_a else None
    print(json.dumps(observe_chain(args.chain, urls), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
