# Open evidence and reproducibility method

**Purpose:** A common quality standard that does not require any founder, institution, AI vendor, or custodian to be trusted merely on assertion.

## Statement labels

Every consequential claim in ORD should be distinguishable as:

| Label | Required basis |
| --- | --- |
| **Observed** | A dated primary source, readable documented event, or independently inspected result with a reproducible location |
| **Calculated** | Steps, units, inputs and reproducible operations stated; scenarios must identify synthetic assumptions |
| **Inferred** | What reasoning follows from observations, including alternative interpretations and limits |
| **Proposed** | A possible design, explicitly not evidence of implementation or legal feasibility |
| **Unverified** | A material premise without direct evidence, or a result for which independent review is absent |
| **Falsified** | A hypothesis contradicted by reproducible counterexample or reliable evidence; keep correction history |

Do not treat a project's promotional documentation as independent physical audit, financial solvency confirmation, or source of legal authority. Cite primary materials and distinguish issuer claims from independent evidence.

## Evidence entry

For every major cited economic, scientific or technical claim:

1. State the narrow claim and whether it concerns an existing system, historical precedent, projected future or proposed ORD mechanism.
2. Give a canonical URL, publisher, title and **publication or access date**. Prefer official statutes, first-party technical specifications and peer-reviewed research; include independent confirmation for factual audit claims.
3. State the relevant scope: metal, legal jurisdiction, date, population, counterparty, custody terms and what the source did **not** establish.
4. For a numerical claim, publish units and assumptions; for a calculation, allow an independent person to recompute the result from public input.
5. Publish material revisions with explicit attribution, reason for change and a permanent GitHub discussion/PR link.

**Avoid novelty overclaims.** A search that found no identical system is not proof that no one has proposed it. Closer prior art should update [PRIOR_ART.md](PRIOR_ART.md).

## Boundaries on money and software

- A program that balances synthetic claims validates arithmetic conditional on assumptions, not real-world reserve existence.
- Hash-linked, append-only logs can be internally checked but may be rewritten from scratch without external independent anchors.
- Metal standards (weight, purity, custody) do not themselves guarantee ownership or priority over competing claimants.
- Resource-backed value is not necessarily price-stable, liquid or equivalent to a basic income.
- Public research is distinct from an authorised offering, redemption obligation, banking, investment or cryptoasset service.

## Constructive counterexamples

A strong review identifies exactly which claim fails, the smallest scenario that demonstrates the failure, the affected assumption, and the minimum evidence that could resolve it. A correction that makes ORD less plausible is still successful research. Research output must never depend on agreement with the founder.

## Review and maintenance

Open-source review is public by default except genuinely sensitive reports. Small low-risk corrections need no ceremonial meeting. Material economic claims should reference the corresponding issue or discussion. Keep contributor guidance readable and avoid unnecessary dashboards, repeated automated tests, dependent services or competing sources of truth.
