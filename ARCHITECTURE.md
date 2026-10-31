# ORD research architecture and assurance boundaries

**Status:** design exploration v0.1 · **no live protocol, collateral, issuer, entitlement or custody**. The example code is a synthetic accounting classroom, not a proposed production deployment.

## 1. Separate problems that must not be collapsed

| Layer | What it would claim | Required evidence | What a ledger cannot establish |
| --- | --- | --- | --- |
| Physical inventory | Specific mass, grade, location and uniqueness of material | Independent assaying, custody inventory, warehouse lot/bar references | A vault really contains any metal |
| Legal ownership | A holder has an enforceable delivery/ownership right, free of other liens | Title documents, warehouse agreements, jurisdictional legal analysis, encumbrance searches | That a token holder outranks a creditor |
| Issuance and liabilities | Outstanding claims do not exceed legally deliverable collateral | Independent complete liability reconciliation across all issuers/bridges and matched reserves | Liabilities that an issuer deliberately hides |
| Claims history | Issuance, transfer, cancellation and correction events are internally coherent | Independent replay, publicly witnessed commitments, finality and governance rules | Truth of false original records or unanchored rewritten histories |
| Universal distribution | A distribution was paid from an existing legally funded asset pool | Pool pre-/post-balances, contribution provenance, eligibility checks, cost commitments | Existence of sustainable future income or unique human identities |
| Open exchange | Owners can willingly exchange for goods, metals and compute | Tested redemption/market access across independent providers | Liquidity, absence of monopoly or guaranteed competitive prices |
| Privacy and safety | People can participate without compulsory public exposure | Threat modelling, legal privacy review, third-party security review | That pseudonymous wallet addresses are inherently private |

**Physical verification must be independent of the token issuer**: a signed assertion from the issuer, even if immutable and hashed, is not independent material evidence.

## 2. Two distinct accounting boundaries

For each physical asset class (Au, Ag, Cu) independently:

```text
0 <= total_issued_claims_m <= audited_unencumbered_deliverable_reserves_m
0 <= pool_held_claims_m <= total_issued_claims_m
0 <= a_period_distribution_m <= pool_held_claims_m - valid_locked_commitments_m
```

All quantities must use the same specified physical unit, purity/grade and delivery entitlement. Claims on two different jurisdictions or warehouses may not be interchangeable merely because their quoted commodity prices match. Claim equivalence must include enforceable legal rights, fees, delivery rights and counterparty insolvency risk.

**Backing can be necessary without being a dividend source.** If a depositor brings 1kg of copper and receives a corresponding token, the backing and claim both grow; this deposit alone does *not* transfer wealth to everyone. The dividend pool must separately receive **legal ownership** of those claims, funded by gifts, endowment income, actual physical deliveries or a justified economic arrangement. The pool distributing existing claims does not expand total issuance.

## 3. Append-only ledger: illustrative event grammar

The educational `examples/stock_flow.py` model emits four **synthetic** event types:

| Event | Inputs | Deterministic state consequence |
| --- | --- | --- |
| `assumed_deposit` | owner, metal, positive quantity, unique evidence ID | + reserve and + owner claim, **assuming** legal title/custody already accepted |
| `transfer` | source, target, metal, positive quantity | claim owner changes without changing total issued or reserve |
| `funded_distribution` | pool, unique recipient labels, per-person quantity, total, buffer | transfer only existing pool claims, respecting a chosen retained buffer |
| `assumed_delivered_redemption` | owner, metal, positive quantity, unique delivery ID | - owner claim and - assumed reserve after **assuming** physical delivery |

The model records `sequence`, `previous`, `kind`, `metal`, `details`, `digest` where digest is SHA-256 of canonical UTF-8 JSON of the preceding fields (sorted keys, compact separators). This is **an educational schema only**; it does not specify sufficient identifiers, signatures, external anchors, lot references, dispute processes, finality or privacy for a production protocol.

The independent `examples/replay_audit.py` reads the complete event log and reconstructs liabilities and ownership from zero, enforcing each economic transition and checking internal hashes. It does not read an issuer-supplied balance as truth. Reconciliation then compares the reconstructed state with any supplied snapshot.

**Critical limit:** without independently published, signed checkpoints or independently trusted copies, someone with full write access can replace an entire history and recompute every hash. External witnessing, validated proofs and consensus are **open design questions**, not features of the toy code.

## 4. Critical failure scenarios

| Threat | Required later acceptance evidence |
| --- | --- |
| Custodian double-pledges or substitutes a metal lot | Independently checked unique lot references, legal lien status, title audit and custody cross-check |
| Issuer hides wrapped or off-ledger liabilities | Consolidated proof of all redeemable obligations, independent liability auditing and no double counting |
| Deposit is forged or title defective | Third-party physical inspection and legal ownership evidence **before** minting |
| Redemption burns a claim but delivery fails | Explicit interim obligation, escrow, cancellation/compensation, dispute and loss allocation with auditable status |
| Individual is counted twice for a dividend | Privacy-preserving eligibility, accountable exclusions/appeals and credible anti-Sybil testing |
| Validator committee or auditors captured | Independently verifiable evidence, role rotation, conflicts disclosure, open dispute mechanisms and contingencies |
| Repository maintainer disappears | Reproducible clone and local tools, permissive project licences, documented governance and successor community—not a private API |
| Someone presents research as an investment product | Clear non-operational scope, no token/wallet/deposit addresses, active correction of misleading claims |

## 5. What is explicitly outside the current repository

No asset-custody API, financial contract, smart contract mainnet, KYC identity database, trading venue, price oracle, investment solicitation, actual proof-of-reserves or claim of authorisation. The non-financial example's source code must **never** be deployed as a ledger controlling real assets.

A future production project would require separate legal, audit, security and community decisions, and a complete formal definition of physical asset rights. Nothing in the v0.1 paper or research tests grants that decision.

## 6. Domain and source references

- [Funding note](FUNDING_MODELS.md) — pool/issuance distinction and candidate sources.
- [Simulated example](examples/README.md) — reproducibility and limitations.
- [Open research questions](OPEN_QUESTIONS.md) and [community governance](GOVERNANCE.md).
- LBMA Good Delivery: https://www.lbma.org.uk/good-delivery/good-delivery-rules-and-governance — a practical example of how strict specifications and vault acceptance matter to gold/silver; it is **not** an ORD endorsement or a universal standard for copper.
- UK FCA cryptoasset regime policy statements, 30 June 2026: https://www.fca.org.uk/publications/policy-statements/cryptoasset-regime — regulatory treatment changes over time; specialised independent advice would be needed before anyone offered a token or custody service.

**Research challenge:** propose evidence that can bridge each boundary, or show why the combined design is infeasible. Not knowing is an acceptable research result.
