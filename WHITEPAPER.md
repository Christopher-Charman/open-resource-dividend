# Open Resource Dividend (ORD)
## An open, physically redeemable universal economic entitlement for an AI-transformed economy

**Discussion white paper · Version 0.1 · 31 October 2026 · Research proposal, not a deployed currency**

> **Status and limitations.** This document specifies a hypothesis for public examination. No ORD tokens are issued, no metal is held, no entitlement is funded, and no redemption, liquidity, investment return, or regulatory status is promised. This is not an offering or financial advice. The originality of the *combination* has not been established by an exhaustive prior-art review.

### Abstract

AI and automation could shift production away from direct human labour and toward ownership of compute, energy, materials and infrastructure. Universal Basic Compute responds by distributing access to AI capacity, but access issued by a particular provider can recreate dependency on that provider. ORD explores a different starting point: a universal *economic claim* on finite, independently verified physical resources, voluntarily transferable and redeemable, usable in any competitive market—including AI compute—but not restricted to AI.

The open market, rather than an AI provider, determines what recipients purchase, produce or exchange. An append-only ledger supplies independently inspectable accounting history. Physical auditing and enforceable property rights connect recorded claims to real-world backing. The proposal must solve the funding of universal entitlement without making unbacked claims, rather than silently assuming a perpetual mint.

### 1. Motivation: AI is the disruption; openness is the goal

An AI-bound economy may make access to productive computation economically significant. But **an individual need not use AI to participate in its economic benefits**. A person living simply must be free to sell, hold, redeem or exchange their entitlement with somebody seeking more compute. No provider-specific quota should confine how entitlement is spent. Voluntary exchange and individual property rights—not enforced equal outcomes or compulsory resource circulation—are core assumptions.

ORD is **not** an AI token standard, an assertion that linguistic model tokens are interchangeable, or a requirement that AI inference be purchased. AI providers are ordinary, competing sellers in a wider market.

### 2. Proposed principles (design objectives, not verified properties)

1. **Universal entitlement:** every eligible person can receive a periodic distribution from a *funded pool*; no AI adoption or employment requirement.
2. **Non-discretionary resource backing:** every outstanding redeemable claim corresponds to independently verified, unencumbered and legally claimable resources. An index tracking metal prices is not equivalent to backing.
3. **Voluntary exchange:** holders may spend, transfer, accumulate, sell, donate, or redeem claims, and may retain the acquired resources indefinitely.
4. **Provider neutrality:** no AI provider, marketplace, government, custodian or issuer should be a necessary monopoly counterparty for trade.
5. **Open verification:** reproducible public rules, cryptographic history, supply/claims proofs and independent audits.
6. **Private persons, public integrity:** public liabilities and reserve aggregates should be inspectable without requiring public disclosure of every individual's holdings.
7. **Correctability without silent rewriting:** append-only events and explicit reversals/compensations, with disclosed governance and contingency handling.

### 3. Terminology and scope

- **Resource claim:** a defined, enforceable right to a specified quantity, grade and delivery jurisdiction of a metal, held as approved collateral. Example metal classes for research: gold (Au), silver (Ag), copper (Cu).
- **ORD accounting / exchange unit:** a proposed transferable representation of a resource entitlement. Its denomination, fungibility and exchange mechanism are *undecided*.
- **Universal dividend:** a distribution of *already-funded* rights; it is not free issuance of uncollateralised promises.
- **AI tokens:** model/provider-specific metering units for inference. A resource claim can be **exchanged for** inference through a market, but it is not intrinsically one inference token.
- **Append-only ledger:** a verifiable event history for claims, transfers, minting, burning and disclosures; it does not itself prove that a bar of metal exists.

### 4. Layered conceptual architecture

**Layer A — Physical asset and legal title.** Approved custodians certify location, mass, purity, grade, insurance, lien status, legal ownership and delivery conditions. Copper is especially challenging because quality, lot size and warehouse delivery may not suit small retail redemption.

**Layer B — Independently audited reserve registry.** Independent physical inspections and independent liability checks reconcile eligible inventory with all outstanding claims, including those held through bridges or intermediaries. Every report is timestamped, signed, identifies its scope and states observation limits. A price oracle is *not* an inventory audit.

**Layer C — Append-only claims ledger.** Permissionless verification of issuance, transfer, redemption instructions and reserve commitment history. Validator incentives, consensus/finality, decentralisation, key recovery and governance are subject to research; choosing a blockchain alone does not make governance independent.

**Layer D — Universal dividend pool.** A separately governed pool holds actual resource claims or receives real revenue with which to acquire them. Individuals are allocated transfers out of this pool; distributions are not created by a perpetual unbacked mint.

**Layer E — Open exchange.** Buyers and sellers trade claims, physical metals, goods, services and AI capacity voluntarily. Multiple compute providers can quote the amount of work they supply per unit of resource value; model quality, latency and price vary freely.

### 5. Accounting invariants and lifecycle

For each resource class `m` at time `t`:

```text
R_m(t) = eligible, verified, unencumbered reserve quantity
L_m(t) = total enforceable outstanding liability for that resource
Safety invariant: L_m(t) <= R_m(t)
```

The invariant must be checked for **each metal**; mark-to-market basket values cannot silently substitute copper for missing gold unless a holder's contractual rights explicitly permit that substitution.

**Illustrative operations:**

- **Deposit:** accept metal only after title, authenticity, quality and custody are verified. Then issue exactly the corresponding new claims with a unique asset reference. No issuance merely because a price rises.
- **Transfer:** move claims between holders while keeping aggregate liabilities unchanged.
- **Universal distribution:** transfer *existing* claims from the dividend pool to verified recipients. Do not invent matching backing.
- **Redemption:** lock and extinguish the appropriate claim through a recorded state transition, and release the specified material under a linked delivery procedure. Real-world delivery is not cryptographically atomic; the protocol must document escrow, failed delivery, compensation and dispute resolution. Prevent duplicate redemption.
- **Adjustment:** publish a new compensating event, not hidden history editing. Compensating events cannot make missing metal reappear.

A simple funding constraint for each distribution period is:

```text
claims allocated in period <= verified funded pool at period start
                            + independently settled contributions in period
                            - previously committed claims
```

The **central unsolved economic problem** is the ongoing source of that funded pool at global scale. Possibilities for analysis—not approved mechanisms—include voluntary contributions, rights to actual resource-derived revenues, a legally constituted resource trust, or market-purchased reserve additions. No one of these is assumed feasible, universal or politically neutral.

**Empirical feasibility research (31 October 2026):** A [dated, reproducible copper scale envelope](research/COMMODITY_SCALE.md) uses 2025 worldwide copper mine production and an approximate 2026 population to quantify the material requirements of a universal allocation. Under an *unfunded counterfactual* of 1% of annual mine output, the calculation yields only ~28.5 grams of copper content per person, before fees or converting raw output to deliverable custody stock. This is **not an available resource pool or evidence of viable income**. A separate [dual-book demonstration](examples/compare_books.py) confirms why internally consistent append-only records cannot establish the actual reserves. Candidate mechanisms remain open in [RFC 0001](research/RFC_0001_RESOURCE_CLAIMS.md).

**Purchasing-power stress test:** The [open external-funding model](research/VALUE_AND_FUNDING.md) separates real endowment income and market purchases from the legal ownership of metal received by individuals. As an order-of-magnitude *hypothetical*, an allowance of metal valued at $100/person/year for 8.3 billion people requires roughly $946 billion of settled annual funding under its example costs and buffer. No funding source or large-volume physical market access is verified, and the assumed price would likely change dramatically at that scale. The dollar value is a reporting benchmark, **not a token peg or compulsory spending destination**.

**Broader metal comparison:** The copper calculation alone is not representative of ORD's prospective Au/Ag/Cu resource basket. The [2025 gold, silver and copper mine-flow comparison](research/THREE_METAL_COMPARISON.md) now uses primary supply sources for all three. Under explicitly assumed external prices, even a fictional 1% contribution of *each* annual global mine flow equates to only about $1.045/person of reference value. This is not a proposed distribution, real ownership, a fungible fixed basket, or an argument for seizing resource owners' property. Aboveground existing stocks, voluntary trade, endowment income and actual physical custody are distinct economic requirements.

**Issuer-neutral implementation alternative (under public review):** [RFC 0002](research/RFC_0002_ISSUER_NEUTRAL_DISTRIBUTION.md) explores distributing **already-owned external resource claims** rather than minting a new ORD currency. An [offline sample](examples/issuer_neutral_distribution.py) models distinct copper and gold claims from separate fictional custodians, voluntary transfers and an unextinguished liability during a pending redemption. It does **not** establish independent ownership evidence, real physical reserves, universal human eligibility or an adopted design. This alternative is compatible with the open-market motivation while making the remaining trust in existing issuers explicit.

### 6. Frank and Bob: an essential counterexample to provider-tied compute

Frank rarely uses AI. Bob wants more computational capacity than his periodic entitlement can purchase. Frank freely offers some of his resource claims—or the metal he has redeemed—in exchange for goods or services Bob can supply. Bob can then buy inference from whichever operator offers suitable terms. Frank still benefits from the AI-driven economy without consuming AI. He may decline any offer and retain his assets.

The value of the exchange depends on both parties' preferences and genuine property rights. It is not guaranteed that every desired trade clears; warehousing, liquidity, shipping, spreads and market power impose real constraints.

### 7. Audit model, threats and independence

A credible design would need at least:

- **Proof of liabilities** for every outstanding direct and wrapped claim, across all authorised ledgers and custodial ledgers.
- **Proof of reserves** grounded in independent physical inventory counts, assay, legal title, encumbrance searches and insurance/custody checks. Cryptographic commitments to custodian statements do not independently prove physical possession.
- **Conservation and non-reuse** of unique warehouse lots, with no double pledge, fractional or rehypothecated backing unless explicitly disclosed and contractually permitted (the initial proposal disallows it).
- **Public issuance and redemption events**, independent reconciliation of totals, monitorable exceptions and reproducible validation software.
- **Custodian and auditor plurality**, transparent conflicts of interest, governance limits, key rotation and emergency handling.
- **Privacy-preserving proof of unique eligibility**, resistant to multiple identities (Sybil attacks) without turning individual eligibility into a universal surveillance ledger.
- **Operational and legal recourse** if a vault fails, delivery is contested, governance is captured or a chain reorganises.

Append-only history provides evidence against undisclosed alteration, not a guarantee against fraudulent original entries, coerced validators, captured auditors or insolvency. Open source and independent auditing are both necessary inputs; neither substitutes for enforceable ownership rights.

### 8. Competition and its limitations

Holders should be free to redeem, store and resell metals. Suppliers compete for holders' claims; holders compete for useful goods, services and compute. Improvement in AI efficiency can increase work purchased per unit of commodity-backed value. But open trading does not guarantee competitive supply: semiconductor fabrication, land, energy grids, logistics, patents, warehouse infrastructure and governance can still concentrate market power. The hypothesis should be evaluated, not asserted as a theorem.

Material choices are research inputs, not immutable dogma: gold, silver and copper differ drastically in storage economics, industrial demand, divisibility, environmental cost and delivery minima. Compute consumes electricity and uses more than these three metals. The case for backing with precisely these commodities requires empirical comparison with alternative baskets or separate assets.

### 9. Open design choices

1. **Nature of claims:** three individually redeemable tokens, a fixed-weight basket with enforceable delivery, or a transferable claim with holder-selected conversion? Do not conflate these.
2. **Denomination:** mass units versus a neutral settlement numeraire; what happens to commodity price risk?
3. **Eligibility:** how to recognise unique people while respecting privacy, jurisdiction and differing legal identities?
4. **Funding:** which real assets or income support recurring distribution, who originally owns them and who may withdraw them?
5. **Custody:** independently auditable, distributed vaults and robust delivery rules; minimum redemptions, fees, cross-border taxes and sanctions compliance.
6. **Governance:** who can amend rules, emergency stops, claim semantics and dispute resolution? How to avoid validator, foundation or custodian capture?
7. **Infrastructure:** what ledger is sufficient, and does an existing audited platform avoid needless chain creation?
8. **Competition:** can independent compute sellers actually accept the entitlement with low friction, or will exchange be dominated by intermediaries?
9. **International law:** what are the property, securities, money transmission, consumer and financial-promotion regimes in each jurisdiction?

### 10. Investigation, falsification and roadmap

**Phase 0 — Prior art and critical review.** Reproduce the comparison in `PRIOR_ART.md`; solicit serious critiques from monetary economists, property/custody specialists, commodity market practitioners, cryptographers, auditors and AI-infrastructure operators.

**Phase 1 — Economic feasibility.** Write a flow-of-funds model showing where real backing and recurring dividend assets originate, including conservation across mint, distribute, trade, redeem and default. Compare copper-heavy vs gold-heavy costs and divisibility. Initial candidate funding routes and a reproducible accounting toy example are now documented in [FUNDING_MODELS.md](FUNDING_MODELS.md); no source of sustainable global distributions has been verified.

**Phase 2 — Formal event/accounting model.** Produce an open, non-financial toy simulator and machine-checkable invariants. No actual token sale, live collateral, or private identity records.

**Phase 3 — Legal and independent-audit design.** Seek specialist review before any deployment, public solicitation, promised redemption or custody of value.

**Falsification / pause criteria:** inability to specify an enforceable redemption right; inability to fund distribution without undisclosed liabilities; double-pledged reserves; unverifiable eligibility at acceptable privacy cost; inability to redeem at plausible costs; unavoidable capture of critical exchange infrastructure; inability to meet applicable law.

No mainnet, token issuance, fundraising, claims of guaranteed return or physical reserve are proposed for the current repository.

### 11. Relation to prior work

This is not a claim to have invented basic income, tokenised commodities, proof-of-reserves, digital ledgers, decentralised compute markets or Universal Basic Compute. It explores their intersection while keeping ownership of resources and voluntary market exit independent from AI providers.

- Sam Altman, *Three Observations* (2025) — AI compute budget: https://blog.samaltman.com/three-observations
- Sam Altman, Universal Basic Compute interview (2024), transcript: https://lawwu.github.io/transcripts/nSM0xd8xHUM.html
- GoodDollar, *A Distributed Basic Income* — https://whitepaper.gooddollar.org/
- Circles UBI, Protocol Whitepaper (historic v1; check newer version separately) — https://handbook.joincircles.net/docs/developers/whitepaper/
- Kinesis, independent physical gold and silver audit records — https://kinesis.money/audits/
- Akash Network, providers, bidding and leases — https://akash.network/docs/learn/core-concepts/providers-leases/
- *Proof of reserves: a double-helix framework*, British Accounting Review (2025), DOI: https://doi.org/10.1016/j.bar.2025.101730
- UK Financial Conduct Authority, cryptoasset guidance — https://www.fca.org.uk/firms/cryptoassets

The adjacent systems demonstrate components, not the existence or feasibility of ORD. The literature survey is non-exhaustive and dated 31 October 2026.

### 12. Invitation

ORD begins as an open research effort. Critique the assumptions, point to overlapping work, disprove an invariant, improve the economic model or offer better non-fiat designs. Disagreement and negative results are valued. See `OPEN_QUESTIONS.md` and `CONTRIBUTING.md`.

**Provenance:** Concept arose from an exploratory discussion by the repository owner on 31 October 2026; this first draft was prepared with AI assistance and is subject to public revision.
