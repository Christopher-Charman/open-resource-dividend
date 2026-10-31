# Local development and reproducibility

**ORD is research-first.** This page allows a first-time contributor to reproduce the educational results from a fresh public clone with no account, container image, cloud service, API key, package install or paid CI.

## What is required?

- Python **3.10 or later** with the standard library.
- Git only if you wish to clone or submit changes.
- No blockchain node, proof-of-reserves API, market feed, wallet, trading account or real personal data.

```bash
git clone https://github.com/Christopher-Charman/open-resource-dividend.git
cd open-resource-dividend
python3 -m unittest discover -s examples -p 'test_*.py' -v
python3 examples/stock_flow.py
python3 examples/replay_audit.py
python3 examples/funding_scenarios.py
```

The tests check logical properties **inside a synthetic model**, not whether metal exists. The scenario output is deterministic, in abstract metal units (not market prices or forecasts). It is appropriate to run the three model commands separately, not as a service or financial system.

## Quantitative research and dual-book assurance demo

The repository contains an intentionally small independent economic-data calculation and an example of a materially false reserve claim:

```bash
python3 research/scale_envelope.py
python3 -m unittest discover -s research -p 'test_*.py' -v
python3 examples/compare_books.py
```

The [source data](research/scale_inputs.json) comes from dated primary published market and population statistics. The numbers represent a **counterfactual portion of global mine output**, not physical resources available to ORD. The comparator reports **UNVERIFIED_PHYSICAL_AND_LEGAL_BACKING**, even if declared stock covers all claims: it cannot authenticate a warehouse or prove no hidden obligations.

Read [research/README.md](research/README.md) and [research/COMMODITY_SCALE.md](research/COMMODITY_SCALE.md). Never present this simulation as a proof-of-reserves, title certificate, investment valuation or a fixed-income projection.

## Purchasing-power and funding sensitivity

```bash
python3 research/value_funding.py
```

Its [inputs](research/value_funding_inputs.json) are intentionally rounded **hypothetical** funding sums, copper market prices, operating expenses and an endowment-return assumption. The output compares physical copper amounts with estimated world mine production and computes a reverse annual funding requirement for a reference benchmark. There is no committed endowment or price feed. Do not report the US dollar reference as an ORD peg or a promised payment. See [value and funding research](research/VALUE_AND_FUNDING.md).

## Issuer-neutral allocation over already-owned rights

Run the [synthetic externally-issued-claims scenario](examples/scenarios/issuer_neutral.json):

    python3 examples/issuer_neutral_distribution.py
    python3 -m unittest discover -s examples -p 'test_*.py' -v

This tests a **distribution of existing holdings** from two imaginary independent issuers rather than creating an ORD token. The current model has no custody connection, real inventory proof, electronic signatures, legal title evidence or identity verification. Its `delivery_assumed` event is explicitly not an independent physical-delivery confirmation. See [RFC 0002](research/RFC_0002_ISSUER_NEUTRAL_DISTRIBUTION.md).

## Exploring funding assumptions

The editable sample lives at [examples/scenarios/volatile_copper.json](examples/scenarios/volatile_copper.json).

```bash
python3 examples/funding_scenarios.py examples/scenarios/volatile_copper.json
```

The scenario has a single `metal` (Au, Ag or Cu), an `initial_endowment_units`, a `target_per_person_units` and a list of labelled periods. Each period specifies:

- `recipients` — **assumed** unique recipients, not verified identities;
- `contribution_units` — synthetic incoming verified physical metal **assumed** already delivered, funded and contributed to the pool;
- `operating_cost_units` — charges in the *same metal claim units*, paid to an operating counterparty;
- `buffer_units` — a desired minimum pool balance that may restrict the dividend.

At each period, settled contributions increase assumed reserves and claims in equal quantities. Expenses are paid before dividends; unpaid costs become explicit arrears, carried to later periods. If obligations remain unpaid, the toy defers the dividend. Otherwise it pays as many whole units per person as the pool can fund, up to the target. Every period is independently reconciled against the event log.

**Do not interpret this as evidence that a dividend is affordable**. It has no price model, deposits from real mines, taxes, identities, liquidity, insurance or legal rights. It assumes all deposits and deliveries succeed.

## Checking the illustrative history

`examples/replay_audit.py` independently replays the synthetic event log rather than trusting the model's own balances. Run it with its built-in small example, or give it a JSON file containing the exact event-list schema used by `StockFlow.events`:

```bash
python3 examples/replay_audit.py
python3 examples/replay_audit.py --events path/to/synthetic-events.json
```

It detects malformed links, overspending, duplicate synthetic receipt IDs, unfunded distributions and snapshot divergence. A fully malicious history can still be rewritten and rehashed without an independently witnessed checkpoint. This is **not** a consensus mechanism.

## Maintaining the work

- Keep the economic invariants legible. Prefer one small independently explained test for a genuine new failure mode over broad redundant test matrices.
- Check claims against primary sources and record dates. Do not silently promote `proposed` into `implemented` or `verified`.
- Open an issue or PR, connect it to a [research question](OPEN_QUESTIONS.md), and include a reproducible example or counterexample.
- Follow [Governance](GOVERNANCE.md), [Contributing](CONTRIBUTING.md) and [Security](SECURITY.md). Submissions carry no obligation to support the original hypothesis.
- No GitHub Actions or third-party CI is configured. Maintainers may execute the above commands on their own computers; do not assume an external runner is required.

## Files at a glance

| Location | Function |
| --- | --- |
| [START_HERE.md](START_HERE.md) | Two-minute public explanation |
| [WHITEPAPER.md](WHITEPAPER.md) | Economic hypothesis |
| [FUNDING_MODELS.md](FUNDING_MODELS.md) | Sources of physical-claim distributions |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Ownership, custody, audit and ledger trust boundaries |
| [examples/stock_flow.py](examples/stock_flow.py) | Educational account transitions |
| [examples/replay_audit.py](examples/replay_audit.py) | Independent reconstruction of synthetic balances |
| [examples/funding_scenarios.py](examples/funding_scenarios.py) | Multiple periods, variable population, income and costs |
| [examples/test_*.py](examples/) | Focused Python standard-library tests |

[Source code licence: MIT](LICENSE-CODE.md) · [Research text licence: CC BY 4.0](LICENSE.md).
