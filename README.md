# Open Resource Dividend (ORD)

**Open research into universal economic ownership without compulsory dependence on AI, a proprietary currency issuer, or a particular service provider.**

As AI changes how wealth is produced, ORD asks whether everyone could receive a **genuinely funded, freely exchangeable ownership interest in scarce physical resources**—initially gold, silver or copper—while remaining free to save, transfer, sell, or seek lawful physical redemption.

**ORD is a proposal, not an issued token or operating fund.** No assets, universal payments, custodian, financial licence, audited reserves, verified physical delivery, investor returns or guaranteed income exist here. The economic and legal feasibility remain open to falsification. No one is being asked to invest or deposit assets.

[Start here](START_HERE.md) · [White paper](WHITEPAPER.md) · [FAQ](FAQ.md) · [Research](research/README.md) · [Prior art](PRIOR_ART.md) · [Developer guide](DEVELOPMENT.md) · [Contribute](CONTRIBUTING.md) · [Governance](GOVERNANCE.md)

## The idea

Frank rarely uses AI. Bob wants additional compute. **If** an independent fund has legally acquired real, unencumbered resource claims and can distribute them fairly, both receive a funded allocation. Frank can retain his rights or voluntarily trade them to Bob for anything they both value. Bob can buy compute from competing providers. Neither must use AI, and neither is forbidden to acquire more than the original allocation.

The proposed rules separate five things:

1. **Funding:** the distributable pool must already own legitimate assets or receive actual income; issuing a digital receipt is not a source of wealth.
2. **Backing and ownership:** each enforceable claim needs independently inspected, unencumbered physical reserves and legally defensible rights, not a mere price quotation.
3. **Open accounting:** an append-only, independently witnessable record should reconcile issued claims, transfers, locked obligations, redemptions and complete liabilities.
4. **Voluntary exchange:** holders choose what to do with property; no mandated AI service, provider, purchaser, price or maximum accumulated holding.
5. **Practical exit:** legal title, actual physical delivery conditions, custody fees and insolvency rights must work for ordinary small holders—not just wholesale institutions.

An immutable hash chain **cannot itself prove that metal exists or belongs to the person receiving a token**.

## What existing work tells us

ORD does not claim invention of commodity receipts, universal income, AI-windfall trusts, tokenised bullion or open transfer networks. The [external-project review](research/EXISTING_PROJECTS_DUE_DILIGENCE.md) examines existing systems and their published source, terms and limitations.

| Evidence now available | What ORD can use or learn | What is still unverified |
| --- | --- | --- |
| [GoodCollective's funded UBI pool](https://github.com/GoodDollar/GoodCollective/blob/master/packages/contracts/contracts/UBI/UBIPool.sol) | Open-source distribution logic based on an existing pool balance | Distribution of independently titled physical resources, universal privacy, limits on managers |
| [Paxos PAXG](research/TRANSFER_INTERFACE_FINDINGS.md) and [Kinesis KAU/KAG](research/EXISTING_PROJECTS_DUE_DILIGENCE.md) | Actual bullion-claim terms, transfer conventions, custody/redemption precedents | Affordable global small-holder delivery and rights free of unacceptable issuer discretion |
| [Paxos public holder-to-bar lookup](research/PUBLIC_BAR_ALLOCATION_EVIDENCE.md) | Existing mapping of token balances to identified gold bars | Independent per-holder vault/title verification and legally successful exit |
| [Windfall Trust and resource dividends](PRIOR_ART.md) | Potential precedents for an independent economic source of distributions | A committed ORD endowment and reliable recurring funding |
| [Quantitative commodity and financing research](research/README.md) | Transparent funding/market-scale counterexamples | A viable, scalable funding mechanism at executable prices |

For example, an illustrative **$100/year reference value for each of 8.3 billion people** would require around **$946 billion in annual external funding** under one expressly hypothetical cost model. That is **not a proposed dollar peg or an existing fund**. At hypothetical prices, acquiring such quantities of one metal would materially affect markets. See [the full assumptions](research/VALUE_AND_FUNDING.md) and [gold, silver and copper comparisons](research/THREE_METAL_COMPARISON.md).

**Candidate architecture under review:** [RFC 0002](research/RFC_0002_ISSUER_NEUTRAL_DISTRIBUTION.md) asks whether ORD could simply distribute *existing* independently held claims, without minting its own currency. It is a hypothesis, **not** a selected monetary protocol. [Open discussion](https://github.com/Christopher-Charman/open-resource-dividend/discussions/12).

## First live external-ledger observation

ORD has now [cross-checked actual PAX Gold token supply](research/LIVE_PAXG_CHAIN_EVIDENCE.md) at **Ethereum mainnet finalised block 26,315,983** through **two independent public RPC operators**. Both matched **442,885.899659 PAXG**, the block hash, 18-decimal precision and deployed contract code. The [open-source read-only verifier](research/paxg_chain_observer.py) and [exact observation JSON](research/observations/paxg_ethereum_block_26315983.json) permit independent inspection.

**Scope:** this is verified **on-chain supply**, not an audit of gold bars, all issuer liabilities, legal title or an ORD-funded distribution. No wallet, provider account, token transfer or financial service was involved.

## Original independent accountant's gold reserve examination

We've now reviewed the [issuer-hosted September 2026 KPMG report](research/KPMG_SEPTEMBER_2026_ATTESTATION.md), not merely the token issuer's transparency page. It states **435,306 reported PAXG liabilities across four networks** and **435,306 fine troy ounces of gold** at its **30 September, 21:00 UTC** cutoff. Two independent Ethereum nodes corroborated the exact block timestamps surrounding that instant. The [reproducible report verifier](research/attestation_cutoff_reconciler.py) checks the published arithmetic but **does not falsely claim historic on-chain supply, personal legal title or independent physical vault inspection have been verified by ORD**.

## Reproduce the research

The illustrative accounting and financing examples need only **Python 3.10+ standard library**—no wallet, account, package installation, chain, paid CI or proprietary service.

```bash
git clone https://github.com/Christopher-Charman/open-resource-dividend.git
cd open-resource-dividend
python3 -m unittest discover -s examples -p 'test_*.py' -v
python3 -m unittest discover -s research -p 'test_*.py' -v
python3 examples/issuer_neutral_distribution.py
python3 examples/provider_transfer_evidence.py
python3 research/value_funding.py
```

The examples use **fabricated balances, recipients and provider-shaped records**. Passing tests establishes internal model behaviour only, **not live financial execution or an independent gold audit**. See [developer instructions](DEVELOPMENT.md) and [research evidence method](RESEARCH_METHOD.md).

## Contribute or challenge the idea

The project benefits from serious counterexamples, closer precedents, economic criticism and legal corrections—not just supportive commentary.

- [Can a universal resource dividend actually be funded? #2](https://github.com/Christopher-Charman/open-resource-dividend/issues/2)
- [What independent evidence establishes enforceable metal rights? #3](https://github.com/Christopher-Charman/open-resource-dividend/issues/3)
- [Find a closer earlier system #4](https://github.com/Christopher-Charman/open-resource-dividend/issues/4)
- [Compare public gold-bar allocations and real attestations #19](https://github.com/Christopher-Charman/open-resource-dividend/issues/19)
- [Evaluate authorised, no-real-value provider sandbox transfer evidence #20](https://github.com/Christopher-Charman/open-resource-dividend/issues/20)
- [First non-founder maintainer acceptance #7](https://github.com/Christopher-Charman/open-resource-dividend/issues/7)

First contributions without code: [verify references #9](https://github.com/Christopher-Charman/open-resource-dividend/issues/9) or [research redemption costs #10](https://github.com/Christopher-Charman/open-resource-dividend/issues/10). See [community discussion](https://github.com/Christopher-Charman/open-resource-dividend/discussions/5), [roadmap](ROADMAP.md), [code of conduct](CODE_OF_CONDUCT.md) and [security guidance](SECURITY.md).

## Open governance and continuity

Christopher Charman remains the original GitHub repository owner, but **the research is open to independent critique, forks, governance proposals and consenting maintainers**. There is no permanent founder veto over evidence. Routine community maintenance can be shared with invited contributors; owner-only GitHub administrative powers still belong to the personal account. An independent maintainer has **not yet** been verified. See [Governance](GOVERNANCE.md) and [Stewardship](COMMUNITY_HANDOFF.md).

Original research/documentation: [CC BY 4.0](LICENSE.md). Illustrative code: [MIT](LICENSE-CODE.md). Upstream material retains its own licence; current [Circles v2](https://github.com/aboutcircles/circles-contracts-v2) code is AGPL-3.0 and is **not** copied into ORD.

For a citable fixed snapshot, see [ORD Research v0.6 — real external-ledger evidence](https://github.com/Christopher-Charman/open-resource-dividend/releases/tag/v0.6.0) ([earlier v0.5](https://github.com/Christopher-Charman/open-resource-dividend/releases/tag/v0.5.0)). Current work and corrections are on `main`. **ORD is public research, not a currency launch or financial solicitation.**
