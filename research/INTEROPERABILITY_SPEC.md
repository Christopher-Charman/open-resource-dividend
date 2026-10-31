# Interoperability specification: distribution without becoming a new custodian

**Public design candidate 0.1 · 31 October 2026 · not adopted · no financial integration**

This document derives a **minimal separation-of-concerns contract** from observed live precedents and the existing [ORD issuer-neutral research model](RFC_0002_ISSUER_NEUTRAL_DISTRIBUTION.md). It is designed to give independent contributors concrete, falsifiable integration targets without assuming permission to issue, custody or transmit anyone's money.

## Decisions justified by existing evidence

**Use the funded pool pattern as a research donor, not the GoodDollar currency.** Source-level inspection of [GoodCollective `UBIPool.sol`](https://github.com/GoodDollar/GoodCollective/blob/master/packages/contracts/contracts/UBI/UBIPool.sol) reveals per-cycle distribution from the pool's existing `rewardToken.balanceOf`, a uniqueness-validator root, administrator-adjustable caps/settings and a final token `safeTransfer`. An ORD distribution mechanism could instead consume a finite, **legally verified existing ownership balance** from any admitted issuer class, then transfer it to a consenting claimant.

**Do not adopt one commodity issuer as the universal entitlement authority.** [PAXG terms](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions) grant contractual rights but restrict issuer redemptions to verified customers, specify 430 PAXG per direct bar redemption and retain freeze/upgrade powers. [Kinesis current redemption guidance](https://support.kinesis.money/hc/en-gb/articles/38687923843741-Redeeming-Gold-and-Silver-in-App) specifies 100 KAU or 200 KAG increments with fees and delivery logistics. **These are design constraints, not an endorsement or proposed purchases.**

**Treat GoodDollar identity and Circles social trust as alternative inputs, not universal eligibility proof.** A global human uniqueness system has major privacy, exclusion and governance decisions; neither protocol's assumptions can be adopted as proof of universal inclusion merely because the code is open.

## Candidate adapter interface (research semantics only)

The following are **specification operations**, not deployed endpoints or executable asset-transfer permissions:

| Operation | Required signed/independent input | Required observable result | No shortcut |
| --- | --- | --- | --- |
| `describe_claim_class` | Exact issuer identity, custodian, metal, grade/atomic unit, custody contract version, controlling jurisdiction, legal beneficial right | Immutable class reference unique to those rights; explicit redemptions, minimums, fees, freezes, expiry and issuer-controlled rules | Never collapse two issuers' "gold" into an implicitly fungible asset |
| `verify_preexisting_funded_holdings` | Source fund's genuine legal/control ownership, full direct+indirect liabilities, independently inspected unencumbered reserves, audit recency and scope | A dated externally witnessed fund balance and conditions under which it can be transferred | A wallet balance, smart-contract event or issuer's own reserve dashboard is not independent title proof |
| `prepare_distribution` | Authorized fund intent, eligible recipient set, unit amount per class, existing assets, fee commitments and retained pool buffer | Deterministic *proposed* batch; reject overdraft, duplicate recipients, cross-class conversion and unrecorded obligations | No "new ORD token" created because recipients increased |
| `authorize_and_transfer` | Recipient's valid right to receive, genuine consenting owner signatures, issuer-supported **legal assignment of title**, jurisdiction and eligibility constraints | Destination ownership independently read back, effective time, dispute/settlement status and an auditable transfer reference | Neither a synthetic event nor a token send is necessarily a legally effective property transfer |
| `request_redemption` | Holder control over an existing claim; accepted vault/issuer redemption request including minimums/fees and lawful delivery destination | A **locked but still outstanding** liability, not an assumed burn | Do not extinguish economic ownership when delivery is only requested |
| `complete_or_reverse_redemption` | Independent evidence of valid delivery or agreed legal discharge, or cancellation/recovery with owner consent | Proven claim retirement and reserve release, or reinstated transferable claim, with no double release | Issuer assertion or an on-chain "burn" alone cannot prove delivery |
| `publish_assurance` | Independent third-party inspection, liability completeness attestation, conflicts and uncertainty declarations | Public verifiable commitments including validity periods and independent witness identities, preserving necessary personal privacy | Never report "fully backed" from self-declared custody data |

A **normal automated check should fail closed** when required evidence is expired, absent or contradictory, but this rule is intended to prevent *unbacked financial assertions*, not to add permission gates to research, public criticism or ordinary voluntary transactions.

## Practical routes identified in current public projects

1. **GoodCollective source donor:** study `UBIPool.sol`, `UBIPoolFactory.sol` and `UBIPool.claim.test.ts` for finite-pool claims, same-human root accounting, zero-income periods, manager fee and upgrade authority. It is MIT licensed and does **not** itself verify metal title. There is no justification to fork/install its complete production stack merely to reuse those ideas.
2. **Paxos PAXG provider study:** the [Paxos developer guide](https://docs.paxos.com/guides/stablecoin/paxg) describes tokenized-gold transfers and [PAXG Dashboard guide](https://docs.paxos.com/guides/dashboard/paxg) documents deposits, withdrawals, purchases and sales. Paxos also documents a [testnet faucet for test PAXG](https://docs.paxos.com/guides/developer/fund-sandbox-with-test-crypto). **A test asset is only a software simulation**; it neither grants a real vault claim nor proves permission to receive/transfer real PAXG. KYC, legal and account requirements remain. No live or testnet key material has been created in ORD.
3. **Kinesis KAU/KAG provider study:** reserve audit indexes and holder-redemption policies are documented. Confirm native KAU/KAG versus any ERC-20 wrapper as *separate liabilities*; wrapper proofs and reserves cannot be inherited by citation. No open public transfer API or direct ORD admission was verified during this review.
4. **Circles v2 research donor:** current `aboutcircles/circles-contracts-v2` is AGPL-3.0. Trust networks and group currencies are intellectually relevant; **do not copy or mix source code into ORD's MIT sample without legal compatibility analysis**.
5. **Optional compute sellers:** Akash proves that competing providers can offer paid compute, but its lease/ACT payment protocol is **not** an ORD resource-title settlement. ORD should not mandate Akash or any particular provider.

## Demonstration that would actually advance the claim

The smallest legitimate external integration trial would be a **no-financial-value, provider-documented sandbox** (only if genuinely supported), with:

- independently inspectable testnet asset class and separate issuer identity;
- a simulated but explicitly pre-funded distribution pool with verifiable pre/post balances;
- signed **test-only** instructions from two independent volunteers or test actors and a deliberately failed insufficient-funds claim;
- transfer readback from the provider's independent test environment;
- an explicitly separate test for *on-chain movement* versus actual legally recognised physical title (the latter necessarily remains **unverified** in a sandbox);
- no integration with a private real wallet, live reserve, KYC record, or asset-custody account.

Passing a sandbox should not automatically approve the external provider for production. **Real asset admission would require independent legal/custodial and source-of-funds evidence, plus the community's distinct governance and regulatory decisions.** The ORD research repository has not authorised issuing/holding real assets.

## Expected result of this research phase

A contributor can now inspect specific upstream **MIT source**, legally significant issuer terms and exact acceptance questions. The next productive path is to validate an existing *rights-preserving* issuer transfer mechanism against this interface. If none permits universal small-holder property and affordable independent exit, publish that negative result and consider a different underlying asset or non-issuer structure rather than manufacture another token.

This work is unaffiliated with Paxos, Kinesis, GoodDollar, Circles, Windfall Trust or Akash and does not imply their approval or participation.
