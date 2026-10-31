# Open Resource Dividend (ORD)

**Open research proposal: an independently verifiable, physically redeemable universal entitlement for an AI-transformed economy.**

**New here? [Start with the two-minute overview](START_HERE.md) or [critical FAQ](FAQ.md).**

**Stable public reference:** [ORD Research v0.4 — Issuer-neutral distribution](https://github.com/Christopher-Charman/open-resource-dividend/releases/tag/v0.4.0) (includes the earlier [v0.2 economic baseline](https://github.com/Christopher-Charman/open-resource-dividend/releases/tag/v0.2.0)). All releases are **research snapshots, not currency launches**. This is an open research project intended for community maintenance, with [transparent governance](GOVERNANCE.md) and a [founder-independent contribution plan](COMMUNITY_HANDOFF.md). The original proposer remains the GitHub repository owner.

[White paper](WHITEPAPER.md) · [Funding feasibility](FUNDING_MODELS.md) · [Architecture and assurance](ARCHITECTURE.md) · [Reproduce the examples](DEVELOPMENT.md) · [Prior art](PRIOR_ART.md) · [Roadmap](ROADMAP.md) · [Contribute](CONTRIBUTING.md) · [Community discussion](https://github.com/Christopher-Charman/open-resource-dividend/discussions/5)

> **Research only · v0.1 · 31 October 2026.** No tokens exist, no physical reserves are held, no redemption or universal allowance is funded, and no economic or legal feasibility has been demonstrated. Nothing here constitutes an investment offering or recommendation.

## One-sentence idea

As AI increases the economic significance of compute, a person should be able to participate in the resulting economy **without needing to use AI or trust an AI provider**: distribute already-funded, independently auditable claims on scarce physical resources, and permit holders to exchange them freely for whatever they value.

## Why *open* matters

The hypothesis deliberately separates five things:

- **Backing:** specifically defined claims on verified, unencumbered gold, silver or copper—not merely tokens tracking their prices.
- **Entitlement:** a periodic universal dividend funded by *existing* resources or genuine income, never discretionary unbacked minting.
- **Accounting:** a public, append-only, independently verifiable history of issuance, transfer, redemption and corrections.
- **Redemption:** an enforceable path to obtain the underlying materials, with clear custody and delivery obligations.
- **Exchange:** open markets for materials, goods, services and compute. AI is a participant, not the system's monetary authority.

### The Frank–Bob example

Frank uses little AI. He still receives his properly funded resource entitlement and can hold it, redeem gold/silver/copper, or trade claims to Bob, who wants more compute than his own allocation provides. Bob can select any competing service provider. Frank does not have to change his lifestyle. The terms are voluntary; no exchange is guaranteed.

## What is unresolved?

The central question is **where real, recurring and legally owned backing for a universal distribution comes from**. Additional hard problems include physical collateral auditing, proof of all liabilities, copper divisibility, ownership rights, identity/eligibility without surveillance, governance capture, real-world redemption costs and financial law. See [Open questions](OPEN_QUESTIONS.md).

## Relationship to existing work

Universal Basic Compute, GoodDollar, Circles, Kinesis and Akash already explore overlapping components. This repository makes **no claim of having invented those ideas**, and no exhaustive originality search has been completed. See [the source-linked comparison](PRIOR_ART.md).

## Research questions open for review

- [Can a fully backed universal dividend be funded sustainably?](https://github.com/Christopher-Charman/open-resource-dividend/issues/2)
- [What proves physical metal ownership, custody and all outstanding liabilities?](https://github.com/Christopher-Charman/open-resource-dividend/issues/3)
- [Can you identify closer prior art or disprove the proposed differentiation?](https://github.com/Christopher-Charman/open-resource-dividend/issues/4)

Contributors are encouraged to submit sources, worked counterexamples and objections. No token purchases or financial participation are requested.

## Community challenge: should ORD issue a currency at all?

The [open research Discussion #12](https://github.com/Christopher-Charman/open-resource-dividend/discussions/12) compares separate metal receipts, a legally specified basket, and an **issuer-neutral distribution layer over existing backed assets**. Independent criticism, better precedents and clear evidence against these alternatives are expressly invited.

## New: economic feasibility in purchasing-power terms

The [reproducible economic value study](research/VALUE_AND_FUNDING.md) investigates what an **independently funded** worldwide allocation could plausibly purchase, rather than treating grams of metal as an income. Under purely hypothetical costs and population assumptions, providing a metal entitlement with a **$100 annual reference value** to 8.3 billion people would require around **$946 billion of annual external funding**. A productive endowment yielding an assumed 4% in a period would imply roughly **$23.6 trillion of pre-existing capital**. Neither such funds nor the assumed investment yield exists or is guaranteed.

The result is deliberately sceptical about using one metal at fixed market quotes: copper-only purchases at this scale vastly exceed historical annual mined output. USD is a **comparison numeraire**, not a dollar peg or a monetary-issuance rule. This research is a feasibility challenge, not an intended payout.

## Physical ownership must be more than a digital promise

The [new primary-source title/custody review](research/TITLE_AND_CUSTODY.md) compares LBMA allocated and unallocated bullion holdings with the LME's electronic metal-warrant system. It explains why even a fully audited transaction ledger can represent a **credit claim against an institution** rather than individually enforceable physical ownership. A proposed resource-backed dividend must specify which right its recipients actually hold.

## Gold, silver and copper: the original resource basket

The new [three-metal research comparison](research/THREE_METAL_COMPARISON.md) covers **all three materials in the original concept**, using separately sourced 2025 mine-production figures. At explicitly assumed prices, even an entirely hypothetical transfer of **1% of annual world mine output in each metal** would represent only about **$1.05 of commodity reference value per person** across 8.3 billion people before costs. No ownership or donation of that production is established.

That conclusion does not rule out transfers of existing aboveground metal stock or independently financed ownership. It shows why identifying a lawful funding source matters more than inventing a ledger.

## Working issuer-neutral distribution reference

The [RFC 0002 candidate](research/RFC_0002_ISSUER_NEUTRAL_DISTRIBUTION.md) and [dependency-free demonstration](examples/issuer_neutral_distribution.py) show how a **fund that already holds existing external resource claims** could allocate those rights to Frank, Bob and other holders without minting a new ORD currency. Copper and gold claims from independent fictional custodians remain distinct, and pending physical-redemption requests remain liabilities until separately resolved.

The example also demonstrates why a synthetic account balance **cannot prove** physical gold, copper, legal ownership, signed consent, eligible humans or a funded real-world dividend. This is a research option for public criticism, not an adopted monetary standard or launched financial service.

## Reuse real systems, not an invented financial stack

The [live external-project assessment](research/EXISTING_PROJECTS_DUE_DILIGENCE.md) now examines **Paxos PAXG, Kinesis gold/silver, GoodDollar/GoodCollective funded UBI pools, current Circles v2, the Windfall Trust, and Akash**, using published redemption contracts, external audit directories and actual open-source code. The [interoperability specification](research/INTEROPERABILITY_SPEC.md) identifies which existing components could inform ORD and what evidence would be necessary before anyone could honestly claim that commodity title transfers to a universal recipient.

**Key finding:** GoodCollective supplies a particularly relevant *funded-pool distribution pattern*; Paxos and Kinesis already provide physical-metal instruments, but their actual redemption minimums, issuer powers and jurisdictional requirements mean none is a verified drop-in universal ORD backing asset. No partnership, integrated live provider or real reserve exists.

## First contributions welcome

No AI account, investment, coding background or connection to the original proposer is required to join the research. Two bounded starter tasks are open:

- [Verify three prior-art references from primary sources — good first issue #9](https://github.com/Christopher-Charman/open-resource-dividend/issues/9)
- [Compare real physical metal redemption minimums and costs — good first issue #10](https://github.com/Christopher-Charman/open-resource-dividend/issues/10)

The project benefits from evidence-based criticism as much as supportive contributions.

## Community stewardship

[Join the public discussion on volunteering and maintaining ORD](https://github.com/Christopher-Charman/open-resource-dividend/discussions/5). The project welcomes contributors who question the hypothesis as well as those who support it. No contributor requires the founder's permission to fork or propose research; invited collaborators can independently maintain routine project work. The original proposer may remain the account owner without controlling every research decision. [Governance](GOVERNANCE.md) · [Stewardship roadmap](COMMUNITY_HANDOFF.md) · [Code of conduct](CODE_OF_CONDUCT.md).

The personal-account owner retains GitHub-specific administrative controls. This distinction is stated openly: community stewardship is being built; it is **not yet a proven independent maintainer group**. [Independent-maintainer acceptance task](https://github.com/Christopher-Charman/open-resource-dividend/issues/7).

## New: quantitative feasibility and independent audit challenge

The [independently reproducible research package](research/README.md) now examines the proposal rather than assuming it works. Using dated copper production data, it shows that even an entirely **hypothetical** transfer of 1% of one year's world copper mine output would provide only about **28.5 grams of copper content per person across 8.3 billion people**, before costs. No actual metal is held or pledged to ORD.

The [dual-book audit example](examples/compare_books.py) deliberately finds a shortfall between an internally consistent claims ledger and a separate physical-inventory declaration. It **does not** claim to certify any real reserves. [Three alternative resource-claim structures](research/RFC_0001_RESOURCE_CLAIMS.md) remain open for community scrutiny; a new issuer or token is not assumed necessary.

Source-linked findings: [physical scarcity study](research/COMMODITY_SCALE.md) · [wholesale vs retail redemption](research/REDEMPTION_EVIDENCE.md) · [RFC 0001](research/RFC_0001_RESOURCE_CLAIMS.md).

## Reproducible open research

All examples use the Python standard library, synthetic metal units and **no real assets or identities**. Contributors can reproduce the stock-flow model, independently reconstruct its event history, and run a four-period funding shortfall scenario from a fresh clone. The checks validate only arithmetic and event consistency under assumed custody; they do not attest gold, silver or copper.

See [Development](DEVELOPMENT.md), [Architecture](ARCHITECTURE.md), [Research method](RESEARCH_METHOD.md) and [Roadmap](ROADMAP.md). New contributors can start with the [public research questions](OPEN_QUESTIONS.md) or a [source-based counterexample](https://github.com/Christopher-Charman/open-resource-dividend/issues/2).

## Scope and participation

This repository contains **research documents and non-financial accounting illustrations**. It contains no token smart contracts, no mainnet, no fundraising, no financial promotion, and no affiliated third-party provider. Contributions that disprove an assumption or identify a closer precedent are welcome.

Original research text: [CC BY 4.0](LICENSE.md). Illustrative source code: [MIT License](LICENSE-CODE.md). Do not copy third-party content without its own licence and attribution.
