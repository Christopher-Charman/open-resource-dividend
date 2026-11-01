# Resource ownership, warehouse rights and independent custody

**ORD legal/market research note · 31 October 2026 · for independent expert review, not legal advice**

## The decisive distinction

A purported "physically backed token" can be **two very different economic assets**:

1. A person's enforceable proprietary interest in identified, segregated physical metal, with a custodian holding it for the owner; or
2. A person's claim against an issuer, clearer or warehouse operator that **owes them metal**, where the person's recovery depends on that institution's legal and financial position.

A public blockchain may record both identically. **The ledger's technical transferability cannot decide which legal right the holder actually owns.** For an open ORD proposal motivated partly by avoiding concentrated monetary discretion, this may matter more than choosing a particular chain.

## Primary market precedents (no ORD affiliation)

| Market mechanism | What official rules describe | Implication for ORD, not an implemented feature |
| --- | --- | --- |
| **LBMA allocated precious-metal account** | The [LBMA clearing guide](https://www.lbma.org.uk/market-standards/clearing) identifies specific bars on a weight list, including serial number, weight and fineness, with the dealer acting as custodian for client-owned bars. The [precious-metals account guide](https://www.lbma.org.uk/publications/the-otc-guide/precious-metal-accounts) distinguishes this from a general unallocated balance. | An ORD receipt would need demonstrable legally protected owner/beneficiary rights, unique reserve inventory and evidence the holder can enforce custody/redemption—not merely a provider assertion that a pool is fully backed. |
| **LBMA unallocated account** | The same [LBMA account guide](https://www.lbma.org.uk/publications/the-otc-guide/precious-metal-accounts) says an unallocated balance is a contractual claim against the clearer, rather than a specific numbered bar. The holder bears clearer credit exposure. Unallocated balances are commonly used because they simplify fractional trading and settlement. | Fractional tradeability does **not** prove insulated physical ownership. An unallocated entitlement may be useful commercially, but ORD must not market a general unsecured obligation as if Frank owned segregated metal. |
| **LME metal warrant** | The [LME warrants description](https://www.lme.com/en/sustainability-and-physical-markets/warehousing/lme-warrants) describes a warrant as entitlement to a particular approved physical lot, using dematerialised warrants in LMEsword for many jurisdictions. [LMEsword](https://www.lme.com/en/trading/systems/lmesword) supports warrant ownership transfer and stock reporting. | Transferable evidence of specified warehouse assets already exists. However, a private ORD fractional token is **not** automatically an LME warrant, LME member account, legal assignment of title or access to an LME warehouse. The warrant transfer structure and full terms would require specialist review. |
| **UK cryptoasset custody guidance** | The [FCA's 2026 cryptoasset regime policies](https://www.fca.org.uk/publications/policy-statements/cryptoasset-regime) discuss safeguarding, ownership rights, record-keeping and reconciliation, while [PERG 18](https://handbook.fca.org.uk/handbook/perg18) addresses differing cryptoasset regulatory scopes. | Regulatory classification depends on actual rights, jurisdictions and activities. Research is not permission to issue or promote a redeemable asset, and open source does not grant custody authorisation. |

These precedents are **not** independent legal opinions about ORD and do not establish a single law that governs a worldwide holder. The description concerns the market rules as currently published, not any contract this repository has executed.

## UK statutory stress test: fractional bulk title is conditional (1 November 2026)

**Primary law, not an ORD legal opinion.** The [Sale of Goods Act 1979, section 20A](https://www.legislation.gov.uk/ukpga/1979/54/section/20A), and [section 20B](https://www.legislation.gov.uk/ukpga/1979/54/section/20B), provide a particularly relevant *conditional* model for fractional interests in an identified bulk of goods. The [Electronic Trade Documents Act 2023](https://www.legislation.gov.uk/ukpga/2023/38/contents) supplies a separate possible route to **possessable electronic trade documents**. Neither statute turns an arbitrary token into enforceable title to gold, silver or copper.

| Primary provision | Narrow legal effect to test | Critical limit for ORD |
| --- | --- | --- |
| [Sale of Goods Act 1979 §20A(1)–(3)](https://www.legislation.gov.uk/ukpga/1979/54/section/20A) | Where a **contract for sale** specifies a quantity of unascertained goods from an **identified bulk** and the buyer has **paid** for some/all of them, the buyer can become an owner in common of an undivided share of that bulk (unless otherwise agreed). | A donated claim, pooled custody receipt, unallocated account balance or freely transferred token **does not automatically satisfy** the sale/payment/identified-bulk conditions. A legal expert must identify the actual transfer and property structure. |
| [Sale of Goods Act 1979 §20A(4)](https://www.legislation.gov.uk/ukpga/1979/54/section/20A) | If the aggregate calculated shares would exceed the bulk, buyers' **undivided property shares are proportionately reduced** to fit the available bulk. | **Co-ownership is not an assurance of 100% backing**: legal allocation of an existing shortfall does not create missing metal. |
| [Sale of Goods Act 1979 §20B(1)–(3)](https://www.legislation.gov.uk/ukpga/1979/54/section/20B) | Co-owners are deemed to consent to specified deliveries/dealings with other co-owners' portions; the statute does not impose a duty on one buyer to compensate another buyer for a shortfall. | A fractionally held lot needs explicit warehouse control, shortfall remedies, and independently verified **total** claims, rather than a promise that every owner can withdraw the original quoted mass. |
| [Electronic Trade Documents Act 2023 §§1–3](https://www.legislation.gov.uk/ukpga/2023/38/contents) | A qualifying trade document, potentially including a **warehouse receipt**, may be possessed electronically when its **reliable system** distinguishes the document from copies, protects integrity, enables demonstrable **exclusive exercise of control**, and **divests** prior control on transfer. It then has the same effect as its paper equivalent. | [Official explanatory notes, paragraphs 21–22](https://www.legislation.gov.uk/ukpga/2023/38/notes/division/6/index.htm) specifically caution that warehouse receipts are **not documents of title at common law**. Electronic possession is **not automatically ownership of the metal**, nor an independent assay or lien check. |
| [Electronic Trade Documents Act 2023 §5](https://www.legislation.gov.uk/ukpga/2023/38/section/5) | The Act permits an **opt-out** of the electronic-possession effects and excludes certain uncertificated securities. | A token labelled 'warehouse receipt' must be tested against the actual contractual terms and statutory scope; merely implementing a transferable data record is insufficient. |

### Reproducible shortage counterexample

Suppose a hypothetical, physically identifiable **100 kg** copper bulk is subject to two **paid sale contracts** for **80 kg** (buyer A) and **50 kg** (buyer B). Assume §20A's conditions apply and the parties have not agreed otherwise. The total promised is **130 kg**, but the identified bulk contains **100 kg**. Applying §20A(4) to the share formula in §20A(3):

```text
A's proportional property share = 100 kg × (80 / 130) = 61.538461... kg
B's proportional property share = 100 kg × (50 / 130) = 38.461538... kg
Total undivided property shares                      = 100 kg
Uncovered quantity promised by the two sale contracts = 30 kg
```

This is a **mathematical illustration of a statutory shortfall rule**, not an assertion that a particular court has adjudicated these facts, that contractual remedies disappear, or that ORD has sold copper. Section 20B(3) does **not** itself make A compensate B for the other's shortage; contractual recourse against a seller or warehouse requires separate examination. An append-only token ledger recording 80 + 50 kg would still record **130 kg of promises against 100 kg of goods**. Proportional reduction of property shares is not proof that the liabilities were covered.

For comparison, if the identified 100 kg bulk had instead been sold as **40 kg + 60 kg** under the same assumed conditions, the arithmetic would fit; that would **still not independently establish** inventory existence, absence of encumbrances, sale validity, current warehouse access, or protection from an operator's insolvency.

### Electronic receipt control is not the same as independent holder control

The [2023 Act's official explanatory notes, paragraphs 38–40](https://www.legislation.gov.uk/ukpga/2023/38/notes/division/6/index.htm), clarify that a system administrator may also have the **ability** to exercise control without automatically disqualifying the document, provided the required exclusive **exercise** of control is maintained. Thus **statutory eligibility does not itself prove ORD's stronger, voluntary holder-control objective**. The [Law Commission's primary reform record](https://lawcom.gov.uk/project/electronic-trade-documents/) also highlights cross-border conflicts of laws. The UK statute cannot simply be presumed to decide rights in a foreign vault or make every holder's token redeemable worldwide.

**Concrete due-diligence questions for one proposed UK-governed arrangement:** Identify the legal seller/transferor, governing law, specific warehouse and bulk/serials, whether §20A applies to each acquisition (or what alternative trust/bailment structure applies), documentary evidence of price/payment if relevant, title and lien searches, all competing co-owners and other claims, the current physical quantity and independent assay, the exact electronic document and its terms/opt-outs, the system's control/divestibility audit, the right to direct warehouse delivery or assign the right to another custodian, insolvency treatment, and actual small-lot delivery charges. **If a recipient is gifted existing claims, explain why legal title follows the gift instead of assuming §20A's sale rules automatically extend to it.**

**Research conclusion:** UK law supplies *possible building blocks*, not a ready-made global, legally insulated ORD asset. Independent physical inspection, complete liability accounting, enforceable individual rights, and affordable non-issuer exit remain separate necessary evidence.

## Holder-centred questions

Consider Frank, who receives a legally funded small metal entitlement and does not use AI:

- **Direct property:** If the issuer becomes insolvent tomorrow, can Frank demonstrate he owns a legally identifiable fraction of a specific bar or lot? Who decides whether the bar can be sold to satisfy the issuer's debts?
- **Control of the exit:** Can Frank transfer legal title to Bob or to a different custodian, not merely move a database balance the original issuer can freeze or revoke?
- **Deliverability:** Is Frank contractually entitled to physical delivery, and at what minimum, fees, timeline, customs treatment and recourse if delivery fails?
- **Visibility of encumbrances:** Could another secured creditor, lender, warehouse, derivative counterparty or third-party token bridge claim the same metal?
- **Authority independence:** If the ledger validates an event but the warehouse refuses to release metal, who resolves ownership and bears the loss? An immutable entry alone cannot compel a physical warehouse.
- **Privacy:** Can an independent auditor verify consolidated liabilities and accepted metal inventory without publicly identifying Frank, Bob or other holders?

These questions must also be answered for holders who cannot meet a wholesale bar delivery size, cannot afford recurring custody fees, or live outside a particular market's membership jurisdictions. Open participation is not proved if the exit exists only for institutions.

## Preliminary assurance evidence package — *proposed*, not implemented

A future commodity claim's public record would need at least:

1. **Asset scope:** metal (Au, Ag, Cu), physical mass and purity/grade, location and warehouse, unique lot/bar reference, expected custody and delivery conditions.
2. **Legally enforceable claim basis:** governing law, named title holder/beneficial interest structure, segregation/trust/bailment rights as applicable, insolvency priority and enforceable redemption or assignment mechanism, independently reviewed.
3. **Physical and legal status:** dated independent inventory/assay evidence; actual chain of title; lien and rehypothecation checks; identified audit scope and genuine auditor independence.
4. **Liability scope:** all outstanding direct/indirect claims, derivative pledges, wraps/bridges, off-ledger obligations and any overlapping beneficial owners. A proof-of-reserves unsupported by proof of liabilities is insufficient.
5. **State transitions:** deposit acceptance, mint, owner change, escrow or cancellation when redemption starts, eventual physical delivery, failed delivery and enforceable compensation or return to available state. A "burn" does not itself prove an item was delivered.
6. **External review:** independent parties must be able to inspect the public economic claims and recreate cryptographic checks, while protected identity and sensitive warehouse data are disclosed only to duly authorised auditors and rights holders.
7. **Exit reality:** tested transfers between independent counterparties, redemption rights, non-exclusive custodians where practicable, and explicit costs and minimums. Practical economic exit is distinct from a contractual right that a small holder could not afford to exercise.

**No attestation should be labelled "independently verified" merely because its author uploaded a signed file to a public ledger**. A hash is evidence of document integrity, not of truth, legal enforceability or auditor independence.

## Proposed legal research comparisons (no result assumed)

| Design | Legal challenge most worth testing |
| --- | --- |
| Specific fully allocated individual metal | How would billions of small legal fractional title transfers work without prohibitive bar/lot handling costs? |
| Fractional co-ownership of segregated metal lots | Does the governing jurisdiction enforce the holder's fractional beneficial interest against a failing custodian, and how is a partial delivery discharged? |
| Multiple regulated/approved independent receipt issuers | Are claims of different issuers fungible enough for open exchange despite different legal risks and redemption fees? |
| Physically collateralised general debt claim | Is it candidly a counterparty-credit instrument rather than direct metal ownership? If so, does it satisfy ORD's original independence objective? |
| Issuer-neutral distribution of pre-existing audited assets | Can recipients verify rights and transfer independently without ORD being another issuer, custodian or mandatory market maker? |

## Research acceptance, not a deployment checklist

A defensible next milestone is a **jurisdiction-specific legal and operational opinion** for *one* concrete asset/custody structure, publicly scoped with conflicting views preserved. It should identify who owns the bar, who can direct delivery, what happens on insolvency, and the admissible evidence. Then evaluate scale, cross-border holders, licensing and fees. Any actual financial instrument would need separate legal/regulatory approval and real independently verified reserves.

Until then, the precise statement is: **ORD is an open research hypothesis about distribution of enforceable commodity ownership**, not a metal-backed currency that presently exists.

Related: [resource claim RFC](RFC_0001_RESOURCE_CLAIMS.md) · [physical redemption](REDEMPTION_EVIDENCE.md) · [economic funding](VALUE_AND_FUNDING.md) · [assurance model](../ARCHITECTURE.md).
