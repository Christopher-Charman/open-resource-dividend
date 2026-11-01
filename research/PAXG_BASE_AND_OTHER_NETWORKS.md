# September PAXG: independent Base supply; Robinhood and Solana limits

**Public read-only research, 1 November 2026. No ORD custody, issuance, wallet, paid API, or financial transaction.**

**Evidence update, 1 November 2026:** The Robinhood historical-state gap described below was **subsequently resolved** using three independently operated archive RPC services. Read the [new direct Robinhood observation and Solana mint-rights findings](PAXG_ROBINHOOD_SOLANA_RIGHTS_EVIDENCE.md) and the [verified state receipt](observations/paxg_robinhood_block_76821239.json). The earlier investigation is retained here as dated provenance, not as the current accepted state.

The [original September KPMG examination](KPMG_SEPTEMBER_2026_ATTESTATION.md) reports PAXG token supply on **four chains** at **2026-09-30 21:00:00 UTC**. [Ethereum was previously cross-checked](PAXG_ARCHIVE_ETHEREUM_CUTOFF.md). This study independently verifies **Base** at that cutoff and preserves specific reproducible *negative* results for Robinhood and Solana, without claiming a four-chain reserve reconciliation.

## Base: two independent archival operators agree

Alchemy's documented [keyless public Base RPC](https://www.alchemy.com/rpc/base) and [dRPC](https://drpc.org/) both returned an identical 18-decimal PAXG `totalSupply()` at the last block before the reporting instant.

| Base at 30 September 2026 | Two independent providers |
| --- | --- |
| Network/chain ID | Base / **8453** |
| PAXG token contract, from KPMG Exhibit A | `0xe904AEA5E1b110c9174728fA2efFc8aeD19E98Ef` |
| Last block prior to cutoff | **52,006,326**, timestamp **20:59:59 UTC** |
| Block hash | `0x64da095197b644d97fd4e7ddb32af141119a0ad900e052724a69a3d238156fe0` |
| First block after reporting instant | **52,006,327**, timestamp **21:00:01 UTC** |
| Following block hash | `0xffa7f0fd775e510f66dd3f5725f3e5a695314858b2fcfbbdc673c658b5ae21a2` |
| Original token supply | `235001500000000000000` atomic units |
| ERC-20 precision | **18 decimals** |
| **Actual independently observed tokens** | **235.001500 PAXG** |
| KPMG Exhibit A's displayed quantity | **235 whole PAXG** |
| Observed less displayed | **+0.001500 PAXG** |
| Deployed proxy bytecode | 2,052 bytes; SHA-256 `20a6d3df9e472dc509b5e3bb553e2186605401a16f018058f0cefd23e1033d70` |

The nearest-whole-token *hypothesis* would explain the tiny difference but has not been validated as the accountants' published presentation rule. In particular, **do not subtract a rounded published figure from real raw supply and call the difference missing physical gold**.

Two RPC services observe the **same chain consensus**, not two independent physical vaults.

The [read-only verification program](paxg_other_evm_cutoff.py) checks both node results at pinned block plus the following block, rejects wrong chain IDs/contract bytecode and mismatched state, then reports the exact supply and conditional rounding result. The [immutable source observation](observations/paxg_remaining_networks_20260930.json) includes independent node names and the chain-state checksum.

## Robinhood Chain: block timing verified; historical state still inconclusive

The [Robinhood Chain official documentation](https://docs.robinhood.com/chain/connecting/) specifies mainnet **chain ID 4663** and public RPC `https://rpc.mainnet.chain.robinhood.com`. Its PAXG contract is **`0x121BbE58fe4684057FB66d2dd535A19e16B4f66F`** per the KPMG original PDF.

Multiple independent public endpoints agreed on the report cutoff blocks:
- Last preceding: **76,821,239** at **20:59:59 UTC**, hash `0x84fda2283dd7f328d2c8487b2337567a1c69418aba53b4b774c34dde68cf8365`.
- First at/after cutoff: **76,821,240** at **21:00:00 UTC**, hash `0x2ea4e53598d56d57032abe4a283ec1f3c69aed15ac58059d67e8aec793e0e210`.

Historical state retrieval was materially less reliable: official RPC reported unavailable old state; PublicNode required a personal archive token; dRPC returned a historical-state error; BlockReq's public endpoint supported only recent blocks. **One Pocket public endpoint request returned an apparent historic total of 5.000602 PAXG (18 decimals), but repeats on that same endpoint sometimes failed**, and no second independent endpoint corroborated its quantity. This is **not accepted as verified supply** or as a confirmed match to KPMG's **5 whole PAXG**.

There is a live, source-grounded research route—not a reason to issue a new token: establish *two* independent accessible **historical state** providers on chain 4663 and re-run the same pinned-block comparison. Do not claim failure of the blockchain just because public providers prune old state.

## Solana: a current supply observation is NOT the September answer

The KPMG report identifies Solana PAXG mint `5GgRAEmv8ZxF2PR5hY72Qs5x1bnQ6UK2RbTPoqJ3wSwW` and reported **2,560** PAXG at September cutoff. A read-only `getTokenSupply` request to Solana Labs' public RPC returned **3,215.284434 PAXG**, 6 decimal places, at a **later finalised slot 463,885,046**. This is **current network data** at the query context, not the September 30 state, and cannot be used to declare a shortage or surplus against the old report.

Solana's RPC `getTokenSupply` returns a result tied to the response slot; it does not automatically mean the caller requested arbitrary **historical** mint supply. A reliable cutoff comparison would need archival ledger/replay evidence or a documented independently witnessed historical mint-state snapshot, with matching program/mint identity and slot/block time.

## Current independent evidence matrix

| Source | Independently corroborated at September 30 KPMG cutoff? | Status |
| --- | --- | --- |
| Ethereum | **Yes** — two public archive providers | **432,505.935219**, report displays 432,506 |
| Base | **Yes** — two independent public archive providers | **235.001500**, report displays 235 |
| Robinhood Chain | **Header yes; actual token state not verified** | Report displays 5 |
| Solana | **No historical read at cutoff** | Report displays 2,560 |

**Do not add independently observed Ethereum and Base to *issuer-reported* Robinhood and Solana and label the resulting sum “independently verified four-chain liabilities.”** The full KPMG opinion remains a separately scoped independent accountant's examination of issuer management assertions. This research has independently verified only **two of four ledger token quantities** at the old cutoff, not gold custody, all liabilities, title or practical physical exit.

## Reproduce with ordinary public infrastructure

```bash
python3 research/paxg_other_evm_cutoff.py --chain Base

# Historical Ethereum from earlier step:
python3 research/paxg_attestation_ethereum_check.py

# No default Robinhood run exists until two archive providers are established.
python3 -m unittest discover -s research -p 'test_*.py' -v
```

Python 3.10+ standard library. Only `eth_chainId`, `eth_getBlockByNumber`, `eth_call`, `eth_getCode` permitted. The software never signs, posts an asset transfer, sees private wallets or requires third-party identity.

**Next genuinely valuable work:** a source-backed independent historical mint state on Solana; two archival readers on Robinhood; confirmation of KPMG whole-unit presentation convention; and legal/physical evidence on whether any of these assets can meet the human-scale ownership and voluntary-exit principles of ORD.

No third-party approval, provider partnership, asset purchase, redistribution or live ORD financial integration exists.
