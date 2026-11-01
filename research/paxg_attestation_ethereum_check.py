"""Recheck September 2026 PAXG Ethereum supply using two LIVE archive RPCs.

This is intentionally a network-read-only extension to the locally verified
KPMG report: it does not sign anything, trade, invoke an issuer, or attest
physical bullion. The September report's whole-token presentation policy is
not specified sufficiently to claim exact six-decimal agreement.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from attestation_cutoff_reconciler import DEFAULT, ReconciliationError, reconcile
from paxg_chain_observer import PAXG_ETHEREUM, observe

ARCHIVE_NODES = (
    "https://eth-mainnet.g.alchemy.com/public",
    "https://eth.drpc.org",
)


def check_live_ethereum(report: dict, endpoints: tuple[str, str] = ARCHIVE_NODES,
                        pdf: Path | None = None) -> dict:
    """Require actual independent historical RPC reads, never arbitrary JSON."""
    base = reconcile(report, pdf)
    header = report["public_chain_header_evidence"]["cutoff_previous_block"]
    result = observe(nodes=endpoints, block=header["number"])
    if (result["ethereum_chain_id"] != 1
            or result["block_hash"] != header["hash"]
            or result["block_timestamp_utc"] != header["timestamp_utc"]
            or result["contract_address"].lower() != PAXG_ETHEREUM.lower()
            or result.get("node_agreement") is not True
            or len(result["node_observations"]) != 2
            or len({x["rpc_host"] for x in result["node_observations"]}) != 2
            or result["node_observations"][0]["decimals"] != 18
            or result["node_observations"][1]["decimals"] != 18):
        raise ReconciliationError("historical Ethereum RPC result does not match pinned cutoff")

    reported = Decimal(base["reported_ethereum_tokens"])
    observed = Decimal(result["supply_token_units"])
    if not observed.is_finite() or observed < 0:
        raise ReconciliationError("invalid independently observed supply")
    # This is an explicit HYPOTHESIS for interpreting a report that displays
    # whole token units. It is NOT a demonstrated KPMG rounding policy.
    nearest = observed.quantize(Decimal(1), rounding=ROUND_HALF_UP)
    compatible = nearest == reported
    return {
        "scope": "INDEPENDENT_ETHEREUM_HISTORICAL_SUPPLY_ONLY",
        "report_as_of_utc": base["report_as_of_utc"],
        "accountant_report_file_sha256": base["source_pdf_sha256"],
        "source_pdf_hash_locally_reverified": base["source_pdf_hash_locally_reverified"],
        "historical_ethereum_block": result["block_number"],
        "historical_ethereum_block_hash": result["block_hash"],
        "historical_ethereum_supply_paxg": str(observed),
        "report_ethereum_whole_tokens": str(reported),
        "observed_minus_report_in_tokens": str(observed - reported),
        "observed_rounded_nearest_whole_token": str(nearest),
        "compatible_with_hypothetical_nearest_whole_reporting": compatible,
        "report_uses_nearest_whole_rounding_independently_established": False,
        "ethereum_historical_rpc_node_agreement": True,
        "ethereum_rpc_hosts": [x["rpc_host"] for x in result["node_observations"]],
        "other_chains_reported_not_verified": base["reported_other_network_tokens"],
        "all_four_networks_independently_reconciled": False,
        "physical_reserves_verified_by_ord": False,
        "legal_property_or_delivery_verified_by_ord": False,
        "conclusion": ("ETHEREUM_MATCHES_HYPOTHETICAL_WHOLE_TOKEN_PRESENTATION_ONLY"
                       if compatible else "ETHEREUM_DISCREPANCY_REQUIRES_INVESTIGATION"),
        "warning": "Ethereum historical chain state is independently corroborated. "
                   "KPMG whole-token presentation/rounding is unconfirmed. "
                   "Other chains, custody, legal title and all liabilities are NOT independently verified by ORD.",
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--manifest", type=Path, default=DEFAULT)
    ap.add_argument("--source-pdf", type=Path)
    ap.add_argument("--rpc-a", default=ARCHIVE_NODES[0])
    ap.add_argument("--rpc-b", default=ARCHIVE_NODES[1])
    args = ap.parse_args()
    source = json.loads(args.manifest.read_text(encoding="utf-8"))
    print(json.dumps(check_live_ethereum(
        source, (args.rpc_a, args.rpc_b), args.source_pdf
    ), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
