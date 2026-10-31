# ORD RFC 0002 — Issuer-neutral universal distribution

**PUBLIC RESEARCH CANDIDATE, not adopted · 31 October 2026**

This is a concrete exploration of architecture C in [RFC 0001](RFC_0001_RESOURCE_CLAIMS.md), not a launched currency, selected chain, trust, custodian, financial claim or funded universal entitlement. The community can reject it if evidence supports a better structure.

## Core proposal: distribute existing rights, do not create ORD money

An independent fund acquires **legally existing commodity claims from willing contributors or through genuinely earned resources**, then distributes *those same claims*. The owners remain free to hold, transfer, trade, aggregate or seek lawful physical redemption with the original external issuer. AI is the motivation, but no AI provider becomes the required issuer or spending destination.

Frank can receive a transferable resource entitlement without using AI. Bob may voluntarily buy Frank's rights and use his purchasing power at a competing compute provider. No one is required to trade or use AI. ORD must not silently exchange gold for copper or assume that two unrelated custodians' promises are fungible.

The candidate **does not solve universal funding** or remove the need to trust custodians. It primarily removes the assumption that ORD itself must mint another currency.

## System boundaries

| Role | Must provide | ORD must not claim or control |
| --- | --- | --- |
| External resource issuer or custodian | Independently evidenced quantity, title, asset-specific contractual terms, liability completeness, reliable lawful redemption | A hash alone is a custody audit; all metal claims are fungible; or an ORD-issued title replaces the issuer's legal duty |
| Genuine donor or income-generating pool | Actual, settled ownership of transferable pre-existing rights | Unlimited issuance, compulsory transfer of other people's commodities, or a promised recurring dividend without funding |
| Open distribution rule | Reproducible transfer quantities, an identifiable funded pool, accounting of pending obligations | Authority to confiscate, mint, freeze or rewrite third-party property |
| Eligibility and privacy services | Unique eligible claimants, reviewable exclusions, appeals and appropriate confidentiality | That public pseudonyms or merely hashing people's names produces privacy or human uniqueness |
| Holders and open exchanges | Voluntary hold, trade, transfer and independently enforceable exit | Guaranteed liquidity or guaranteed favourable terms |

## Executable reference and state rules

The [stdlib-only model](../examples/issuer_neutral_distribution.py) consumes a [synthetic JSON manifest](../examples/scenarios/issuer_neutral.json). Each **distinct external asset class** includes an issuer ID, custodian ID, Au/Ag/Cu metal type, atomic unit, governing legal-rights reference, *self-reported* original outstanding claims and *self-reported* eligible reserves. Initial owner holdings must sum to the declared outstanding claims.

It then permits only four operational categories:

1. **Transfer** existing units between holders of the *same* external claim class.
2. **Funded dividend** from a pool to distinct synthetic recipient labels, subject to an explicit retained buffer.
3. **Redemption request** that locks holdings without destroying the issuer's outstanding liability.
4. **Cancel request** to restore the claim, or **assume completed delivery** to model its retirement after a hypothetical off-chain event.

There is deliberately **no ORD mint, reset, conversion rate, cross-custodian exchange or unilateral issuance**. Different issuer/custodian/contract rights remain separate even if the physical metal looks identical. A repeated claim-rights description under a different asset ID is rejected within the supplied manifest; this cannot detect double-pledging outside that file.

### Conservation invariant

For every externally identified claim class, after each event:

    initial declared liabilities
      = available claims + locked redemption claims
        + retired claims treated as delivered in the synthetic scenario

And for every distribution:

    allocated claims <= pool's existing claims - committed retained buffer

A redemption **request** is never proof that the underlying metal has left a vault. An "assumed delivery" event here is not an actual metal delivery receipt, and cannot be used to extinguish a real person's property rights. A real implementation would additionally require authenticated rights-holder consent, independent discharge evidence, status transitions, escrow, failed-delivery recovery and dispute resolution.

## Frank and Bob sample

The sample has two imaginary external claim issuers: one for copper gram claims and another for gold milligram claims, with different custodians and rights. Two donors transfer portions of their already declared balances to a fund. Frank, Bob and Casey receive funded copper allocations; Frank and Bob receive funded gold allocations. Frank freely trades some copper to Bob; Bob transfers copper to an imaginary competing compute seller. Frank's pending gold redemption is cancelled without retiring his liability; Bob's copper delivery is explicitly **assumed**, not verified.

No ORD asset is minted. The demonstration confirms only the internal algebra and declared asset separation. It does not verify any person's identity, a consent signature, real exchange consideration or economic value, nor does it depend on a central ORD wallet.

From a fresh public clone:

    python3 examples/issuer_neutral_distribution.py
    python3 -m unittest discover -s examples -p 'test_*.py'

Python 3.10+, no non-standard packages, server, blockchain or credentials.

## What remains **unverified** even if all tests pass

- Physical bars/lots, purity, legal title, lien status and custodian solvency.
- Completeness of the issuer's total obligations, including bridges, liens, double pledges, derivatives, nominee holdings and off-ledger claims.
- Whether the recipient's legally enforceable right is direct allocated property, beneficial fractional co-ownership or an unsecured contractual IOU.
- Whether legal transfer of the commodity right actually occurs when an account balance changes in the sample.
- Cryptographic authorisation, independent witnessing and non-replay of submitted transfers. The model accepts a **local unsigned JSON file**, not authenticated instructions.
- Unique human eligibility, privacy, appeal rights, excluded populations and multi-period entitlement funding.
- Market liquidity, feasible delivery sizes, custody expense, cross-jurisdiction law and a sustainable real-asset endowment.

For these reasons every sample result reports **physical_reserves_verified=false**, **title_rights_verified=false**, **complete_external_liabilities_verified=false** and **redemption_delivery_verified=false**, regardless of accounting balances. A balanced self-reported inventory is not proof of reserves.

## Independent acceptance questions

1. Can a first provider demonstrate independently inspected and unencumbered metals *and* enforceable small-holder title, rather than merely an issuer-controlled digital account?
2. Is the holder able to transfer title or leave through an independent counterparty without mandatory resale to the original issuer?
3. Can the pool obtain meaningful *recurring* assets through legitimate voluntary ownership/revenues, not mint events?
4. Can an auditor independently prove all obligations including encumbered or externally wrapped claims?
5. Can unique universal entitlements be allocated without making recipients expose their identities to a public ledger?
6. Could independent providers represent the same type of rights without disguising different custody/legal risk?

**RFC decision: none.** This is an option for evidence-led discussion, not an endorsed issuer or a commitment to a currency launch. See [Research Discussion #12](https://github.com/Christopher-Charman/open-resource-dividend/discussions/12), [funding issue #2](https://github.com/Christopher-Charman/open-resource-dividend/issues/2) and [custody issue #3](https://github.com/Christopher-Charman/open-resource-dividend/issues/3).

Related: [independent legal title](TITLE_AND_CUSTODY.md), [real funding](VALUE_AND_FUNDING.md), [resource-claim alternatives](RFC_0001_RESOURCE_CLAIMS.md).

**No tokens, actual metal, external issuer integration, funded pool, identity registry, payment service or investment offer exists in ORD.**
