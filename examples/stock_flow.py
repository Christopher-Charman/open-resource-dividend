"""ORD thought-experiment only: conserved metal claims, not a token implementation.

Units are arbitrary *integer* physical units of each separate metal. A deposit
represents an assumed independently verified delivery; no title, custody,
identity, delivery, or oracle evidence is validated here. The hash-linked log
is for illustration, not a consensus system or immutable external anchor.
"""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from typing import Iterable

METALS = ("Au", "Ag", "Cu")
GENESIS = "0" * 64


class FundingError(ValueError):
    """An operation would create an invalid or unfunded claim."""


class StockFlow:
    """Toy balance sheet: every issued claim has exactly one metal unit."""

    def __init__(self) -> None:
        self.reserves = dict.fromkeys(METALS, 0)
        self.accounts: dict[str, dict[str, int]] = defaultdict(
            lambda: dict.fromkeys(METALS, 0)
        )
        self.receipts: set[str] = set()
        self.events: list[dict] = []

    @staticmethod
    def _valid(metal: str, quantity: int) -> None:
        if metal not in METALS or type(quantity) is not int or quantity <= 0:
            raise FundingError("expected a supported metal and positive integer quantity")

    @staticmethod
    def _account(value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise FundingError("account must be nonempty")

    def _append(self, kind: str, metal: str, details: dict) -> None:
        record = {
            "sequence": len(self.events) + 1,
            "previous": self.events[-1]["digest"] if self.events else GENESIS,
            "kind": kind,
            "metal": metal,
            "details": details,
        }
        message = json.dumps(record, sort_keys=True, separators=(",", ":"))
        record["digest"] = hashlib.sha256(message.encode("utf-8")).hexdigest()
        self.events.append(record)
        self.verify()

    def deposit_assumed_verified(
        self, owner: str, metal: str, quantity: int, evidence_id: str
    ) -> None:
        """Simulate receipt of unencumbered metal; NOT a proof of receipt."""
        self._valid(metal, quantity)
        self._account(owner)
        if not isinstance(evidence_id, str) or not evidence_id.strip():
            raise FundingError("a synthetic evidence identifier is required")
        if evidence_id in self.receipts:
            raise FundingError("deposit evidence identifier already used")
        self.receipts.add(evidence_id)
        self.reserves[metal] += quantity
        self.accounts[owner][metal] += quantity
        self._append("assumed_deposit", metal, {
            "owner": owner, "quantity": quantity, "evidence_id": evidence_id
        })

    def transfer(self, sender: str, recipient: str, metal: str, quantity: int) -> None:
        self._valid(metal, quantity)
        self._account(sender)
        self._account(recipient)
        if sender == recipient or self.accounts[sender][metal] < quantity:
            raise FundingError("self-transfer or insufficient existing claims")
        self.accounts[sender][metal] -= quantity
        self.accounts[recipient][metal] += quantity
        self._append("transfer", metal, {
            "from": sender, "to": recipient, "quantity": quantity
        })

    def dividend(
        self, pool: str, recipients: Iterable[str], metal: str,
        per_person: int, retained_buffer: int = 0
    ) -> None:
        """Atomic *toy* allocation from already-owned pool holdings."""
        self._valid(metal, per_person)
        self._account(pool)
        if type(retained_buffer) is not int or retained_buffer < 0:
            raise FundingError("retained buffer must be a nonnegative integer")
        people = list(recipients)
        if not people or len(people) != len(set(people)) or pool in people:
            raise FundingError("eligible recipients must be unique and exclude pool")
        for person in people:
            self._account(person)
        total = len(people) * per_person
        if self.accounts[pool][metal] - total < retained_buffer:
            raise FundingError("dividend is not fully backed by available pool claims")
        self.accounts[pool][metal] -= total
        for person in people:
            self.accounts[person][metal] += per_person
        self._append("funded_distribution", metal, {
            "pool": pool, "recipients": people, "per_person": per_person,
            "total": total, "retained_buffer": retained_buffer
        })

    def redeem_assumed_delivered(
        self, holder: str, metal: str, quantity: int, delivery_id: str
    ) -> None:
        """Assume verified physical delivery; real delivery is NOT atomic."""
        self._valid(metal, quantity)
        self._account(holder)
        if not isinstance(delivery_id, str) or not delivery_id.strip():
            raise FundingError("synthetic delivery identifier required")
        if delivery_id in self.receipts:
            raise FundingError("delivery evidence identifier already used")
        if self.accounts[holder][metal] < quantity:
            raise FundingError("redemption exceeds current holdings")
        self.receipts.add(delivery_id)
        self.accounts[holder][metal] -= quantity
        self.reserves[metal] -= quantity
        self._append("assumed_delivered_redemption", metal, {
            "holder": holder, "quantity": quantity, "delivery_id": delivery_id
        })

    def verify(self) -> None:
        """Check the toy's conservation and hash links, not real-world reserves."""
        for metal in METALS:
            balances = [account[metal] for account in self.accounts.values()]
            if any(balance < 0 for balance in balances):
                raise AssertionError("negative claim balance")
            if self.reserves[metal] < 0 or sum(balances) != self.reserves[metal]:
                raise AssertionError("issued claims do not equal assumed reserves")
        previous = GENESIS
        for index, event in enumerate(self.events, 1):
            bare = {key: value for key, value in event.items() if key != "digest"}
            content = json.dumps(bare, sort_keys=True, separators=(",", ":"))
            expected = hashlib.sha256(content.encode("utf-8")).hexdigest()
            if (event["sequence"] != index or event["previous"] != previous
                    or event["digest"] != expected):
                raise AssertionError("illustrative event chain altered")
            previous = expected


def demonstration() -> dict:
    """Frank can trade, Bob can purchase compute, neither needs new claims."""
    model = StockFlow()
    model.deposit_assumed_verified("donor", "Cu", 1000, "SYNTHETIC-CU-1")
    model.transfer("donor", "dividend-pool", "Cu", 1000)
    model.dividend("dividend-pool", ["Frank", "Bob"] + [
        f"Person-{i:03d}" for i in range(98)
    ], "Cu", 9, retained_buffer=100)
    model.transfer("Frank", "Bob", "Cu", 3)  # assumed off-ledger consideration
    model.transfer("Bob", "compute-provider", "Cu", 5)
    model.redeem_assumed_delivered("Frank", "Cu", 2, "SYNTHETIC-DELIVERY-1")
    model.verify()
    return {
        "assumed_copper_reserve_units": model.reserves["Cu"],
        "outstanding_copper_claim_units": sum(
            balance["Cu"] for balance in model.accounts.values()
        ),
        "fund_copper_claim_units": model.accounts["dividend-pool"]["Cu"],
        "frank_copper_claim_units": model.accounts["Frank"]["Cu"],
        "bob_copper_claim_units": model.accounts["Bob"]["Cu"],
        "compute_provider_copper_claim_units": model.accounts["compute-provider"]["Cu"],
        "recorded_events": len(model.events),
        "last_event_digest": model.events[-1]["digest"],
    }


if __name__ == "__main__":
    print(json.dumps(demonstration(), indent=2, sort_keys=True))
