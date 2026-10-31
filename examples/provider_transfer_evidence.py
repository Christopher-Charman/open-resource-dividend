"""Paxos v2 *record-shape* reconciliation, never an authenticated transfer.

This uses only documented field names from Paxos Create/Get/List Transfer APIs.
Inputs are local JSON declarations, which anyone can forge. Even matching
COMPLETED debit/credit records do NOT prove recipient legal title or physical
redemption, and no API request, wallet mutation, key or account is used.

For rights-bearing commodity claims, successful token movement is necessary
evidence in some designs but cannot independently establish property rights.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

FIXTURE = Path(__file__).resolve().parent / "scenarios" / "paxos_transfer_records.json"


class TransferEvidenceError(ValueError):
    """Unusable, inconsistent or overstated provider-transfer record."""


def _name(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise TransferEvidenceError("identifier must be a nonempty string")
    return value


def _amount(value: object) -> Decimal:
    # An API decimal must not silently turn into a binary float.
    if not isinstance(value, str):
        raise TransferEvidenceError("amount must be a decimal string")
    try:
        amount = Decimal(value)
    except InvalidOperation as exc:
        raise TransferEvidenceError("invalid decimal amount") from exc
    if not amount.is_finite() or amount <= 0:
        raise TransferEvidenceError("amount must be finite and positive")
    return amount


def assess(intent: dict, transfers: list[dict]) -> dict:
    """Check claimed matched debit/credit records against a declared intent.

    Successful arithmetic describes only supplied provider-shaped JSON.
    It never authenticates who supplied the data or verifies actual custody.
    """
    if not isinstance(intent, dict) or set(intent) != {
        "client_ref_id", "asset", "from_profile_id", "to_profile_id", "amount"
    }:
        raise TransferEvidenceError("unexpected transfer-intent schema")
    ref_id = _name(intent["client_ref_id"])
    asset = _name(intent["asset"])
    sender, receiver = _name(intent["from_profile_id"]), _name(intent["to_profile_id"])
    amount = _amount(intent["amount"])
    if sender == receiver:
        raise TransferEvidenceError("source and destination must differ")
    if not isinstance(transfers, list):
        raise TransferEvidenceError("transfer records must be a list")

    seen_ids: set[str] = set()
    debit: dict | None = None
    credit: dict | None = None
    for item in transfers:
        if not isinstance(item, dict):
            raise TransferEvidenceError("malformed transfer record")
        required = {"id", "group_id", "type", "status", "profile_id", "asset", "amount", "direction"}
        if not required.issubset(item):
            raise TransferEvidenceError("required Paxos v2 fields absent")
        record_id = _name(item["id"])
        if record_id in seen_ids:
            raise TransferEvidenceError("duplicate transfer record id")
        seen_ids.add(record_id)
        _name(item["group_id"])
        if item["asset"] != asset or _amount(item["amount"]) != amount:
            raise TransferEvidenceError("asset or amount differs from declared intent")
        if item["status"] not in ("PENDING", "COMPLETED", "FAILED"):
            raise TransferEvidenceError("unexpected provider transfer status")
        if item["type"] == "PAXOS_TRANSFER_DEBIT":
            if debit is not None or item["direction"] != "DEBIT" or item["profile_id"] != sender:
                raise TransferEvidenceError("conflicting source debit")
            if item.get("ref_id") != ref_id:
                raise TransferEvidenceError("source ref_id does not match proposed request")
            debit = item
        elif item["type"] == "PAXOS_TRANSFER_CREDIT":
            if credit is not None or item["direction"] != "CREDIT" or item["profile_id"] != receiver:
                raise TransferEvidenceError("conflicting destination credit")
            credit = item
        else:
            raise TransferEvidenceError("unsupported operation kind; not an internal/crypto withdrawal")

    if debit is not None and credit is not None and debit["group_id"] != credit["group_id"]:
        raise TransferEvidenceError("opposing records do not belong to same provider group")
    paired_complete = (
        debit is not None and credit is not None
        and debit["status"] == "COMPLETED" and credit["status"] == "COMPLETED"
    )
    statuses = [r["status"] for r in (debit, credit) if r is not None]
    return {
        "assessment": (
            "SUPPLIED_PROVIDER_RECORDS_RECONCILE"
            if paired_complete else "RECORDS_INCOMPLETE_OR_NOT_COMPLETED"
        ),
        "documented_provider": "Paxos v2",
        "declared_asset": asset,
        "declared_amount": str(amount),
        "client_ref_id": ref_id,
        "observed_in_input": {
            "debit": debit is not None,
            "credit": credit is not None,
            "statuses": statuses,
            "paired_completed": paired_complete,
        },
        "evidence_is_local_unauthenticated_json": True,
        "provider_api_authentication_verified": False,
        "provider_records_independently_retrieved": False,
        "destination_balance_independently_read_back": False,
        "underlying_commodity_title_assigned_or_verified": False,
        "physical_custody_and_liabilities_verified": False,
        "holder_eligibility_and_consent_verified": False,
        "no_live_transfer_attempted": True,
        "scope_warning": "Matching provider-shaped transfer records are NOT proof of metal "
                         "ownership, delivery, complete liabilities or independently verified settlement.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=FIXTURE)
    args = parser.parse_args()
    evidence = json.loads(args.fixture.read_text(encoding="utf-8"))
    print(json.dumps(assess(evidence["intent"], evidence["transfers"]), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
