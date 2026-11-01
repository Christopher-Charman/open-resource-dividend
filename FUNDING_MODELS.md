# Funding the Universal Resource Dividend
## Feasibility research note · 31 October 2026 · v0.1

**Purpose:** Examine what *real* physical ownership could finance a recurring universal distribution without creating fiat-like discretionary claims. This is a research analysis, not a proposed sale, reserve attestation, token contract or commitment to deliver dividends.

**Result in one sentence:** A commodity-backed token can faithfully represent already-owned physical metal, but the ledger cannot itself generate the *continuing real-asset income* needed for universal allocation. A funded endowment, legally owned productive resource rights, or voluntary ongoing contributions must supply that income, and newly claimed metal must actually enter custody before it backs newly issued tokens.

## 1. The conservation distinction

Separate the **backing ledger** from the **distribution pool**. For metal class `m` (Au, Ag, Cu), define:

- `R_m` = audited quantity of eligible, unencumbered physical metal under enforceable custody/title;
- `L_m` = total outstanding claims redeemable for that metal, including any wrapped or custodial representations;
- `P_m` = claims **already issued and owned** by the dividend pool (a *subset* of `L_m`, not new collateral);
- `N_t` = valid unique recipients in distribution period `t`, as established by a privacy-preserving eligibility process yet to be designed;
- `B_m,t` = a pool-held commitment/expense buffer, expressed as existing claims, that cannot be distributed.

Fundamental rule, **per resource**:

```text
0 <= L_m <= R_m
0 <= P_m <= L_m
0 <= D_m,t <= max(0, P_m,t - B_m,t)
```

Transfers from the pool to recipients (`D_m,t`) reduce `P_m`, but **do not change** aggregate `L_m` or `R_m`. Distributions are not mints.

Additional claims can be created only after an owner deposits *newly eligible, unencumbered physical metal* and passes title, quality, quantity and custody checks. A **future royalty, mining reserve underground, pledged metal, expected investment gain, uncollected receivable or signed warehouse assertion** is not yet eligible reserve metal.

Simplified state transitions, in consistent metal units:

| Event | Physical eligible reserves `R_m` | Outstanding claims `L_m` | Dividend pool `P_m` |
|---|---:|---:|---:|
| Verified new custody deposit of `q`; corresponding claims minted to depositor | +q | +q | unchanged |
| Depositor voluntarily transfers `q` existing claims to dividend pool | unchanged | unchanged | +q |
| Pool distributes `q` existing claims | unchanged | unchanged | -q |
| Holder redeems `q` claims and receives metal | -q | -q | unchanged unless holder was pool |
| Pool pays `q` existing claims for legitimate expenses | unchanged | unchanged | -q |
| Mine promises `q` of future output but has not delivered it | unchanged | unchanged | unchanged |

**Anti-double-counting:** If a trust owns claims on the metal, their backing is already included in `R_m`; that trust's holdings cannot simultaneously be counted as a second independent asset backing the same liabilities. A metal royalty right can be an *income-generating investment of the endowment*, but until delivery it does not also count as the vault's redeemable metal.

For a single universal payout per metal class, a mechanically calculable upper bound is:

```text
d_m,t <= floor_to_smallest_unit(max(0, P_m,t - B_m,t) / N_t)
total allocated D_m,t = N_t * d_m,t
```

This rule guarantees **no over-distribution of the funded pool**. It does **not** guarantee a socially meaningful minimum income, that every eligible person can register privately, or that the metal is obtainable without fees.

### Toy numerical example — NOT a live issuance

- An owner contributes **1,000 verified copper-kilogram claims** already backed by copper held at an approved warehouse.
- A dividend trust now holds `P_Cu = 1,000 kg` in outstanding claims. No new claims were created by the gift.
- It reserves 100 kg of those claims for known expenses or commitments and identifies 100 eligible recipients.
- Maximum funded one-period allocation is **9 copper-kilogram claims per person** (900 kg total).
- All 1,000 kg of claims remain in existence after the transfers, and physical reserves remain unchanged until a holder redeems. They are **not** backed by 1,000 kg *plus* a separate 900 kg.
- The next period has no new funds if the remaining 100 kg are still reserved. A promise of another 9 kg per person would be **unfunded** without new contributions, income, or release of the buffer.

### Why fixed universal payouts are not automatic

A guarantee `d_m,t >= d_min > 0` to an ever-changing population requires a reserve of distributable claims or reliably received real income at least `N_t*d_min` **every period**. No issuance constraint, voluntary exchange, improved AI performance or consensus algorithm creates that metal. Universal *eligibility* can be maintained without promising a fixed periodic quantum; an unconditional fixed minimum needs a credible funding mechanism and contingency reserves.

## 2. Candidate funding sources (distinct economic mechanisms)

| Mechanism | What genuinely enters the pool? | What must happen before minting additional resource claims? | Strengths | Primary unresolved limitations |
|---|---|---|---|---|
| **A. Donated metal or existing claims** | Voluntarily donated title to physical metal or existing resource claims | For metal: verify custody/title, then mint to the donor/trust; for existing claims: simply transfer | Clear origin, no compulsory levy, immediately understandable, compatible with open markets | Finite stock alone does not perpetually fund new dividends; donations are uncertain |
| **B. Independently endowed resource trust** | Existing claims bought or received using legally owned trust income | Acquire and verify actual additional metal in reserve before new claims | Separates productivity/income from redemptions; endowment can compete for assets | Who endows it? Trust governance, returns and costs; principal losses/low income |
| **C. Actual metal-delivery stream** | Metal delivered under an enforceable commercial production contract | **Only after physical delivery and accepted unencumbered title**; delivery payments/fees must be financed | Already-known financing structure; can be privately contracted | Upfront and per-delivery costs, mine downtime, delivery default; expected future tonnes are *not* current reserves |
| **D. Resource royalties or other income** | Contractual revenue paid to a trust, later spent to buy resource claims or actual metal | For cash revenue, convert and settle a physical purchase; allocate existing claims or mint after actual accepted metal | Diversifies potential income sources; precedents for resource-derived dividends | Cash revenue is not in itself a redeemable metal entitlement; timing, taxes, counterparties and volatility |
| **E. Voluntary protocol-service surplus** | Legitimately earned, disclosed fees in resource claims that are transferred into pool | No mint on receipt of fees: existing claims change hands | May fund part of expenses or payouts without new reserves | Fees can make small balances uneconomic and create monopolistic incentives; does not guarantee meaningful UBI |
| **F. Publicly owned resource-rent transfer** | A legally authorised share of existing resource revenues/assets | The receiving fund still must acquire existing claims/verified metal | Strong precedent for resource dividends where communal resource rights exist | Legitimacy and jurisdiction depend on public property law and political choices; not an assumption that state ownership or compulsory contributions are desirable |

Models A–E are compatible with **voluntary private transfers** in principle; model F is a contextual precedent, not the default design. Different regional or global funding trusts could compete or cooperate while accepting an interoperable, independently validated claim format. However, competitive trusts **do not by themselves** guarantee universal geographic coverage.

## 3. Closest economic precedents

### Alaska Permanent Fund: resource wealth -> income -> dividend

Alaska's Permanent Fund converts revenue from mineral-related royalties into an invested public fund, with a distinct earnings account used for public spending and the dividend. The Alaska Permanent Fund Corporation describes a nonspendable principal and a spendable Earnings Reserve Account. Alaska's Dividend Division describes an annual resident dividend funded from investment earnings tied to mineral royalties. This is a precedent for turning finite resource wealth into continuing payments—not for private physical-metal redemption or a provider-neutral AI economy.

- Alaska PFD Division: https://pfd.alaska.gov/Division-Info/about-us
- Alaska Permanent Fund Corporation, fund structure: https://apfc.org/the-fund/fund-structure/
- Alaska constitutional resource-revenue rationale: https://apfc.org/about/a-pioneering-investment-model/

### Windfall Trust: AI wealth -> shared endowment -> universal income

The Future of Life Institute describes a proposed **Windfall Trust** intended to give people a stake in potentially enormous profits from advanced AI, including research into legal structures, investment policy, payout formulas and governance. This is an especially relevant **AI-era universal-wealth** antecedent. The proposal does **not** establish that a global, gold/silver/copper-redeemable entitlement is funded or exists; its emphasis is shared ownership of AI windfalls, not open physical-resource claims.

- Future of Life Institute: https://futureoflife.org/project/the-windfall-trust/

### Metal streaming: contract for future metal -> delivery -> potential backing

Wheaton Precious Metals describes metal streaming as upfront financing plus an additional payment upon the mine delivering a percentage of production. It illustrates a real contractual method by which a fund **could seek** recurring physical metal, but the right to future production must be separated from current, auditable reserves. A contract alone cannot back immediately redeemable ORD claims.

- Wheaton company model: https://www.wheatonpm.com/about/Our-Business-Model/default.aspx
- Independent comparative overview: https://www.mckinsey.com/industries/metals-and-mining/our-insights/streaming-and-royalties-in-mining-let-the-music-play-on

### Real-world redemption has operational friction

[Verified Kinesis customer redemption terms](https://support.kinesis.money/hc/en-gb/articles/38687923843741-Redeeming-Gold-and-Silver-in-App) require **100 KAU or 200 KAG delivery increments**, a **0.45% charge plus $100 administration**, and separately quoted packing and postage. [Paxos's direct allocated-gold redemption terms](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions) require **430 PAXG per London Good Delivery bar plus fees and verified-customer access**. The [fully worked economic comparison](research/REDEMPTION_EVIDENCE.md) shows why a small but genuinely backed universal allocation may not afford direct physical delivery even when transfers or secondary trading are possible. These are **provider-published conditions**, not endorsement, actual ORD title, guaranteed global access or proof that other competing exits cannot exist.

- Kinesis redemption rules: https://support.kinesis.money/hc/en-gb/articles/12439302237085-How-to-redeem-physical-gold-and-silver
- Kinesis audit archive: https://kinesis.money/audits/

## 4. Funding scenarios to investigate first

### Scenario 1: Pure voluntary seed and recurring gifts

A cooperative or charity is granted existing metal claims. It distributes a percentage to all registered participants on an open basis. This needs no AI company or fiat monetary issuer, but there is no mathematically assured **perpetual** dividend. Research must report effective coverage and years of reserves at different intake/distribution schedules, and avoid branding a finite gift as a perpetual UBI.

### Scenario 2: Voluntary resource-income endowment

Legally owned productive interests generate income. Their owner commits a contractually defined portion into an independent fund, which acquires physical metals or already-issued resource claims and distributes them only after settlement. Funds may receive profits from AI companies **without making any provider a currency issuer**. It respects the freedom of participants to buy compute, trade resources or avoid AI entirely. Principal, income, payout governance and eligibility need separate, auditable records.

### Scenario 3: Distributed network of independently endowed pools

Multiple legally separate pools use common accounting and redemption standards. Participants can accept claims from different approved reserve issuers where the legal rights are equivalent, and choose their trading counterparty. This potentially reduces dependence on one trust, but introduces interoperability, equivalence and cross-issuer insolvency questions. A shared ledger does **not** automatically make claims issued by different custodians economically equivalent.

### What cannot be assumed

- "AI productivity will keep increasing" is not a transferable resource stream without ownership of resulting income.
- "Scarcity gives value" does not itself establish yield, reserve custody or guaranteed liquidity.
- "Immutable history" does not establish independent physical asset verification.
- "Universal entitlement" does not prove the fund is sufficiently capitalised for every person alive.
- "A profitable compute provider" does not make universal compute or resource allocation fair or independent by default.
- "Stored gold" does not automatically pay a dividend; its quantity is conserved unless somebody contributes more or willingly transfers some of their stock.

## 5. Candidate research direction, not a settled design

The most tractable first *comparison* is **funded transfers of existing, separately denominated metal claims** under a small, nonfinancial simulation. Start from a real-asset balance sheet model, not a speculative ORD coin or smart-contract deployment. Model a standalone independent trust, one dividend period, at least one redemption, then repeated periods with stochastic donations/realised resource income and expenses.

For each period `t`, publicly report:
- verified, individually redeemable reserves by metal and location;
- total claims outstanding across all issuers and wrappers;
- dividend-pool claims and reserved commitments;
- fully settled sources of the period's contribution;
- participants and privacy-preserving duplicate-eligibility checks;
- distribution per person and forgone payouts if funds are insufficient;
- claims burned, physical material released and failed deliveries;
- independent reserve and liability attestation scope/date;
- custodial, audit, shipping and administrative costs paid.

A falsification criterion for the funding thesis is: **no voluntary or otherwise legitimate resource-income source can meet the desired universal distribution under plausible costs, access and risk**. The system should publish that result instead of moving to unbacked issuance.

### A quantitative challenge to a meaningful payout

The [value and funding feasibility study](research/VALUE_AND_FUNDING.md) turns the distinction between **backing** and **income** into an explicit sensitivity model. At an assumed 8.3 billion recipients, a hypothetical resource entitlement equivalent to **$100 per person per year** would need roughly **$946 billion of settled external income** given the deliberately illustrative cost/spread/buffer assumptions in the file; a 4% realised endowment yield would arithmetically imply about **$23.6 trillion** of capital. No such endowment or income stream has been pledged or identified.

That calculation is not an endorsement of fiat backing, a nominal payout target, a return assumption or a proposal to buy the world's copper. USD is the **external market quote** used to compare the purchasing power of legally acquired physical claims. At large global volumes, unchanged wholesale quotations are demonstrably unreliable modelling assumptions.

## 6. Next research questions

1. Can a legally independent endowment earn *real* income in metal or reliably acquire physical claims without claiming the same metals twice?
2. Who provides initial resources, and do source owners retain genuine choice? What would convince them to contribute?
3. Are full retail redemption rights economical for copper at small allocations, or is aggregation required (and if so, how is it done without issuer discretion)?
4. If contributions are volatile, should payment vary automatically, or is a funded multi-period buffer necessary?
5. Can an interoperable multi-trust system preserve legal title and avoid one validator/custodian/identity authority?
6. Does the value delivered matter more in spendable claims, actual metal, compute, or a basket—and who decides the allocation?
7. How does a recipient prove uniqueness without permitting universal surveillance or excluding people without conventional identity documents?
8. What does "universal" mean when metals, jurisdictions and lawful eligibility are heterogeneous?

**Reproducible illustration:** A four-period, no-dependency [scenario](examples/scenarios/volatile_copper.json) and [simulator](examples/funding_scenarios.py) now expose changing recipient counts, intermittent real-asset contributions (assumed delivered), cost arrears and missed payout targets. Run them using [DEVELOPMENT.md](DEVELOPMENT.md). The example is *not* evidence of an economically viable funding source.

**Summary:** The funding mechanism is independent of the ledger and of AI tokens. A genuinely non-fiat universal resource dividend is a **distribution of enforceable ownership funded by actual assets**, not a command to the ledger to invent wealth.

*This note is provisional. It is not legal, tax, investment or financial advice, and does not imply that physical reserves or tokens exist.*
