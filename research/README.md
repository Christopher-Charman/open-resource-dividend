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
