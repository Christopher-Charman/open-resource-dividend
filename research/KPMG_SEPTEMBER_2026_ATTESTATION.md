# September 2026 PAXG: original KPMG report, network liabilities and exact cutoff

**Primary source read and hashed 31 October 2026 · External research, not an ORD audit or admission of a backed asset.**

## What actually changed

The [first live chain observation](LIVE_PAXG_CHAIN_EVIDENCE.md) established PAXG's Ethereum token supply at an **October 31** finalized block. A reserve comparison needs the **September 30** cutoff of the most recently published independent accountant's report, and **every included chain**, not October's Ethereum count. This report records those exact source facts and a narrow auditable reconciliation.

The original [issuer-hosted independent accountants' examination report (PDF)](https://framerusercontent.com/assets/uwWybrLRlgkC4vexP3yLyrQVeV0.pdf) was downloaded directly from the source linked by [Paxos's transparency portal](https://www.paxos.com/paxg-transparency). Its **490,005 bytes**, **8 pages** and SHA-256 `2611a159b29fc28dd4f438528c5aa38330002e4848e20cbdd8b02ec2864f87a1` were recorded; the full third-party document is **not republished** in ORD.

The report is signed **October 23, 2026** by **KPMG LLP** and examines Paxos Trust Company, National Association **management's assertion as of September 30, 2026, 5:00pm Eastern (21:00 UTC)**. KPMG says management's assertion on the token quantities, reserve composition and comparison is fairly stated in all material respects. Its opinion does **not** extend to separately linked information on Paxos's website. The evidence has a dated scope rather than an ongoing guarantee.

## Precise original Exhibit A: four different token networks

| Network | Original report PAXG redeemable tokens, in reported whole-token units | Official token identifier reported in the PDF |
| --- | ---: | --- |
| Ethereum | **432,506** | `0x45804880De22913dAFE09f4980848ECE6EcbAf78` |
| Solana | **2,560** | `5GgRAEmv8ZxF2PR5hY72Qs5x1bnQ6UK2RbTPoqJ3wSwW` |
| Robinhood Chain | **5** | `0x121BbE58fe4684057FB66d2dd535A19e16B4f66F` |
| Base | **235** | `0xe904AEA5E1b110c9174728fA2efFc8aeD19E98Ef` |
| **All networks** | **435,306** | Report Exhibit A, p. 5 |

**Exhibit B**, p. 6: **435,306 fine troy ounces** of London Good Delivery gold supporting the reported liabilities. Paxos reports sourcing metal from **StoneX Group Inc.** and custody at **Brink's Global Services Ltd.** and **ICBC Standard Bank**. **Exhibit C**, p. 7: **zero reported surplus or deficit**, no listed timing differences, and no temporary/permanent nonredeemable PAXG tokens.

**Checkable arithmetic:** `432,506 + 2,560 + 5 + 235 = 435,306` and `435,306 - 435,306 = 0`. The exact checks are implemented in [attestation_cutoff_reconciler.py](attestation_cutoff_reconciler.py), with the [machine-readable source observations](observations/paxg_kpmg_2026_09_30.json) and three focused adversarial tests. No fiat-dollar peg, investment return, new token or ORD funding is inferred from these mass units.

**Important precision boundary:** the PDF shows integer token counts without fully specifying the relationship to decimal ERC-20 units at the cutoff. Comparing a fraction-rich smart-contract supply to a rounded table as exact decimals without a documented presentation policy would overstate the evidence. This research does not silently choose a rounding method.

## The correct Ethereum cutoff block was independently located

At **21:00:00 UTC**, the last Ethereum block strictly before this timestamp was block **26,092,843**, dated **20:59:59 UTC**, hash:

`0x8188886a9f46bc06f64a47ae89a8464328ca388130addd91d9d78cb97838dfd3`

The following block, **26,092,844**, was dated **21:00:11 UTC**, hash:

`0x33898bb860ae3e8aaedb6157e3e9f6172aa4931887b2fef707f2fa735cb9e1a3`

Both independent public RPC providers, PublicNode and Nodely, returned identical block numbers, timestamps and hashes. This **brackets the precise reporting cutoff**, solving the temporal alignment problem for Ethereum.

**But the nodes did not provide historic PAXG contract state** at that older block via available unauthenticated `eth_call` access (not all providers retain old contract state). We therefore **did not independently verify the Ethereum 432,506 PAXG figure** at the examination instant. Nor have we independently queried the Solana, Robinhood Chain or Base token supply at their corresponding cutoff.

A third-party analyst's [October 31 comparison](https://altstreet.investments/platforms/reviews/paxos) reports having read the Ethereum supply at the exact September 30 cutoff, but **we do not promote that analyst's result to a primary independently read-back ORD observation**. Independent replication with an authorised archival state interface is still required.

## The boundaries of KPMG's assurance versus ORD's aspirations

1. **Accountant opinion:** independent professional examination of a defined *management assertion*, at one instant, using stated criteria. It is not an ORD-conducted physical audit or a guarantee of continuous future solvency.
2. **Asset existence and custody:** Exhibit B identifies the reported gold quantity, supplier and vault operators, but ORD has not physically observed the bars, checked legal liens, seen the entire bar list or demonstrated custody on behalf of any specific future recipient.
3. **Liabilities:** Exhibit A includes PAXG outstanding on all four identified networks. It is not automatically an opinion on every non-PAXG debt, pledged right or hypothetical outside wrapper; the scope is the listed PAXG redeemable tokens.
4. **Legal rights:** the report says all PAXG tokens are redeemable under its AICPA reporting definition. It also explicitly refers to separate issuer terms defining **who** can redeem directly. This does **not** mean every anonymous holder can demand immediate delivery of a small bar without KYC, minimums and fees.
5. **Rounding and timing:** a current Ethereum token count, an older four-network report, and a gold vault ledger cannot be equated as synchronous quantities.
6. **Funding:** a fully backed existing gold instrument does not imply the owner of ORD possesses assets to fund a single universal allocation.

## Reproduce the arithmetic and independently verify the original PDF file

```bash
# Pure standard library, local manifest, no network or wallet:
python3 research/attestation_cutoff_reconciler.py

# Optionally download original PDF YOURSELF from the direct issuer link
# and require exact source size + SHA-256; does not copy it into the repo:
python3 research/attestation_cutoff_reconciler.py --source-pdf /path/to/issuer.pdf

python3 -m unittest discover -s research -p 'test_*.py' -v
```

The program deliberately outputs `PUBLISHED_REPORT_ARITHMETIC_ONLY_CHAIN_SUPPLY_UNRECONCILED` even when the four report figures add up and the PDF hash matches. A matched PDF hash proves these are the **same document bytes** already seen, not a cryptographic signature from KPMG, physical title or a legal claim.

### Next independent, genuinely higher-value external work

- Obtain **two independently operated historical/archival Ethereum state providers** that return PAXG `totalSupply()` and `decimals()` at **block 26,092,843**; independently record and timestamp both, and explicitly handle report whole-unit precision.
- Independently examine the three other **official report-listed networks** at their appropriate UTC cutoffs. Avoid double counting wrapped tokens that are actually liabilities of a different issuer, custodian or legal claim.
- Validate KPMG's *engagement criteria* and whether any separately published **physical on-site inspection** is available for the same period; distinguish on-site assay, legal title, liens and warranties.
- Investigate genuine small-holder transfer and direct delivery rights. If these fail, an issuer-neutral universal fund cannot simply adopt PAXG as the answer.

**Current defensible conclusion:** We have **original report evidence** of an independently examined management assertion of **435,306 PAXG redeemable tokens and 435,306 fine troy ounces as of 30 September**. We have independently corroborated the Ethereum block *time* at that cutoff. We do **not** yet have an independently verified **four-network on-chain historical-supply reconciliation**, let alone individual property and delivery verification.

Source preservation and reproduction are central to a philanthropic project. If later evidence contradicts this report or a protocol's economics, that negative result should be documented rather than hidden.
