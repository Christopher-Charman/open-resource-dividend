# Live provider transfer interfaces: what can actually be verified

**Independent source review · 31 October 2026 · version 0.1 · research and offline record-shape checks only**

This research addresses the next step after [external project diligence](EXISTING_PROJECTS_DUE_DILIGENCE.md): whether a supported transfer interface can move a pre-existing resource claim from a funded owner to an individual, and which claims can be independently accepted afterward. It does **not** authorise integrations, payments, token issuance, custody or real-value transactions.

## Finding: a completed token transfer is not evidence of all the required rights

Paxos publicly documents a genuine **v2 API** for internal/Paxos profile transfers and crypto withdrawals, including a client-side `ref_id` for replay detection, per-transfer `id`, source/destination `profile_id`, `group_id` joining debit and credit legs, `asset`, decimal `amount`, and `PENDING`/`COMPLETED`/`FAILED` status. A separate **Get Transfer** endpoint supports authenticated status retrieval. A two-sided completed transfer record can support **transaction reconciliation**, but the responses do not carry independently audited vault inventories, legal title opinions, beneficiary rights, physical-delivery acknowledgements or complete third-party liabilities.

Relevant official API documentation:
- [Paxos Transfer — create](https://docs.paxos.com/api-reference/endpoints/paxos-transfers/create-paxos-transfer), `POST /v2/transfer/paxos` (a transfer between Paxos profiles, with a client-specified `ref_id`).
- [Get Transfer](https://docs.paxos.com/api-reference/endpoints/transfers/get-transfer) and [List Transfers](https://docs.paxos.com/api-reference/endpoints/transfers/list-transfers) provide `id`, type, status, `group_id`, profile, asset and value metadata; the provider's status is **not** an independently witnessed property-title outcome.
- [Create Crypto Withdrawal](https://docs.paxos.com/api-reference/endpoints/crypto-withdrawals/create-crypto-withdrawal) documents a `ref_id`, destination, network, asset and amount; on-chain tx hash can be present in response. A blockchain transfer is a distinct operation from a physical gold delivery.
- [Paxos Sandbox](https://docs.paxos.com/guides/developer/sandbox) supports mocked transfers with **test-only** assets, including PAXG, subject to limits.
- [API authentication](https://docs.paxos.com/api-reference/introduction) uses OAuth 2 client credentials; [Developer onboarding](https://docs.paxos.com/guides/developer/account) requires an enabled developer account and support activation. ORD has **no authorised Paxos account or credentials**, so it has **not** exercised a real Paxos Sandbox or production API call.

**Critical qualification:** The transfer endpoint's generic `asset` field does not by itself establish which asset/network/profile/direction combinations a particular customer is entitled to execute. That must be confirmed with documented provider support and real account permissions. Do not automatically assume every valid asset can be transferred by every user.

## The legal constraints are unusually important to ORD

Under the [PAX Gold terms (12 December 2025)](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions):

- §4.3 and §5 describe fractional economic ownership of segregated allocated gold, not just a dollar price promise; §5 allows reallocation across identified bars.
- §4.11 limits Paxos issuance and redemption services to verified customers, and may permit refusal under certain conditions.
- §11.4 requires a **minimum 430 PAXG plus fees** for direct delivery of one London Good Delivery gold bar. A tiny universal entitlement **cannot itself use that direct redemption route**.
- §14 grants certain freezing, upgrade and legal-compliance powers over PAXG.
- **§15.2 expressly allows future storage fees funded by issuing additional PAXG to Paxos, diluting existing holders** on a pro-rata basis, subject to advance notice. This is an *allowed contractual contingency*, **not evidence that Paxos currently charges this fee**. ORD cannot describe PAXG as necessarily meeting an immutable no-dilution rule.
- §15.5 describes a potential $2/month inactive-account charge after 12 months for qualifying account holders; custody in a personal Paxos profile is not costless under every possible usage pattern.

These contractual features are **not allegations of misconduct**. They are explicit user-rights conditions. Whether any such asset is acceptable under the *original no-arbitrary-dilution* objective is a **community research decision**, not a question that can be answered by an API status response.

## Kinesis native transfer boundaries

[Kinesis native transfer guidance](https://support.kinesis.money/hc/en-gb/articles/40077246157725-Move-KAU-KAG) describes sending/receiving KAU or KAG on **its native Kinesis network**, requiring identity verification for account deposits and memo/destination information when appropriate. It warns that unsupported cross-network token transfers may lead to loss and notes ERC-20 representations from another system are **not yet native inbound equivalents**. [Redemption guidance](https://support.kinesis.money/hc/en-gb/articles/12439302237085-How-to-redeem-physical-gold-and-silver) separately gives a physical delivery process in increments of **100 KAU** or **200 KAG**, with provider operations involvement.

A publicly documented, unauthenticated, supported **third-party API for a legal title-assignment and independent destination readback** was **not established from the sources reviewed**. This is **not a claim that no API exists**: future contributors may establish one with dated, official, current documentation. Do not invent a Kinesis API route, use unrelated token-wrappers, or treat transfer on the wrong network as reversible.

## GoodCollective is a distribution donor, not a metal custodian

The [actual GoodCollective `UBIPool.sol` source](https://github.com/GoodDollar/GoodCollective/blob/master/packages/contracts/contracts/UBI/UBIPool.sol) calculates payout amounts from the reward token balance and uses `safeTransfer` for payouts. The [factory](https://github.com/GoodDollar/GoodCollective/blob/master/packages/contracts/contracts/UBI/UBIPoolFactory.sol) has manager/administrative powers and an upgradeable implementation. Neither source file asserts or proves legally enforceable metal title for a G$ transfer. Reuse its **finite funded pool semantics** and focus on independent consent, total claims, rights and witness evidence rather than adopting its monetary asset.

## Provider operation comparison

| Evidence source | What public documentation establishes | What ORD has actually exercised | What is missing for admission as a resource-title adapter |
| --- | --- | --- | --- |
| Paxos v2 `POST /transfer/paxos`, GET transfer | Authenticated API records for an asset/profile transfer, statuses, `ref_id`, grouped legs | Offline validation of **invented provider-shaped JSON only**, no API requests | Account-authorised test request, independently observed destination, PAXG legal-title application, custodian/total-liabilities evidence and cost/eligibility analysis |
| Paxos v2 crypto withdrawal | API for network asset withdrawal, status and optional chain tx hash | Documentation review only | Provider network/asset support, independent blockchain receipt and relation to contractually recognised gold title |
| Kinesis native receive/send | Provider's documented native network/UI and physical redemption process | Documentation review only | Supported public API or lawful readback integration, verified source/destination, insolvency/title and off-provider exit |
| GoodCollective UBI pool | Funded reward-token balance transfer and social eligibility mechanisms | Independently read source files; no contracts executed by ORD | Legally effective transfer of existing external rights; limits on manager/factory and eligibility authority |

**No third-party provider currently has a verified, approved ORD asset adapter.** This is a current result of evidence screening—not a ban on further authorised investigation or a requirement to build a new coin.

## An executable reconciliation boundary

[The offline transfer evidence reader](../examples/provider_transfer_evidence.py) consumes a **deliberately fabricated** pair of [Paxos-v2-shaped records](../examples/scenarios/paxos_transfer_records.json). It checks:

- explicit asset, positive decimal quantity, intended sender/destination and source-side client `ref_id`;
- unique transfer IDs, valid debit/credit types, common `group_id` and appropriate profiles;
- both legs present and provider-record statuses `COMPLETED`, otherwise reports pending/incomplete (and rejects contradictory or malformed records).

Even a fully matched input is labelled `SUPPLIED_PROVIDER_RECORDS_RECONCILE` with `provider_records_independently_retrieved=false`, `destination_balance_independently_read_back=false` and `underlying_commodity_title_assigned_or_verified=false`. This is **not proof that any actual Paxos operation happened**; fabricated input can look identical to a real response.

Run locally with Python 3.10+:

```bash
python3 examples/provider_transfer_evidence.py
python3 -m unittest discover -s examples -p 'test_*.py' -v
```

No OAuth token, testnet asset, secret, real name, legal document or external network connection is used.

## The actual next externally grounded demonstration

When independent volunteers have lawful sandbox access and consent, a **separate, explicitly authorised test-only** workflow could:

1. Confirm provider-specific support for PAXG in that route and obtain separate consented sandbox profiles and entitlements.
2. Read source and destination **test-only** balances and establish an actual pre-funded scenario.
3. Make an authenticated sandbox transfer with a unique client reference. Preserve the **exact** request identity; never replay a financial write based only on a timeout or missing acknowledgement.
4. Independently fetch transfer status, destination readback and network receipt, using authorised credentials and an evidence trail that cannot be supplied solely by the code that made the write.
5. Classify **software token settlement** only. Legal property, physical reserves, legal identity of the recipient and universal funding remain **unverified by sandbox**.

A provider's Sandbox may not support the required exact asset/route, and a private account's permission and KYC cannot be inferred from documentation. The test **must not** be promoted to live funds, a token sale or an ORD asset listing without entirely separate legal and custodial acceptance.

### Technical and governance conclusions

- Keep distribution and issuer custody **separate**. This work reinforces RFC 0002, but does not adopt it.
- Avoid authoring a universal "metal adapter" that disguises different legal rights under one `Au` balance.
- Prefer genuine existing APIs over an invented ORD ledger, but refuse to substitute provider status for title or physical delivery.
- Account terms can change: documented right to dilute/freeze is a core property to disclose, not a cosmetic caveat.
- Contributors can replace this provider with a superior rights-preserving alternative; no individual vendor, founder or AI provider owns the proposal.

See [Existing-project due diligence](EXISTING_PROJECTS_DUE_DILIGENCE.md), [Interoperability specification](INTEROPERABILITY_SPEC.md) and [RFC 0002](RFC_0002_ISSUER_NEUTRAL_DISTRIBUTION.md). **Public research only; no third-party partnership implied.**
