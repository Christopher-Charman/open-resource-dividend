# ORD open research: reproduce, challenge, correct

The aim of this folder is **falsifiable economic work**, not another coin launch. All calculations are public, intentionally limited and correctable by anyone. A missing financial or legal premise is reported as missing—not replaced with a blockchain narrative.

## Evidence currently available

| Question | Research | Current finding |
| --- | --- | --- |
| How much copper could a worldwide allowance hypothetically distribute? | [Scale envelope](COMMODITY_SCALE.md) · [numeric inputs](scale_inputs.json) · [Python calculation](scale_envelope.py) | Even a hypothetical 1% of 2025 global copper mine output is only ~28.5 grams per person, before losses, fees and legal funding; **0% actually verified as ORD-owned** |
| How can a hash-consistent ledger still be undercollateralised? | [Dual-book demo](../examples/compare_books.py) and [independent replay](../examples/replay_audit.py) | A synthetic ten-unit copper ledger with only eight declared inventory units exposes an arithmetic deficit of two. All physical/legal and completeness attestations remain **UNVERIFIED** |
| What is the gap between digital divisibility and metal delivery? | [Wholesale redemption evidence](REDEMPTION_EVIDENCE.md) | LME/LBMA publish wholesale physical lot/bar standards. These **do not** establish cost-effective small-holder delivery or legal title |
| Does ORD need to issue its own token? | [RFC 0001](RFC_0001_RESOURCE_CLAIMS.md) | Three non-equivalent resource-claims architectures remain in open examination; closed compute credits are a distinct proposal |

## External funding and purchasing-power research

The [value and funding note](VALUE_AND_FUNDING.md) joins an openly specified [price/cost scenario](value_funding_inputs.json) with a standard-library [calculator](value_funding.py). It asks what *real settled external income* would be needed for a modest global physical-resource entitlement, and how much hypothetical metal the model would need to acquire. The calculator never invents a funded trust or treats a USD benchmark as token backing. Bulk price impact, retail delivery and actual capital ownership remain unanswered.

## Legal ownership versus institutional IOUs

The [title and custody comparison](TITLE_AND_CUSTODY.md) uses primary LBMA and LME materials to distinguish allocated bar ownership and transferable warehouse warrants from unallocated contractual promises owed by a clearer. Both can be recorded digitally; the legal rights are not equivalent. It proposes a reviewable assurance package for physical asset title, liens, custody, liabilities, redemption and independent auditing, but establishes no jurisdiction-specific ORD rights.

## Three-metal quantity and reference-value comparison

[THREE_METAL_COMPARISON.md](THREE_METAL_COMPARISON.md) now covers gold, silver and copper in their original intended roles. It separately cites WGC gold mine and aboveground stock data, Silver Institute 2025 silver mine supply, and COCHILCO copper mine flow. Its reproducible [scenario](three_metal_inputs.json) and [standard-library calculator](three_metal_envelope.py) never infer that any of these privately/publicly owned resources belong to ORD. The USD quotations are entirely hypothetical comparison inputs, **not** a basket exchange rate or peg.

## New: issuer-neutral resource dividend candidate

[RFC 0002](RFC_0002_ISSUER_NEUTRAL_DISTRIBUTION.md) develops the hypothesis that ORD **need not issue a new coin**. Instead, an independent fund transfers pre-existing, independently evidenced resource claims. The [synthetic model](../examples/issuer_neutral_distribution.py) keeps issuer, custodian, metal unit and underlying contractual right separate, rejects unfunded dividends and records pending redemption liabilities without falsely treating them as delivered metal. No actual legal rights or issuer balances are verified.

## Existing project assessment and technical donors

- [Verified primary-source ecosystem diligence](EXISTING_PROJECTS_DUE_DILIGENCE.md) reviews real issuer title terms, gold/silver audits and redemption fees, current GoodDollar/Circles source licences, GoodCollective's actual UBI contract and the Windfall Trust.
- [Interoperability contract](INTEROPERABILITY_SPEC.md) specifies what it would take to move legally existing property through an independent distribution pool, without inventing new issuance or treating a token transaction as proof of metal delivery.

The existing synthetic issuer-neutral sample does not connect to any of those providers. All external issuer/source claims remain independently reviewable and no provider is approved for ORD.

## Provider transfer evidence — local executable boundary

[Provider transfer interface findings](TRANSFER_INTERFACE_FINDINGS.md) now link to **official Paxos v2 Create/Get/List Transfer, API access, Sandbox and legal-title terms**, along with Kinesis native transfer and GoodCollective source. The [Python verifier](../examples/provider_transfer_evidence.py) consumes **synthetic** paired Paxos-shaped debit/credit records and rejects inconsistent asset, amount, identity, status or group references. Even completed provider-shaped records **cannot** independently prove a real transfer, legal property, physical reserve or live redemption.

This is a concrete no-credentials interface analysis, not a provider integration or proposed financial deployment.

## How to reproduce

With Python 3.10+ and no dependencies, from a fresh clone:

```bash
python3 research/scale_envelope.py
python3 -m unittest discover -s research -p 'test_*.py' -v
python3 examples/compare_books.py
python3 -m unittest discover -s examples -p 'test_*.py' -v
```

The raw input is `research/scale_inputs.json`. Replace the 2025 copper mine flow or the rounded population with newer **dated primary statistical evidence**, rather than silently changing an assumption. The audit example is **synthetic**; the program cannot verify a commodity vault by reading JSON.

## Checks against confusing evidence types

- **World mine output** is an economic flow, not the project's physical reserve stock or an unallocated resource available to claim.
- **A digital token** is neither title nor a reserve audit.
- **A warehouse standard** is neither a retail delivery commitment nor an investment product.
- **A reserve declaration** can be fraudulent even if a mathematical inequality holds.
- **An append-only hash chain** can be rewritten if no independent witness pins an authentic checkpoint.
- **Universal eligibility** can be proposed without assuming that recurring funds will pay a nonzero guaranteed income.

## How to contribute a substantive correction

Pick one narrow claim in the research, include a primary source (publisher, date, URL), show the relevant scope and a reproducible calculation or legal counterexample, and submit an issue/PR. The [research method](../RESEARCH_METHOD.md), [community governance](../GOVERNANCE.md), and [contributor entry points](../CONTRIBUTING.md) apply.

If a better precedent replaces ORD or makes its present assumptions untenable, document it. The project prioritises public understanding over the original author's thesis.
