"""Independent current Solana PAXG mint-rights observer; NOT historic audit proof.

Uses only Solana public read methods. Two independently operated RPC nodes
must agree on genesis, Token-2022 mint, six-decimal supply and controller keys.
The result is a CONTEMPORANEOUS snapshot, never the Sep 2026 KPMG cutoff.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

MINT = "5GgRAEmv8ZxF2PR5hY72Qs5x1bnQ6UK2RbTPoqJ3wSwW"
TOKEN_2022 = "TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb"
GENESIS = "5eykt4UsFv8P8NJdTREpY1vzqKqZKvdpKuc147dw2N9d"
NODES = ("https://api.mainnet-beta.solana.com", "https://solana.api.pocket.network")
METHODS = {"getGenesisHash", "getTokenSupply", "getAccountInfo"}


class MintEvidenceError(ValueError):
    pass


def rpc(url: str, method: str, params: list) -> object:
    parts = urlsplit(url)
    if (parts.scheme != "https" or not parts.hostname or parts.username
            or parts.password or parts.query or parts.fragment or method not in METHODS):
        raise MintEvidenceError("unsupported endpoint or method")
    req = Request(
        url,
        data=json.dumps({"jsonrpc": "2.0", "id": 27, "method": method, "params": params}).encode(),
        headers={"Content-Type": "application/json", "User-Agent": "ORD open read-only evidence"},
        method="POST",
    )
    try:
        with urlopen(req, timeout=18) as response:
            obj = json.load(response)
    except (OSError, ValueError) as exc:
        raise MintEvidenceError("RPC retrieval failed: " + type(exc).__name__) from exc
    if (not isinstance(obj, dict) or obj.get("id") != 27
            or "error" in obj or "result" not in obj):
        raise MintEvidenceError("provider returned error or malformed result")
    return obj["result"]


def evaluate(nodes: tuple[str, str] = NODES) -> dict:
    if (len(nodes) != 2 or
            len({urlsplit(x).hostname for x in nodes}) != 2):
        raise MintEvidenceError("two independent RPC hostnames required")
    observations = []
    for node in nodes:
        if rpc(node, "getGenesisHash", []) != GENESIS:
            raise MintEvidenceError("not Solana mainnet")
        supply = rpc(node, "getTokenSupply", [MINT, {"commitment": "finalized"}])
        account = rpc(node, "getAccountInfo", [MINT, {"commitment": "finalized",
                                                    "encoding": "jsonParsed"}])
        if not isinstance(supply, dict) or not isinstance(account, dict):
            raise MintEvidenceError("RPC result malformed")
        value = account.get("value")
        if not isinstance(value, dict) or value.get("owner") != TOKEN_2022:
            raise MintEvidenceError("mint not owned by Solana Token-2022 program")
        parsed = value.get("data", {}).get("parsed", {})
        if parsed.get("type") != "mint":
            raise MintEvidenceError("not a mint account")
        info = parsed.get("info", {})
        mint_amount = info.get("supply")
        qty = supply.get("value", {})
        if (not isinstance(mint_amount, str) or not mint_amount.isdigit()
                or qty.get("amount") != mint_amount or info.get("decimals") != 6
                or qty.get("decimals") != 6):
            raise MintEvidenceError("mint and token-supply results disagree")
        extensions = {}
        for entry in info.get("extensions", []):
            kind = entry.get("extension")
            if kind in ("permanentDelegate", "transferHook", "transferFeeConfig",
                        "mintCloseAuthority"):
                if kind in extensions:
                    raise MintEvidenceError("duplicate mint extension")
                extensions[kind] = entry.get("state")
        delegate = extensions.get("permanentDelegate", {}).get("delegate")
        if not isinstance(delegate, str) or not delegate:
            raise MintEvidenceError("no observable permanent delegate")
        transfer_hook = extensions.get("transferHook", {})
        fees = extensions.get("transferFeeConfig", {})
        observation = {
            "host": urlsplit(node).hostname,
            "supply_slot": supply["context"]["slot"],
            "mint_account_slot": account["context"]["slot"],
            "atomic_supply": mint_amount,
            "decimals": 6,
            "mint_authority": info.get("mintAuthority"),
            "freeze_authority": info.get("freezeAuthority"),
            "permanent_delegate": delegate,
            "transfer_hook_authority": transfer_hook.get("authority"),
            "transfer_hook_program": transfer_hook.get("programId"),
            "transfer_fee_config_authority": fees.get("transferFeeConfigAuthority"),
            "current_fee_basis_points": fees.get("newerTransferFee", {}).get(
                "transferFeeBasisPoints"
            ),
            "mint_close_authority": extensions.get("mintCloseAuthority", {}).get(
                "closeAuthority"
            ),
        }
        observations.append(observation)
    attrs = ("atomic_supply", "decimals", "mint_authority", "freeze_authority",
             "permanent_delegate", "transfer_hook_authority", "transfer_hook_program",
             "transfer_fee_config_authority", "current_fee_basis_points",
             "mint_close_authority")
    if any(observations[0][key] != observations[1][key] for key in attrs):
        raise MintEvidenceError("independent mint observations disagree")
    return {
        "scope": "CURRENT_SOLANA_MINT_METADATA_ONLY",
        "mint": MINT,
        "token_program": TOKEN_2022,
        "genesis_hash": GENESIS,
        "two_operator_agreement": True,
        "current_supply": format(Decimal(observations[0]["atomic_supply"]) / Decimal(1_000_000), "f"),
        "observations": observations,
        "permanent_delegate_can_transfer_or_burn_without_holder_signature": True,
        "historical_2026_09_30_supply_independently_observed": False,
        "delegate_exercised_or_abused_evidence": False,
        "physical_reserves_or_legal_title_verified": False,
        "no_transaction_or_private_account_access": True,
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--rpc-a", default=NODES[0])
    p.add_argument("--rpc-b", default=NODES[1])
    args = p.parse_args()
    print(json.dumps(evaluate((args.rpc_a, args.rpc_b)), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
