# Physical scarcity and universal distribution: a numerical reality check

**ORD research note · 31 October 2026 · Version 0.1 · This is NOT a valuation, funding offer, resource audit or forecast.**

## Executive result

The challenge is not creating an on-chain representation of copper; it is obtaining legally owned, deliverable copper **for everyone**. In a deliberately optimistic, hypothetical calculation, **1% of all 2025 world copper mine production** divided among approximately 8.3 billion people equals **28.512 grams of copper content per person per year**, *before* refining, title acquisition, custody, insurance, auditing, delivery, liquidity and operating costs. **That 1% is not available to ORD. It is property belonging to somebody else until legally transferred.**

This means a commodity claim can be fully backed and tradeable while a meaningful recurring universal dividend remains economically unproven. Neither a token nor an immutable ledger solves that distribution problem. This is an *important constraint on the proposed mechanism*, not a reason to restrict Frank or Bob's voluntary exchange.

## 1. Inputs and their scope

| Input | Value | Source and qualification |
| --- | ---: | --- |
| 2025 global copper **mine production**, copper content | **23,665,300 metric tonnes** | Chilean Copper Commission (COCHILCO), August 2026 monthly statistical bulletin, World Total for 2025: 23,665.3 *thousand* metric tonnes. Mine output, **not** accepted, unencumbered refined copper in a warehouse. [Source](https://boletin.cochilco.cl/productos/boletin.asp?anio=2026&mes=08&tabla=tabla34). Other methods/updates may yield somewhat different totals; the independent USGS 2026 summary rounds its 2025 estimate to ~23 million tonnes. |
| Illustrative 2026 world population | **8.3 billion** | Rounded model assumption informed by UN [World Population Prospects 2024](https://population.un.org/wpp). Not a precise 2026 census and not an independently verified set of eligible recipients. |
| Wholesale LME Grade A copper physical lot | **25 metric tonnes** | [LME copper contract specification](https://www.lme.com/Metals/Non-ferrous/LME-Copper/Contract-specifications): Grade A cathode, approved brands, 25-tonne warrant with ±2% delivery tolerance. **This is not an ORD retail redemption rule.** |
| LBMA London Good Delivery gold bar | **350–430 fine troy ounces** | [LBMA technical specifications](https://www.lbma.org.uk/publications/good-delivery-rules/technical-specifications). A wholesale standard, not the only way to hold or deliver small gold. |
| LBMA newly produced silver Good Delivery bar | **1,000 troy ounces ±10%** | [LBMA technical specifications](https://www.lbma.org.uk/publications/good-delivery-rules/technical-specifications), revised effective 2025; older bars have transitional allowances. Again, not a universal retail delivery minimum. |

All sources are linked publicly; none provides evidence that the owner of ORD holds or controls any of the listed metal. The project has no reserve.

## 2. Transparent thought experiment

Let `Q` be 2025 global copper mine production (tonnes), `f` the **hypothetical** share voluntarily and legitimately contributed to a fund, `N` the illustrative global headcount, and `q` the grams per recipient.

```text
q = (Q * f * 1,000,000 grams/tonne) / N
Q = 23,665,300 tonnes of mined copper content in 2025
N = 8,300,000,000 assumed people
```

For this initial *upper envelope*, assume **100% of that hypothetical contributed copper content is usable without any loss or expense**. Real conversion, procurement and costs lower attainable allocations. Further, mere 2025 production **does not** mean any of it is donated, held in custody, or unencumbered.

| Counterfactual donated fraction of annual mine output | Hypothetical annual copper-content tonnes | Grams per person per year, before costs |
| ---: | ---: | ---: |
| **0.1%** | 23,665.3 | **2.851** |
| **1%** | 236,653 | **28.512** |
| **10%** | 2,366,530 | **285.124** |
| **100%** | 23,665,300 | **2,851.241** |

**Inverse problem:** At this assumed population, a fund promising **10 g copper/person/year** would need 83,000 tonnes/year (0.3507% of the cited 2025 world mine output), **100 g** would need 830,000 tonnes/year (3.5072%), and **1 kg** would need 8.3 million tonnes/year (35.0724%)—in each case before any real-world loss, with legal funding still wholly absent.

These numbers **do not value copper**, establish purchasing power, infer UBI sufficiency, or mean that fractional physical delivery is feasible. Scarcity can support tradability without establishing the monetary utility of each recipient's claim.

The [inputs](scale_inputs.json), [calculation source](scale_envelope.py) and [two focused numerical checks](test_scale_envelope.py) use Python's standard library and `Decimal`, without price feeds, blockchains, private data or third-party services. Run `python3 research/scale_envelope.py` from the repository root. The output exposes `actual_available_to_ord_tonnes: null` rather than quietly inventing a reserve.

## 3. Fractional ownership versus wholesale redemption

At 1% hypothetical contribution, `236,653 tonnes / 25 tonnes` corresponds arithmetically to about **9,466 wholesale Grade A copper lot-equivalents**, although raw mine output does **not** meet LME warrant acceptance. A `28.5 g` digital claim can be transferred, but that does **not** give a small holder a cost-effective right to drive to a wholesale LME warehouse and collect 28.5 grams.

Three distinct meanings of redemption must not be confused:

1. **Individual physical delivery:** specific small metal quantity is delivered to a retail holder, subject to manufacturing/handling/storage/shipping costs and clear legal title. Not currently demonstrated for ORD.
2. **Pooled delivery with splitting/aggregation:** many holders voluntarily aggregate claims into a deliverable lot, with clear ownership and rights over splitting, custody, delivery, loss, insolvency and fees. An intermediary can recreate concentration risk unless independent exits are credible.
3. **Trading a claim for other assets:** the holder sells a legitimate claim to someone else, who may be able to meet larger delivery minima. This supports market exchange, but a market sale alone is **not equivalent to guaranteed physical redemption**.

Wholesale precedents are useful to expose real friction, **not** to assert that ORD must impose those exact lot sizes. Alternatives, including smaller retail bullion bars and contractual fractional title, need their own empirical legal/cost analysis.

## 4. The funding models that remain admissible

A ledger that creates an automatic per-person allocation every month without receiving property is not commodity-backed solely by its code. The following remain economically distinct candidate sources:

- **Funded one-off allocation:** donors transfer existing, already backed claims. Simple to account for; not a continuing revenue source.
- **Independent funded endowment:** owners voluntarily commit productive assets or revenue; the fund *actually buys* existing backed claims or receives verified physical metal, then distributes only what's available after expenses and obligations. Actual net returns can be negative.
- **Contractual metal deliveries:** a royalty, stream or mining agreement produces a resource claim **only after** custody/title evidence is accepted. Expected ore in the ground is not an already-deliverable reserve.
- **Existing public resource-dividend regimes:** a public body may own resource royalties, but its economic/legislative authority is specific to its jurisdiction. ORD does not imply confiscation or automatic ownership of global minerals.

**Universal eligibility is not universal payout capacity.** A fair, open formula may produce zero in an underfunded period; the paper must disclose that result. Source funding and market prices are separate variables. Donors, miners and current metal owners retain their existing rights unless they voluntarily enter an enforceable arrangement.

## 5. Falsifiers and questions for outside experts

1. Can any credible, legally owned resource income finance a *meaningful* recurring global dividend after audit, insurance, conversion, logistics, administration, and inclusion costs? Show sources, assumptions and failure probabilities.
2. Could actual rights of fractional title survive a custodian's bankruptcy or competing secured creditor claims in relevant jurisdictions? Legal expert review required.
3. Are independent custody/issuance/audit markets competitive enough to prevent a replacement monopoly? Evidence, not promises, is needed.
4. Can small-holder physical redemption become economically practical across geographic and legal barriers, or does it effectively become an ordinary price-tracking token?
5. Is a *per-metal claims architecture* more honest than one "backed universal currency" that silently changes gold, silver and copper weights?
6. Would a fundamentally different source of AI-economy dividends (resource rent, shared infrastructure ownership, independent trust) preserve voluntary exchange more effectively than a direct commodity-backed UBI?

### Research distinction

This note establishes a **mass-flow upper envelope under chosen assumptions**. It does not establish real reserve ownership, universal eligibility, a physical delivery implementation, a new monetary standard, socially meaningful distributions, or a forecast. Negative results are welcome; they tell the project what **not** to build.

Related: [FUNDING_MODELS.md](../FUNDING_MODELS.md) · [ARCHITECTURE.md](../ARCHITECTURE.md) · [WHITEPAPER.md](../WHITEPAPER.md).

**Status at publication:** computationally reproducible for synthetic data; factual numbers are third-party statistical estimates/wholesale standards, not issuer-backed collateral evidence.
