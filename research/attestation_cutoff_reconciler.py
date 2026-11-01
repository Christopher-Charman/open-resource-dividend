"""Evaluate a specific accountant's PAXG reserve report WITHOUT inflating assurance.

The file describes publicly published, externally examined *management
assertions*. Its hash pins the source PDF; this is not a KPMG digital signature.
No chain balances, vault contents or property rights are proven by arithmetic.
The program distinguishes a matched internal report table from independent
multi-chain token supply at exactly the same report cutoff.

Python 3.10+ standard library; local inputs only; no transactions or wallet.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

DEFAULT = Path(__file__).resolve().parent / "observations" / "paxg_kpmg_2026_09_30.json"
NETWORKS = {"Ethereum", "Solana", "Robinhood", "Base"}


class ReconciliationError(ValueError):
    """Unusable published table or timing provenance."""


def quantity(value: object) -> Decimal:
    if not isinstance(value, str):
        raise ReconciliationError("quantities must be exact decimal strings")
    try:
        x = Decimal(value)
    except InvalidOperation as exc:
        raise ReconciliationError("invalid decimal quantity") from exc
    if not x.is_finite() or x < 0:
        raise ReconciliationError("negative or nonfinite amount")
    return x


def moment(value: object) -> datetime:
    if not isinstance(value, str):
        raise ReconciliationError("timestamp must be a string")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ReconciliationError("invalid reporting timestamp") from exc
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ReconciliationError("report and observation timestamps need timezone offsets")
    return dt.astimezone(timezone.utc)


def _check_pdf(report: dict, file: Path | None) -> bool | None:
    if file is None:
        return None
    b = file.read_bytes()
    if not b.startswith(b"%PDF") or len(b) != report["bytes"]:
        raise ReconciliationError("supplied PDF bytes do not match observed source size")
    if hashlib.sha256(b).hexdigest() != report["sha256"]:
        raise ReconciliationError("the supplied PDF has a different SHA256")
    return True


def reconcile(doc: dict, pdf: Path | None = None) -> dict:
    if not isinstance(doc, dict) or doc.get("schema_version") != 1:
        raise ReconciliationError("unsupported evidence record")
    report = doc["report"]
    if report.get("accountant") != "KPMG LLP" or report.get("issuer") != "Paxos Trust Company, National Association":
        raise ReconciliationError("unexpected accountant or issuer scope")
    if report.get("sha256") is None or len(report["sha256"]) != 64:
        raise ReconciliationError("PDF digest missing")
    as_of = moment(report["as_of_utc"])
    if as_of.isoformat() != "2026-09-30T21:00:00+00:00":
        raise ReconciliationError("unexpected reporting cutoff; avoid comparison across dates")
    if datetime.fromisoformat(report["accountant_report_date"]).date() < as_of.date():
        raise ReconciliationError("report signed before its cutoff")

    chains = report["chains"]
    if not isinstance(chains, list) or len(chains) != 4 or {x["name"] for x in chains} != NETWORKS:
        raise ReconciliationError("all four reported network rows required")
    for c in chains:
        if not isinstance(c.get("contract"), str) or not c["contract"]:
            raise ReconciliationError("missing network-specific token contract")
    row_sum = sum((quantity(x["tokens"]) for x in chains), Decimal(0))
    liabilities = quantity(report["reported_redeemable_tokens"])
    reserves = quantity(report["reported_redemption_assets_fine_troy_oz"])
    surplus = quantity(report["reported_surplus_fine_troy_oz"])
    timing = quantity(report["reported_unprocessed_timing_difference"])
    if row_sum != liabilities:
        raise ReconciliationError("reported chain rows do not sum to issued liabilities")
    if reserves - liabilities + timing != surplus:
        raise ReconciliationError("report tables disagree on the stated reserve surplus")

    header = doc["public_chain_header_evidence"]
    if header.get("chain") != "Ethereum" or header.get("chain_id") != 1:
        raise ReconciliationError("header must be independent Ethereum-mainnet evidence")
    prev, next_ = header["cutoff_previous_block"], header["cutoff_next_block"]
    prev_time, next_time = moment(prev["timestamp_utc"]), moment(next_["timestamp_utc"])
    if not (prev_time <= as_of < next_time and
            type(prev["number"]) is int and type(next_["number"]) is int
            and next_["number"] == prev["number"] + 1 and
            len(set(header["observed_from"])) >= 2 and
            header.get("block_hash_and_timestamp_agreed") is True):
        raise ReconciliationError("observed chain headers do not bracket report cutoff")
    if not all(isinstance(row["hash"], str) and len(row["hash"]) == 66 for row in (prev, next_)):
        raise ReconciliationError("block hash evidence not well formed")

    pdf_match = _check_pdf(report, pdf)
    actual_chain_observations = doc.get("independent_cutoff_token_supply", {})
    if not isinstance(actual_chain_observations, dict):
        raise ReconciliationError("invalid chain evidence form")
    # Do not accept arbitrary manifest statements as live independent
    # chain evidence. This tool performs ZERO network reads itself.
    if actual_chain_observations:
        raise ReconciliationError(
            "this local-only reader cannot authenticate network token observations"
        )

    return {
        "evidence_level": "ACCOUNTANT_REPORT_TABLE_CHECK_ONLY",
        "report_as_of_utc": as_of.isoformat(),
        "accountant_signed_report_date": report["accountant_report_date"],
        "accountant_opinion_scope": report["accountant_opinion_scope"],
        "source_pdf_sha256": report["sha256"],
        "source_pdf_hash_locally_reverified": pdf_match,
        "reported_ethereum_tokens": str(quantity(next(x["tokens"] for x in chains if x["name"] == "Ethereum"))),
        "reported_other_network_tokens": {x["name"]: str(quantity(x["tokens"])) for x in chains if x["name"] != "Ethereum"},
        "reported_total_liabilities_tokens": str(liabilities),
        "reported_gold_assets_fine_troy_ounces": str(reserves),
        "reported_surplus_fine_troy_ounces": str(surplus),
        "report_internal_arithmetic_reconciles": True,
        "ethereum_cutoff_block_header_bracketed_by_two_node_claims": True,
        "ethereum_cutoff_last_block": prev["number"],
        "cutoff_supply_observed_independently_on_each_network": False,
        "reported_metal_independently_inspected_by_this_tool": False,
        "legal_title_or_unencumbered_reserves_verified_by_this_tool": False,
        "cross_date_october_supply_comparison_permitted": False,
        "conclusion": "PUBLISHED_REPORT_ARITHMETIC_ONLY_CHAIN_SUPPLY_UNRECONCILED",
        "reason": "Report's four-network total matches its gold assets. The historical Ethereum block headers bracket the cutoff, but no independently fetched historical token supply for all networks or physical assay is included.",
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--manifest", type=Path, default=DEFAULT)
    ap.add_argument("--source-pdf", type=Path, help="optional downloaded original for hash verification")
    args = ap.parse_args()
    print(json.dumps(
        reconcile(json.loads(args.manifest.read_text(encoding="utf-8")), args.source_pdf),
        indent=2, sort_keys=True,
    ))


if __name__ == "__main__":
    main()
