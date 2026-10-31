# ORD RFC 0001 — What exactly must be tokenised?

**Status: OPEN DESIGN ALTERNATIVES, not a chosen implementation · 31 October 2026**

## The core economic objective

A universal recipient such as Frank should own something he can keep, transfer, redeem or voluntarily sell—even if he never uses AI. Bob should be able to acquire more from Frank and buy whatever compute he wants from competing providers. Neither should have to trust the AI provider as monetary issuer. Resource scarcity and public, independently auditable accounting are hypothesised constraints on discretionary creation.

**A token is not wealth.** This requires independent answers to *three* questions: (A) what asset does the token represent, (B) where does the dividend pool acquire legal ownership of that asset, and (C) how are legitimate transactions recorded and audited? Confusing them creates a fiat-like system regardless of ledger technology.

## Candidate architectures

### A — Independent, single-resource title receipts (minimum monetary novelty)

A participant may own an independently enforceable fractional claim to specific, eligible copper, silver or gold in a defined custodian and jurisdiction. Multiple issuers could use compatible open accounting formats and a common exchange interface. The entitlement fund buys/receives **existing claims** and transfers them to recipients. Voluntary market exchange selects value across resources and compute providers.

**Advantages:** one quantity/grade/unit per liability; direct per-metal reserve accounting; different participants may favour different metals; no algorithmic basket pegging. **Disadvantages:** issuer/custodian insolvency, retail delivery minima, legal title fragmentation, reserve audits and exchange-rate costs; a token traded at a discount may have poor exit liquidity.

### B — Fixed basket with explicit physical-delivery rights

A share is a legally defined and properly backed bundle (e.g., specific weights of gold, silver and copper), **not** an index tracking market prices. The exact bundle, grade, custody, fees, substitution rights and redemption rule must be in the contract. Individual tokens may be backed by a segregated bundle or a legally enforceable pro-rata share of identified lots.

**Advantages:** price exposure can differ from any single material and an accounting unit might be easier to quote. **Disadvantages:** complex logistics, potential redistribution of commodity risk, correlated physical custody failure, and hidden operator discretion unless the exact basket and delivery mode are fixed. An exchange of one metal for another must be a **real voluntary trade**, not an unreported governance reweighting.

### C — Neutral dividend distribution over pre-existing, independently backed assets

ORD would be an *open distribution / interoperability protocol and research governance process*, not a new central currency issuer. Independent trusts or cooperatives receive actual claims on externally audited metals from multiple custodians. They allocate existing entitlements through provider-neutral rails. Recipients can hold, sell or redeem under each asset's published rules.

**Advantages:** minimises new monetary authority, may re-use proven asset custody systems, and makes the economic problem (who contributes) explicit. **Disadvantages:** varied legal rights/fees make assets non-fungible; dependence on issuer standards remains; independent custody/title and complete liability audits must be demonstrated; no universal funding arises merely from combining issuers.

### D — Compute quota or AI-provider token (explicit non-goal)

Every person receives credits restricted to inference services, or a unit that is only redeemable against a particular compute provider.

**Problem for the original ORD objective:** Frank would be dependent on provider exchange rates or on finding a buyer for a closed service even if he prefers not to use AI. It can be a separate public benefit, but it is not a substitute for an open, physically redeemable resource claim.

## Tests any design must survive

| Scenario | Required answer |
| --- | --- |
| Frank wants to hold physical copper rather than AI compute | Is independent legal delivery realistically enforceable after aggregation/fees? |
| Bob wants to buy more than an individual allowance | Can Frank transfer and Bob acquire claims on neutral market terms? |
| One vault fails or turns out to have a lien | Which specific claims lose backing, and can owners seek recourse without discretionary new issuance? |
| A metal goes up or down in price against others | Who bears price change? Can policy rewrite redemption weights retroactively? |
| Worldwide eligible population grows but income does not | Does the payout shrink or pause, or are unbacked claims minted? |
| A third-party bridge wraps a token | Does the canonical liability remain one underlying claim, with wrapped promises fully disclosed and not double counted? |
| Repository founder is inactive | Can community researchers independently reproduce results and reject the design without requiring the founder's consent? |
| All holders request physical delivery | Can the system fulfil contractual delivery terms, or is the promise secretly conditional on continued secondary-market buyers? |

## Proposed provisional research order

**First test architecture C against A, then B only if the exchange benefits justify complexity.** This is a **study priority**, not a governance selection or mandate to adopt any third-party token. The most dangerous failure would be creating a new financial instrument before verifying title, collateral, dividend funding, and the costs of universal access.

Success is not a code repository full of smart contracts; it is an openly falsifiable monetary and legal model. That model should invite independent review by economists, mineral market specialists, lawyers, auditors, cryptographers, and AI infrastructure buyers.

## Decisions still explicitly unmade

- No issuer, custody provider, warehouse, chain, token name/symbol, exchange, validator organisation or legal form is selected.
- No funding source, universal income amount, eligibility authority or reserve asset is committed.
- No public token offering, sale, redemption promise, investment product or adoption plan is authorised by this RFC.

## Open question to the community

**Which option best preserves Frank's independence, Bob's freedom to purchase compute, and everyone else's enforceable physical ownership without simply recreating concentrated issuance power?**

Submit sources, counterexamples and proposals through public GitHub Discussions and issues. Evidence that all options fail is a valuable outcome.
