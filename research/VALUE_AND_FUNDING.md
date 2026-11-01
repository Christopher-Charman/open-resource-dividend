# What could a universal resource dividend actually be worth?

**ORD research note · 31 October 2026 · v0.1 · reproducible counterfactual, not a valuation, payment, fundraising scheme or forecast**

## Why this matters

The previous [physical quantity study](COMMODITY_SCALE.md) measured grams per person if a fraction of worldwide copper mine output were hypothetically transferred to a universal fund. **Mass is not the same as economic purchasing power**. This paper asks the inverse: if a legally funded, independent dividend pool acquired metal in an open market, how much metal could it *hypothetically* distribute, and how large would the contributing income or capital have to be?

This is **not a proposal to peg ORD to the US dollar**. USD is only a reporting numeraire to compare external market prices and potential recipients' purchasing power. In the proposed real-asset system the entitlement is defined in physical metal or enforceable property rights, not dollars. A quoted value is not a promise that anyone will buy or redeem at the quote.

The essential distinction is:

```text
REAL FUNDING: an existing owner legally commits income/property
       ↓ (funds actually settle; costs paid)
PURCHASE: market participants voluntarily sell identifiable physical metal / valid claims
       ↓ (custody, title and audit actually verified)
CLAIM POOL: holds existing legally enforceable backed assets
       ↓ (publicly accounted distributive transfer)
RECIPIENT: can hold, sell, transfer, aggregate or legally redeem within stated terms
```

Neither a blockchain nor a hypothetical endowment generates the first three real-world events.

## Public inputs and explicit assumptions

| Parameter | Model assumption | Status |
| --- | ---: | --- |
| World population | **8.3 billion** | Rounded 2026 example, not a verified eligibility count; [UN World Population Prospects](https://population.un.org/wpp) |
| Comparative copper flow | **23,665,300 tonnes of mined copper content during 2025** | [COCHILCO August 2026 statistics](https://boletin.cochilco.cl/productos/boletin.asp?anio=2026&mes=08&tabla=tabla34); a **flow**, not an available pool or refined warehoused inventory |
| External copper market quotes | **$7,000, $14,000, $28,000 per tonne** | Chosen **hypothetical sensitivity points**, NOT exact observed prices or bulk executable quotes. The [World Bank Pink Sheet](https://www.worldbank.org/en/research/commodity-markets) is a primary source to consult when upgrading to dated observations |
| Annual settled external funding | **$10 billion, $100 billion, $1 trillion** | Counterfactual donated/earned sums, *none pledged to ORD* |
| Fixed administrative/custody cost | **$50 million yearly** | Simplifying assumption, NOT a cost estimate |
| Variable annual operating costs | **1.5% of funding** | Illustrative assumption, NOT a surveyed rate |
| Metal acquisition price premium | **1% over reference quote** | Illustrative spread, NOT a market quote |
| Claims withheld as reserve in dividend pool | **10% of purchased claims** | Illustrative liquidity/operational buffer, not a loss of backing |
| External income from hypothetical productive endowment | **4% realised in a period** | Pure scenario input, **not** a forecast, guaranteed return, risk-free yield or commitment to endow ORD |
| Wholesale LME Grade A copper delivery lot | **25 tonnes** | [LME contract specification](https://www.lme.com/Metals/Non-ferrous/LME-Copper/Contract-specifications), a comparison of scale **not** ORD retail redemption |

All combinations are openly specified in [value_funding_inputs.json](value_funding_inputs.json). The model is implemented in [value_funding.py](value_funding.py), using standard-library `Decimal` arithmetic and three focused tests. No actual market feed is fetched, no account receives anything, and there is no escrow, asset registration or reserve.

## 1. If $10 billion, $100 billion or $1 trillion were truly funded

At an **assumed $14,000/tonne** copper reference quote:

| Hypothetical **annual settled funding** | Divisible metal per person, after model costs and retained pool buffer | Approximate *reference* USD value per person/year | Metal purchased as share of **2025 annual mine output** |
| ---: | ---: | ---: | ---: |
| $10 billion | **75 g** | **$1.05** | **2.93%** |
| $100 billion | **755 g** | **$10.57** | **29.42%** |
| $1 trillion | **7.55 kg** | **$105.74** | **294.34%** |

**The last column is a scale comparison, not a supply forecast.** Even 29% of a past year's mined flow is a staggering counterfactual acquisition demand at a static price. Over 100% of annual production is *not a mathematical impossibility* because existing stocks, scrap and recycling also exist; however it emphatically cannot be assumed purchasable at an unchanged wholesale quote, or to meet custodial standards, anywhere close to automatically.

Price changes alter **mass** while the model's nominal, price-quoted per-person amount stays nearly unchanged at a fixed budget (because it assumes a price-taking buyer). At a $100B funding scenario:

| Assumed copper quote | Potential mass per recipient | Metal purchase vs past world annual mine flow |
| ---: | ---: | ---: |
| $7,000/t | ~1.51 kg | ~58.84% |
| $14,000/t | ~755 g | ~29.42% |
| $28,000/t | ~377 g | ~14.71% |

**This is not price elasticity modelling.** At these quantities, purchases would change the price, supply, competing industrial use and feasible total distribution. The simple fixed-quote assumption is particularly unreliable at scale. A meaningful model will need market depth, substitute metals, inventory, recycling, price response, mine expansion, geography and time.

## 2. Reverse question: what income supports $100 of metal value per person per year?

```text
N = people in dividend period
T = hypothetical reference value per person (USD/year)
p = acquisition premium relative to quotation
b = fraction of fully acquired resource claims retained in the pool
o = operating expense fraction of settled funding
F = annual fixed administration/custody assumption

Required external funded income = [N*T*(1+p)/(1-b) + F] / (1-o)
```

With `N=8.3 billion`, `T=$100`, `p=1%`, `b=10%`, `o=1.5%`, `F=$50 million`, the calculation requires **approximately $945.68 billion/year in settled external funding**, before unmodelled costs and market price impacts.

If that funding were generated by a hypothetically independent productive endowment yielding **4% of capital in one year**, the capital implied by this single-period *arithmetic* is approximately **$23.64 trillion**. Neither the endowment nor its returns exist in ORD. Investment income can be zero or negative, and compulsory transfer of somebody else's capital is **not** an assumption of this project.

The same numbers, if routed entirely through copper at the example $14,000/t quote, imply over **59 million tonnes of *distributable* copper**, with additional retained metal reserves—far more than cited annual mine production. A hypothetical $100 benchmark for all of humanity therefore does **not** demonstrate that a copper-only physical implementation could buy the needed metal.

This reverse result is a nominal *benchmark*, not a fixed dollar payout proposal. It assumes external contributors voluntarily fund the economic entitlement and holders are allowed to freely exchange it.

## 3. Practical exit: a fractional entitlement can be worth less than a redemption fee

At the hypothetical **$10B income / $14,000 copper quote** case, annual reference metal value per person is about **$1.05**. Even a purely hypothetical $5 delivery-processing charge would exceed that amount; no copper retail fee or right is established. More usefully, [the actual sourced gold/silver provider comparison](REDEMPTION_EVIDENCE.md) finds that **Kinesis publishes 100 KAU (100 g gold) / 200 KAG (200 troy oz silver) physical-delivery increments, 0.45% of value plus a fixed $100 administration charge and variable shipment costs**. Paxos requires **430 PAXG plus fees** for direct allocated gold-bar delivery to eligible verified customers. At this paper's independently labelled hypothetical metal prices, that implies significant accumulation even for a funded **$100/year** entitlement; see the fully worked table. None are ORD-approved outlets, and the comparison does not rule out voluntary secondary-market sales or lawful competing aggregation.

This creates a tradeoff worth testing:

1. **Accumulate:** Frank retains claims for multiple periods until his holdings exceed a realistic delivery minimum.
2. **Transfer/trade:** Frank freely sells small claims to Bob or a competing aggregator, with open price discovery.
3. **Pooled redemption:** holders voluntarily aggregate fractional property for physical delivery and divide proceeds, assuming legal title and enforceable rights permit it.
4. **Issuer-dependent cash-out:** a single operator buys small holdings at an announced rate. This is easier to implement but risks recreating the discretionary counterparty that inspired ORD.

Options 1–3 should be compared against actual custody terms, losses, spreads and bankruptcy rights. A publicly tradeable token that is practically never physically redeemable is a different financial promise than the proposed independently redeemable resource entitlement.

The [redemption evidence](REDEMPTION_EVIDENCE.md) now clearly separates **published Kinesis/Paxos customer redemption thresholds and fee schedules** from **LME/LBMA wholesale settlement specifications**, with actual terms, illustrative prices and conditions. No source establishes globally available, legally independent **retail copper** redemption or an ORD partnership.

## 4. What could make the economics work differently?

This exercise **does not prove all physical commodities are unsuitable**. A different reserve basket with smaller storage-volume requirements, or an issuer-neutral pool distributing already existing audited assets, may be more tractable. Yet each substitute must meet the same legal title, custody, total liabilities, costs, and independently financed distribution requirements.

A future credible comparison would need:
- **Gold and silver flows and above-ground stocks** sourced from current dated primary reports, avoiding invented reserve ownership.
- **Multiple independent custody issuers** with genuine retail delivery and liability-auditing evidence.
- **Actual market depth/price response** instead of assuming a sovereign-scale buyer can transact at a fixed spot quote.
- **Voluntary capital formation / income ownership** at a scale large enough for recipients to obtain meaningful resources.
- **Eligibility coverage and operating costs** at global scale, without making an identity monopoly or surveillance ledger.
- **Enforceable delivery** with small-lot pricing, availability, dispute resolution and insolvency treatment.

This is why the [open RFC](RFC_0001_RESOURCE_CLAIMS.md) examines whether ORD should be a neutral distribution mechanism over real, independently held assets, *not* necessarily an issuer or new blockchain.

## 5. How to reproduce or falsify

```bash
python3 research/value_funding.py
python3 -m unittest discover -s research -p 'test_*.py' -v
```

All inputs are published; no dependencies, API key, network or proprietary data is required. Modify the sample **as a separate labelled scenario**, not as a claim that prices or donations have been observed. Report what assumptions, evidence and sensitivity fail.

The script intentionally reports:
- `status: HYPOTHETICAL_UNFUNDED`;
- `actual_assets_or_income_committed: false`;
- `physical_acquisition_at_this_quote_verified: false`;
- `legal_title_verified: false`;
- `endowment_is_pledged_or_exists: false`.

**Research conclusion:** A commodity-backed *claim* can be sound while a universal *income* remains materially too small or underfunded. Neither scarcity nor immutable accounting automatically makes a globally meaningful endowment exist. That distinction should guide the next iteration, and outside critics should feel free to disprove the chosen assumptions.

Related: [quantity envelope](COMMODITY_SCALE.md) · [funding model](../FUNDING_MODELS.md) · [architecture](../ARCHITECTURE.md) · [community research discussion](https://github.com/Christopher-Charman/open-resource-dividend/discussions/12).

*No actual ORD tokens, bullion, fund, payments, legal rights, capital commitment, exchange or trading service exist.*
