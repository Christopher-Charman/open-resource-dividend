# Independent Ethereum state at the KPMG cutoff: a partial reconciliation

**Research observation recorded 1 November 2026 · No real assets moved · Not a reserve or title certificate**

This supplements the [original 30 September KPMG report examination](KPMG_SEPTEMBER_2026_ATTESTATION.md) and the [original October live-chain result](LIVE_PAXG_CHAIN_EVIDENCE.md). It resolves one question that was genuinely unanswered when the original report was reviewed: **what does the PAXG contract itself report for Ethereum at the accountant's exact cutoff?**

## Direct independently reproduced result

At Ethereum block **26,092,843**, timestamp **2026-09-30 20:59:59 UTC**, the last block before the KPMG report's **21:00:00 UTC** examination cutoff, these two independently operated public archival RPC interfaces both returned the same result:

- [Alchemy public Ethereum RPC](https://www.alchemy.com/rpc/ethereum): `https://eth-mainnet.g.alchemy.com/public`
- [dRPC public Ethereum endpoint](https://drpc.org/public-endpoints/ethereum): `https://eth.drpc.org`

| Field | Verified on both nodes |
| --- | --- |
| Chain ID | 1 (Ethereum) |
| Block hash | `0x8188886a9f46bc06f64a47ae89a8464328ca388130addd91d9d78cb97838dfd3` |
| PAXG issuer-published Ethereum proxy | `0x45804880De22913dAFE09f4980848ECE6EcbAf78` |
| ERC-20 decimals | **18** |
| Raw `totalSupply()` | `432505935219000000000000` atomic units |
| Exact token supply | **432,505.935219 PAXG** |
| Deployed proxy code size | 1,506 bytes |
| Code SHA-256 | `0cc3661444715ecc358c2e32cb85a3175cfe9ab09b3bcd9b436e0f7c2d0a4e66` |

The exact output of the already-existing [two-node observer](paxg_chain_observer.py) is preserved as [source-observation JSON](observations/paxg_ethereum_block_26092843.json). This is **actual historical EVM contract state**, not a synthetic balance, issuer-reported value or merely a block header.

## Compared carefully with KPMG

The [issuer-hosted KPMG report](https://framerusercontent.com/assets/uwWybrLRlgkC4vexP3yLyrQVeV0.pdf), signed 23 October, presents its September 30 Ethereum figures in **whole PAXG tokens**:

| | Ethereum PAXG |
| --- | ---: |
| KPMG examined management assertion, Exhibit A | **432,506** |
| Two independently queried archival nodes at the precise prior block | **432,505.935219** |
| Exact observed minus displayed difference | **-0.064781** |
| Nearest-whole-token comparison (hypothetical policy) | **432,506** |

Thus the independently observed Ethereum state is **consistent with presentation rounded to the nearest whole token**. We have **not verified** that KPMG or Paxos actually applied that rounding convention, so this must **not** be reported as an exact-to-the-decimal KPMG match.

The KPMG report's **other three networks** remain outside this Ethereum finding: **Solana 2,560, Robinhood Chain 5 and Base 235** reported PAXG, a total of **2,800** displayed whole tokens. The report's grand total is **435,306** redeemable tokens and its stated redemption assets **435,306 fine troy ounces**. No independent historical contract supplies for those three networks were obtained in this observation.

**The report may use whole-token approximations.** A direct sum of one six-decimal on-chain quantity and three independently unverified report integers must not be presented as an independently reconciled all-network liability. Even independently verified all-network token supplies are only *the tokenized PAXG obligations*, not every potential other party's separate wrapper, secured claim or contingent contractual obligation.

## Reproduce without money, personal wallets or a new token

```bash
python3 research/paxg_chain_observer.py \
  --block 26092843 \
  --rpc-a https://eth-mainnet.g.alchemy.com/public \
  --rpc-b https://eth.drpc.org

# Also independently reread the underlying report tables:
python3 research/paxg_attestation_ethereum_check.py

# Optional verification of a separately downloaded original PDF:
python3 research/paxg_attestation_ethereum_check.py --source-pdf /path/to/report.pdf
```

The [cross-document verifier](paxg_attestation_ethereum_check.py) runs two **live historical `eth_call` reads**, checks the exact block hash/time, contract, decimals and independent agreement, then evaluates only the explicitly hypothetical nearest-whole-token presentation. If it observes a material discrepancy, it reports that rather than hiding it. It never automatically marks legal title, actual reserves or all four networks verified.

Python 3.10+ standard library only; no account creation, personal data, private keys, paid RPC requirement, blockchain transactions or issuer partnership.

## What this establishes—and what it does not

**Established independently through two RPC services:** a real *Ethereum* PAXG total-supply state from the exact last block before the KPMG reporting instant. Two providers returned the same token quantity and block/bytecode identity.

**Established through the dated original KPMG report:** the professional examination of Paxos management's assertion for four-network PAXG redeemable tokens and gold redemption assets, subject to the accountant's stated scope.

**Still unverified by ORD:** report rounding rules, historic other-network supplies, a separately inspected inventory of all physical bars, completeness of every off-chain obligation, lack of pledges, each holder's enforceable insolvency rights, affordable retail redemptions and a legitimate globally funded ORD distribution pool.

The next high-value independent work is to examine **Solana, Robinhood Chain and Base at 2026-09-30 21:00 UTC** with authoritative archival chain providers, applying each token's correct chain-specific supply definition. Do not infer global collateral adequacy from Ethereum alone.

This is a precise step toward checking a real physical-resource claim, not a decision to adopt PAXG or a recommendation to purchase it.
