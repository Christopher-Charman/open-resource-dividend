"""Issuer-neutral ORD distribution *thought experiment*, not a monetary protocol.

No new ORD asset is minted. Two independent external resource-claim classes
remain distinct (issuer, custody, contractual rights and unit). A separately
funded pool transfers only claims it already holds. No identity, transfer
signature, vault, oracle, legal title or third-party proof is verified.

Python 3.10+ standard library. Manifest and events are SYNTHETIC, unauthenticated
declarations. The demo is an accounting model, NOT an issuer, wallet or exchange.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ASSET_FIELDS = {
    "asset_id", "issuer_id", "custodian_id", "metal", "atomic_unit",
    "legal_rights_reference", "declared_total_claims", "reported_reserves",
}
HOLDING_FIELDS = {"asset_id", "account", "units"}
TRANSFER_FIELDS = {"type", "asset_id", "from", "to", "units"}
DIVIDEND_FIELDS = {
    "type", "asset_id", "pool", "recipients", "units_each", "retained_buffer",
}
REQUEST_FIELDS = {
    "type", "asset_id", "holder", "request_id", "units",
}
RESOLUTION_FIELDS = {"type", "request_id"}


class ManifestError(ValueError):
    """The synthetic declaration or lifecycle violates an accounting rule."""


def _positive(value: object, *, allow_zero: bool = False) -> int:
    if type(value) is not int or value < (0 if allow_zero else 1):
        raise ManifestError("expected a positive integer atomic-unit amount")
    return value


def _identifier(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ManifestError("non-empty string identifier required")
    return value


def _fields(item: object, names: set[str]) -> dict:
    if not isinstance(item, dict) or set(item) != names:
        raise ManifestError("unrecognised or incomplete schema")
    return item


def evaluate(manifest: dict) -> dict:
    """Independently recompute claim balances; never attest the supplied facts."""
    _fields(manifest, {"schema_version", "assets", "initial_holdings", "events"})
    if type(manifest["schema_version"]) is not int or manifest["schema_version"] != 1:
        raise ManifestError("unsupported schema version")
    asset_rows = manifest["assets"]
    holdings = manifest["initial_holdings"]
    events = manifest["events"]
    if not isinstance(asset_rows, list) or not asset_rows:
        raise ManifestError("at least one independently defined asset is required")
    if not isinstance(holdings, list) or not isinstance(events, list):
        raise ManifestError("holdings and events must be lists")

    assets: dict[str, dict] = {}
    for raw in asset_rows:
        asset = _fields(raw, ASSET_FIELDS)
        key = _identifier(asset["asset_id"])
        if key in assets:
            raise ManifestError("duplicate asset class")
        for name in ("issuer_id", "custodian_id", "atomic_unit", "legal_rights_reference"):
            _identifier(asset[name])
        if asset["metal"] not in ("Au", "Ag", "Cu"):
            raise ManifestError("unsupported metal")
        _positive(asset["declared_total_claims"])
        _positive(asset["reported_reserves"], allow_zero=True)
        # Different rights at different custodians must not use one asset id.
        assets[key] = asset

    balances = defaultdict(int)
    for raw in holdings:
        holding = _fields(raw, HOLDING_FIELDS)
        asset_id = _identifier(holding["asset_id"])
        account = _identifier(holding["account"])
        if asset_id not in assets:
            raise ManifestError("unknown external asset")
        amount = _positive(holding["units"])
        balances[(asset_id, account)] += amount

    for asset_id, asset in assets.items():
        summed = sum(units for (key, _), units in balances.items() if key == asset_id)
        if summed != asset["declared_total_claims"]:
            raise ManifestError("initial owner claims do not equal declared external liabilities")

    pending: dict[str, dict] = {}
    resolved: set[str] = set()
    assumed_completed = dict.fromkeys(assets, 0)
    activity = []
    for index, raw in enumerate(events, 1):
        if not isinstance(raw, dict) or "type" not in raw:
            raise ManifestError("missing event kind")
        kind = raw["type"]
        if kind == "transfer":
            _fields(raw, TRANSFER_FIELDS)
            asset_id = _identifier(raw["asset_id"])
            sender, recipient = _identifier(raw["from"]), _identifier(raw["to"])
            amount = _positive(raw["units"])
            if asset_id not in assets or sender == recipient:
                raise ManifestError("invalid transfer destination or asset")
            if balances[(asset_id, sender)] < amount:
                raise ManifestError("insufficient already-owned claim units")
            balances[(asset_id, sender)] -= amount
            balances[(asset_id, recipient)] += amount
        elif kind == "dividend":
            _fields(raw, DIVIDEND_FIELDS)
            asset_id, pool = _identifier(raw["asset_id"]), _identifier(raw["pool"])
            amount = _positive(raw["units_each"])
            buffer = _positive(raw["retained_buffer"], allow_zero=True)
            recipients = raw["recipients"]
            if (
                asset_id not in assets
                or not isinstance(recipients, list) or not recipients
                or any(not isinstance(p, str) or not p.strip() for p in recipients)
                or len(set(recipients)) != len(recipients) or pool in recipients
            ):
                raise ManifestError("invalid or duplicate recipient labels")
            total = amount * len(recipients)
            if balances[(asset_id, pool)] - total < buffer:
                raise ManifestError("unfunded or overcommitted dividend")
            balances[(asset_id, pool)] -= total
            for recipient in recipients:
                balances[(asset_id, recipient)] += amount
        elif kind == "request_redemption":
            _fields(raw, REQUEST_FIELDS)
            asset_id, holder = _identifier(raw["asset_id"]), _identifier(raw["holder"])
            request_id = _identifier(raw["request_id"])
            amount = _positive(raw["units"])
            if asset_id not in assets or request_id in pending or request_id in resolved:
                raise ManifestError("invalid or reused redemption reference")
            if balances[(asset_id, holder)] < amount:
                raise ManifestError("redemption request exceeds freely held claims")
            # Request locks units but DOES NOT extinguish a liability or
            # claim a physical warehouse has released anything.
            balances[(asset_id, holder)] -= amount
            pending[request_id] = {
                "asset_id": asset_id, "holder": holder, "units": amount
            }
        elif kind in ("cancel_redemption", "delivery_assumed"):
            _fields(raw, RESOLUTION_FIELDS)
            request_id = _identifier(raw["request_id"])
            if request_id not in pending:
                raise ManifestError("redemption does not have one open request")
            claim = pending.pop(request_id)
            resolved.add(request_id)
            if kind == "cancel_redemption":
                balances[(claim["asset_id"], claim["holder"])] += claim["units"]
            else:
                # Off-chain delivery is ASSUMED, never evidenced here.
                # Remove liability only in a *hypothetical* post-delivery
                # snapshot. A real system needs legal title/delivery proof.
                assumed_completed[claim["asset_id"]] += claim["units"]
        else:
            # There is intentionally no ORD mint, rebase or exchange-rate
            # conversion event: source rights are issuer-specific.
            raise ManifestError("event type not supported (including new issuance)")
        activity.append({"sequence": index, "operation": kind})

        # Conservation is checked after EVERY event, including pending
        # redemptions, and per issuer/custodian/contract asset class.
        for key, asset in assets.items():
            open_amount = sum(
                value for (aid, _), value in balances.items() if aid == key
            )
            locked_amount = sum(
                p["units"] for p in pending.values() if p["asset_id"] == key
            )
            if open_amount + locked_amount + assumed_completed[key] != asset["declared_total_claims"]:
                raise ManifestError("claim conservation violated")

    report = {}
    for key, asset in sorted(assets.items()):
        available = sum(value for (aid, _), value in balances.items() if aid == key)
        locked = sum(p["units"] for p in pending.values() if p["asset_id"] == key)
        outstanding = available + locked
        reported_unencumbered = asset["reported_reserves"] - assumed_completed[key]
        # Beware: 'reserves' is a self-report and assumed delivery is NOT
        # real warehouse evidence. Negative reported amounts are a deficit.
        report[key] = {
            "issuer_id": asset["issuer_id"],
            "custodian_id": asset["custodian_id"],
            "metal": asset["metal"],
            "atomic_unit": asset["atomic_unit"],
            "legal_rights_reference": asset["legal_rights_reference"],
            "available_claim_units": available,
            "locked_pending_claim_units": locked,
            "claims_assumed_delivered": assumed_completed[key],
            "post_assumed_liabilities": outstanding,
            "post_assumed_reported_reserves": reported_unencumbered,
            "declared_arithmetic_deficit": max(0, outstanding - reported_unencumbered),
            "physical_reserves_verified": False,
            "title_rights_verified": False,
            "complete_external_liabilities_verified": False,
            "redemption_delivery_verified": False,
        }
    return {
        "status": "SYNTHETIC_DECLARATIONS_ONLY",
        "ord_issued_new_claims": False,
        "synthetic_accounts_not_human_eligibility": True,
        "transfer_ownership_or_authority_signatures_verified": False,
        "cross_issuer_fungibility_assumed": False,
        "assets": report,
        "ending_balances": [
            {"asset_id": aid, "account": account, "units": units}
            for (aid, account), units in sorted(balances.items()) if units
        ],
        "open_redemption_requests": pending,
        "event_history": activity,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "manifest", nargs="?", type=Path,
        default=Path(__file__).resolve().parent / "scenarios" / "issuer_neutral.json"
    )
    args = parser.parse_args()
    print(json.dumps(
        evaluate(json.loads(args.manifest.read_text(encoding="utf-8"))),
        indent=2, sort_keys=True
    ))


if __name__ == "__main__":
    main()
