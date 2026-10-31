# Gold, silver and copper together: how much of a universal entitlement?

**Research note · 31 October 2026 · reproducible source-labelled counterfactual; not a valuation, reserve, endowment or offered payment**

## Result

ORD was conceived as an **open, voluntarily exchangeable, physically redeemable resource entitlement** motivated by the economic changes expected from AI. Copper is only one possible reserve asset. Gold and silver also matter, particularly because their ownership, price and custody characteristics are very different.

To stop the quantitative research overfocusing on copper, this study compares the three *separately*: each metal's 2025 mine production, units, explicitly assumed market price and hypothetical share of global output.

**Under the deliberately hypothetical prices of $4,000 per troy ounce for gold, $75 per troy ounce for silver and $14,000 per tonne for copper, a contribution of 1% of each metal's entire 2025 worldwide mine output would have a combined reference-market value of only about $1.04 per person across 8.3 billion people.** That output is already owned by someone else, is not fully refined/available at a given custody location, and is **not committed to ORD**. An open ledger cannot allocate it without real legal transfers.

These prices are **round-number scenario inputs**, not World Bank observations, current quotations, acquisition commitments or pegs. The ratio is an accounting thought experiment, not a moral claim over other people's resources.

## Reproducible input sources (2025 material flows)

| Metal | 2025 global mine output | Source and scope | Endowment distinction |
| --- | ---: | --- | --- |
| Gold (Au) | **3,671.6 metric tonnes** | [World Gold Council, 2025 gold supply](https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-full-year-2025/supply), published 29 January 2026. Includes mine production, not total aboveground stock. Industry estimates can differ from government mineral-statistics methodologies. | [World Gold Council 2026 market primer](https://www.gold.org/goldhub/research/market-primer/gold-market-primer-market-size-and-structure) separately estimates **220,700 tonnes aboveground at end-2025**, an existing *stock* with many owners; it is **not available ORD property**. |
| Silver (Ag) | **846.6 million troy ounces**, approximately **26,332 metric tonnes** | [Silver Institute/Metals Focus, April 2026 retrospective on 2025](https://silverinstitute.org/elevated-lease-rates-regional-liquidity-tightness-and-robust-investor-interest-resulted-in-record-silver-prices-in-2025/). Mine production only. | Industrial use, recycling, accumulated inventories, warehouse acceptance and existing title remain separate. Do not infer available metal from annual mine output. |
| Copper (Cu) | **23,665,300 metric tonnes copper content** | [COCHILCO August 2026 statistical bulletin](https://boletin.cochilco.cl/productos/boletin.asp?anio=2026&mes=08&tabla=tabla34). Annual copper-content mine flow, not refined cathode or legal delivery inventory. | A copper mine's output is not automatically legally deliverable in one tonne or 25-tonne retail form. |

These sources have **different industry/statistical methodologies**. The aggregate is a rough comparative exercise, not a precisely matched supply-and-demand balance, and no source establishes the legal ownership needed for ORD issuance.

## The open arithmetic

Using an approximate population of 8.3 billion and a counterfactual **1%** of each 2025 mine-production flow:

| Metal | Hypothetical 2025 mined mass per person | Reference value/person at *illustrative* prices |
| --- | ---: | ---: |
| Gold | **0.004424 g** (~4.42 mg) | **$0.569** |
| Silver | **0.031726 g** (~31.7 mg) | **$0.077** |
| Copper | **28.512 g** | **$0.399** |
| **Total reference value** | **Three separate metal claims, not a physically homogeneous unit** | **~$1.045** |

A 10%-of-all-three-production counterfactual yields approximately **$10.45 per person**, before any costs. A whole year's new mined output from **all three metals combined**, valued at the same deliberately fixed quotations, is around **$867 billion**, or **$104.46 per person** at that illustrative population.

Consequently, **a $100/person/year physical-resource value benchmark would require around 95.7% of the combined nominal value of this particular three-metal annual mined flow** if funded *solely* from these materials at unchanged quoted prices and no costs. That is **not a feasible donation forecast**; it is a stress measure exposing how much wealth would need to move.

Calculation:
```text
hypothetical grams/person = mine-tonnes * flow-share * 1e6 / population

hypothetical reference value/person:
  copper = tonnes * flow-share * assumed USD/tonne / population
  gold or silver = troy-ounces mined * flow-share
                   * assumed USD/troy-ounce / population
```

The values of gold, silver and copper are added **only for this external comparison**. They are **not** merged into a single ORD-backed basket, and they are not proof of collateral or a legal redemption contract.

### Critical constraints that these values cannot settle

1. **Existing ownership:** who owns the mine output? No amount of public ledger transparency creates consent to transfer it. An independently funded trust needs voluntary or otherwise legitimately owned revenues/assets.
2. **Market price response:** acquiring 10%, much less 95%, of global annual mine flow would likely change market prices and supply. These quotes are held artificially fixed only to show scale.
3. **Stock versus flow:** aboveground gold (~220,700 tonnes at end-2025) is much larger than annual production but is held by private and public owners. The ability to exchange for it is **not** a claim it is unowned or freely distributable.
4. **Physical rights:** tiny milligram entitlements can be *represented* digitally, but cost-effective individual bar delivery, enforceable fractional title and insolvency protection remain unproven.
5. **Sustainable recurrence:** even a generous one-off distribution from existing stock is not a perpetually funded yearly dividend.
6. **Cost and yield:** the numbers deliberately exclude storage, fees, logistics, auditing, insurance, legal compliance and endowment investment losses. [The funded-income model](VALUE_AND_FUNDING.md) treats a distinct illustrative cost schedule; it still does not identify a real fund.

### Why this does not reject the thesis

ORD's objective is **economic agency through real ownership and voluntary exchange**, not compulsory distribution of all newly mined metal. A legitimate independent endowment could potentially obtain already owned gold, silver or copper claims from willing sellers. Recipients would remain free not to use AI; Bob could voluntarily acquire Frank's holdings. That requires actual existing property and a source of income—not a token-mint shortcut.

The investigation should therefore prefer **identifying an independent and lawful stream of real transferable economic value**, then choosing the least centralised way to hold and transfer it. The physical commodity is a proposed backing and exchange constraint, not a magic source of dividends.

## Reproducibility and falsification

The full public input set is [three_metal_inputs.json](three_metal_inputs.json). The arithmetic is implemented in [three_metal_envelope.py](three_metal_envelope.py) using Python's standard-library Decimal and focused tests:

```bash
python3 research/three_metal_envelope.py
python3 -m unittest discover -s research -p 'test_*.py' -v
```

Source publication dates, unit conversions, hypothetical prices, and out-of-scope claims remain visible. The model always returns `reserve_or_income_owned_by_ord: false` and `all_metals_legally_accessible_at_synthetic_quote: false`.

A serious rebuttal would show an alternative legitimate funding stream, a stronger legal asset/title structure, different but primary-source documented mine/statistical values, costs or liquidity conditions. These would update the model openly. **Evidence that a metal basket is inferior to independent resource receipts is a successful research result.**

Related: [physical quantity](COMMODITY_SCALE.md) · [market-value financing](VALUE_AND_FUNDING.md) · [custody and title](TITLE_AND_CUSTODY.md) · [issuer-neutral alternative](RFC_0001_RESOURCE_CLAIMS.md).

**No live ORD resource, token, payout, endowment, vault, deposit or guaranteed buying price exists.**
