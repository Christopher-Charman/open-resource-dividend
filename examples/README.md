# Illustrative stock-flow model

This folder contains **non-financial, standard-library-only Python examples** of a resource-entitlement system. It is not a blockchain, smart contract, wallet, custodian, oracle, proof-of-reserves implementation or fundraising system.

## Run locally

```bash
python3 examples/stock_flow.py
python3 -m unittest discover -s examples -p 'test_*.py' -v
python3 examples/replay_audit.py
python3 examples/funding_scenarios.py
```

Ten focused tests cover the initial model, independent journal replay and a multi-period funding scenario. The source is dependency-free; no hosted CI is configured. Run the commands above on your own computer.

## The worked example

A hypothetical donor holds 1,000 units of copper in an assumed verified warehouse deposit. The simulation issues corresponding claims to the donor, transfers those existing claims to a distribution pool, and allocates **9 units each to 100 people** while retaining 100 units. Frank transfers 3 of his units to Bob, Bob pays a compute provider 5 units, and Frank redeems 2 units for **assumed** delivered copper.

After the redemption, the toy state has **998 reserve units and 998 outstanding claim units**. The distribution did **not** increase issuance; the eventual redemption reduced both outstanding claims and the assumed physical reserve by 2.

The model uses **separate** accounting units for Au, Ag and Cu. It never assumes 1 unit of gold can be replaced by 1 unit of copper on the basis of market price alone. Metal classes are not fungible unless contractual rights explicitly make them so.

## Independently reconstructing a synthetic history

The [replay auditor](replay_audit.py) recomputes the entire synthetic state from canonical event entries and compares it against any supplied snapshot. It rejects changes to unanchored hashes, overspends and unfunded distributions—but it cannot prove that claimed physical metal exists, nor can it detect a perfectly rehashed alternate history without independent external witnesses.

The [funding simulator](funding_scenarios.py) uses the editable [volatile copper example](scenarios/volatile_copper.json). Over four periods, the scenario's **assumed** contributions total 2,100 copper units; 1,890 are distributed, 40 pay operating costs and 170 remain in the pool. Payment falls below its 9-unit target during contribution and population stress. This is a deterministic accounting example, **not** a real-world income or market forecast.

For detailed commands and variable definitions, consult [DEVELOPMENT.md](../DEVELOPMENT.md).

## Compare the two books, not just the hash chain

Run `python3 examples/compare_books.py`: a synthetic ten-unit copper transaction log passes internal arithmetic, yet a separately **declared** inventory of eight units produces a two-unit deficit. This reveals an important missing assurance beyond event replay. Even a balanced declaration is **not an independent physical audit**.

For the independently calculated economic scale envelope, see [research/README.md](../research/README.md). The accounting demonstrations cannot establish real inventory, legal ownership, delivery rights, external witnesses or completeness of all liabilities.

## No new issuer: two external claim types

The [issuer-neutral reference](issuer_neutral_distribution.py) reads the [Frank/Bob JSON scenario](scenarios/issuer_neutral.json). Separate fictional copper and gold receipt issuers contribute pre-existing claims to one funded pool; transfers, allowances, requests and cancellation remain separated by external asset ID. The code has **no ORD minting operation** and prevents an asset class or unowned claim from being silently substituted. It also models a pending physical redemption as an outstanding obligation, not an immediate token burn.

This is an **unsigned accounting experiment**. Balancing declared claims against declared inventory is not an independent reserve audit, and the example does not verify recipient identities or real owner consent. More details: [RFC 0002](../research/RFC_0002_ISSUER_NEUTRAL_DISTRIBUTION.md).

## Limitations that must not be confused with guarantees

- `deposit_assumed_verified` assumes custody, legal title, purity and no competing liens; it **does not** verify them.
- `redeem_assumed_delivered` assumes physical delivery is completed as part of a simplified single-step model. Real custody release and delivery are asynchronous and require escrow, disputes and failure handling.
- The sample accounts are synthetic labels, not real persons or privacy-preserving identity credentials.
- Hash-linked events are tamper-*evident* only to a verifier holding an independent checkpoint; the toy has no consensus, external witness or enforced append-only storage.
- There is no identity-uniqueness, fee, market-price, insurance, custody-failure, issuer-insolvency or perpetual funding model.
- The model proves at most the arithmetic of **its own assumptions**, not economic feasibility.

For the funding argument, consult [FUNDING_MODELS.md](../FUNDING_MODELS.md). For hard unresolved issues, see [OPEN_QUESTIONS.md](../OPEN_QUESTIONS.md).

Example source code is under the [MIT License](../LICENSE-CODE.md); research text is covered separately by [CC BY 4.0](../LICENSE.md).
