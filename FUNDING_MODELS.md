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

### Audited FY2026 Alaska cash-flow precedent: resource receipts are not the dividend budget

The [Alaska Permanent Fund Corporation's FY2026 annual report](https://apfc.org/reports/2026-annual-report/) (published 28 September 2026; financial year ended **30 June 2026**) is a **real, publicly audited funding precedent**, not a funding source available to ORD. Its financial statements and [September 2026 audit announcement](https://apfc.org/fund-news/fy26-audit-and-budget-proposal/) separate existing capital, new royalty receipts, realised income, unrealised investment appreciation and appropriations:

| FY2026 APFC measure | Reported amount | What it means for an ORD funding hypothesis |
| --- | ---: | --- |
| Ending total fund balance | **$91.901004 billion** | Existing invested public wealth, **not** annual distributable income or ORD-owned reserves |
| Mineral royalty deposits into principal | **$535.039 million** | Actual external resource-related receipts in the period; legally committed to Alaska's fund, **not** a voluntary global metal donation |
| Statutory net income | **approximately $8.2 billion** | Realised accounting income credited to the Earnings Reserve Account; varies with investment activity and cannot be equated with settled free cash |
| GAAP net income | **approximately $10.1 billion** | Includes **unrealised** gains; **not** the amount immediately available for annual distributions |
| General Fund distribution during FY2026 | **$3.798888 billion** | Actual reported transfer to Alaska's General Fund, for **public services and dividends together**, not a direct $3.8bn dividend paid to residents |
| Committed FY2027 POMV draw at FY2026 close | **$3.996865 billion** | Committed for a **subsequent fiscal year**; must not be counted again as an FY2026 cash distribution |
| Total reported FY2026 fund liabilities | **$6.327953 billion** | Balance-sheet obligations; includes **$4.767994 billion securities-lending collateral** and other liabilities. Not a second source of unencumbered backing |

**Independent arithmetic check from the report's financial statements:** ending fund balance $91.901004bn = assets $98.228957bn − liabilities $6.327953bn. Reported FY2026 general-fund transfers of $3.798888bn are **less than** the reported ~$8.2bn statutory net income, but that comparison alone cannot establish the spendable, legally appropriated balance for any other purpose. The $535.039m mineral deposits and the fund's investment earnings are **different flows**; adding both to an ORD metal-reserve ledger would be double-counting without actual settled title to independently deliverable metal.

**Transferable design lesson:** A genuinely sustainable distribution institution needs independently evidenced *period-specific inflows*, expenses, appropriations, liquidity and retained capital, and must not confuse (i) physical-resource income or donations, (ii) investment returns, (iii) realised cash available for lawful spending, (iv) funds actually transferred to recipients and (v) audited *unencumbered deliverable metal*. Alaska's audited fund demonstrates the accounting and governance separation, **not** a globally transferable, voluntarily funded or physically redeemable metal right. Its public-law financing and resident eligibility are jurisdiction-specific. ORD's [synthetic funding scenarios](examples/funding_scenarios.py) must continue to represent hypothetical settled contributions as assumptions, not relabel Alaska's actual balances as ORD backing.

### Copper delivery benchmark: wholesale warrants are not small-holder redemption (9 November 2026)

The [LME's current copper contract specification](https://www.lme.com/metals/non-ferrous/lme-copper/contract-specifications) identifies **Grade A copper cathodes**, an **LME-approved brand**, a **25 metric-tonne physical warrant with ±2% tolerance**, and a 25-tonne physical lot. Its **5-tonne LMEmini** is explicitly **cash settled**; it does not provide a five-tonne physical exit. These are exchange contract/warrant specifications, **not a retail copper redemption offer** and not a representation that an ORD holder owns an LME warrant.

The [LME warehouse-charge schedule for 1 April 2026–31 March 2027](https://www.lme.com/en/sustainability-and-physical-markets/warehousing/warehouse-charges) identifies **warehouse rent and Free on Truck (FOT) handling charges** payable by warrant holders. Actual warehouse/location rates and further transport, insurance, customs and delivery expenses must be obtained for the selected destination; the exchange-wide schedule does not justify inventing a flat global small-holder fee. The [LME warrant-collateral FAQ](https://www.lme.com/about/faqs/warrants--as-collateral-faqs) also confirms that warrants can be pledged as collateral while warehouse rent remains payable, reinforcing the need to distinguish physical inventory, pledged warrants and legally available holder claims.

**Worked scale comparison (quantities only, no assumed price):** A hypothetical recipient with **1 kg** of genuinely backed copper claims has **0.001 tonnes**. A standard 25-tonne LME copper warrant is **25,000 kg**, or **25,000 times** that balance; the ±2% warrant tolerance is **±500 kg**, itself 500 times the recipient's holding. Even 5,000 such 1 kg recipients pooled together would reach only 5 tonnes, **not** one standard LME physical warrant. The 5-tonne cash-settled LMEmini does not solve that delivery gap. Pooling 25,000 recipients would reach a nominal 25 tonnes, but does **not** establish collective legal title, transfer of a warrant, warehouse access, custody authority, allocation of fees or permission to redeem. Any pooling/aggregation route requires separately evidenced governance, enforceable beneficial ownership, consent, independently reconciled liabilities and a viable exit for participants who cannot afford or do not want physical shipment.

**Implication for ORD:** A wholesale copper warrant is a useful physical-market benchmark, not an adequate small-holder service. A credible small-holder path needs independently evidenced lower-lot custody/withdrawal terms or voluntary aggregation with explicit cost allocation, opt-out/secondary transfer and insolvency protections. Do not promise retail physical redemption on the basis of exchange-grade inventory alone. This complements the existing [Kinesis and Paxos gold/silver redemption comparison](research/REDEMPTION_EVIDENCE.md) and addresses the copper side of [research issue #10](https://github.com/Christopher-Charman/open-resource-dividend/issues/10).

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

### Operational funding and issuance distinction: GoodCollective versus GoodDollar (7 November 2026)

Two existing, related products demonstrate **different** mechanisms and must not be conflated when considering ORD's voluntary funding:

- [GoodCollective's published product description](https://www.gooddollar.org/goodcollective) describes donor-funded, identity- or activity-specific payment pools. It explicitly charges a **5% network fee on each donation** and permits additional pool-configured administration fees. Thus a purely illustrative **$100 gross donation yields $95 before any additional pool fees**, not $100 of assets available to distribute. This is a **published fee schedule**, not an audited receipt or an estimate of metal custody costs; the donor-funded pool still requires independent verification of what it legally holds.
- [GoodDollar's current architecture](https://docs.gooddollar.org/how-gooddollar-works/architecture-and-value-flow) describes a cryptocurrency reserve, identity verification and daily distributions. Its protocol **mints new G$ by reducing the reserve ratio / increasing leverage**. This is an existing cryptocurrency monetary mechanism, **not a transfer of already-owned, fixed-mass, unencumbered metal claims**. It cannot be assumed to satisfy ORD's `L_m <= R_m` physical-unit rule. Its value-transfer experience is relevant; its issuance economics are **not interchangeable** with ORD's resource-title requirement.

**Quantified funding consequence:** Under the *illustrative assumption* that a proposed voluntary funding channel charged GoodCollective's published 5% network fee (no partnership is proposed or established), acquiring **$1,000,000 of net metal-purchase budget** would require **$1,000,000 / (1 - 0.05) = $1,052,631.58 in gross gifts**, *before* separate administration, storage, audit, purchase premium and delivery costs. That calculation is **not a quote** for ORD, and the actual fee base or applicability of any future provider must be established contractually. For a genuinely funded physical-claim distribution, account for fees **before** acquiring or transferring claims, and do not fill a shortfall by increasing the token supply without newly verified eligible metal.

This comparison tightens the difference between **donation gross receipts**, **net settled acquisition funds**, **existing asset claims transferred** and **new digital money created against a variable reserve ratio**. [Prior-art classification](PRIOR_ART.md) documents the operational versus proposed mechanisms. These findings do not imply GoodDollar, GoodCollective or any other provider endorses ORD.

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

### Endowment-yield stress: funding continuity is not reserve solvency (14 November 2026)

The [reproducible funding model](research/value_funding.py) calculates approximately **$945.68 billion in annual settled external income** for an entirely hypothetical $100 reference-value allocation to 8.3 billion recipients, including its stated cost, acquisition-premium and retained-claims-buffer assumptions. At a *hypothetical* 4% realised annual return, the corresponding capital arithmetic is approximately **$23.64 trillion**. Neither amount exists or is pledged to ORD.

Hold that hypothetical capital constant and vary only the **realised, spendable, settled income** in a period. Values below are rounded and exclude tax, market price impact, capital volatility and any legal restrictions on distributing returns:

| Realised annual return on illustrative $23.64T capital | Settled income available before model costs | Shortfall against illustrative $945.68B funding requirement |
| ---: | ---: | ---: |
| 4% | ~$945.6B | ~$0.1B (rounding) |
| 2% | ~$472.8B | ~$472.9B |
| 0% | $0 | ~$945.7B |

The comparison deliberately holds the initial notional capital constant: it **does not** assume capital can be liquidated, borrowed against or pledged to cover a payout. At 2%, maintaining the *same* illustrative gross income would instead require approximately **$47.28 trillion** of capital, before changes in costs or asset prices. A negative return may impair capital and cannot be treated as negative metal reserves or an authority to issue additional claims.

**Implication:** A fund can remain fully backed in the narrow sense that its *existing* metal liabilities do not exceed eligible reserves, while being unable to finance **new** universal distributions. Its period payout must fall with actual uncommitted pool holdings after expenses and buffers; a fixed payout requires a separate, demonstrably funded multi-period guarantee. The appropriate invariant is `new_distribution <= settled_unencumbered_pool_claims - commitments - retained_buffer`, not `new_distribution = target * population`.

This is a scenario stress test, **not a forecast, investable yield, promised payment or evidence of an endowment**. It extends the funding falsification criterion in [issue #2](https://github.com/Christopher-Charman/open-resource-dividend/issues/2). The same external funding and physical-title verification obligations apply regardless of the return assumption.

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
