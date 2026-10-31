# First real cross-provider chain observation — PAX Gold

**Observed 31 October 2026 at 23:37:33 UTC · Ethereum mainnet, finalised block 26,315,983 · research only**

This note records ORD's **first independently reproduced observation of an actual external resource-token ledger**, not another invented ledger balance. A new, standard-library-only [read-only two-node verifier](paxg_chain_observer.py) queried the live deployed PAXG token contract at the **same historical block**, through two unrelated public Ethereum RPC services.

## Independently matched on-chain facts

| Field | Exact value |
| --- | --- |
| Chain | Ethereum mainnet, chain ID `1` |
| Issuer-published PAXG proxy contract | `0x45804880De22913dAFE09f4980848ECE6EcbAf78` |
| Finalised block | `26,315,983`, timestamp `2026-10-31T23:18:47+00:00` |
| Block hash | `0x19440d133c6b75580de3313d8fc6a6914784393772710d577e6d1641f6810191` |
| ERC-20 `totalSupply()` | `442885899659000000000000` atomic token units |
| ERC-20 `decimals()` | `18`, observed on chain |
| Token supply | **442,885.899659 PAXG** |
| Bytecode size | 1,506 bytes at the published proxy contract |
| SHA-256 of deployed code bytes | `0cc3661444715ecc358c2e32cb85a3175cfe9ab09b3bcd9b436e0f7c2d0a4e66` |
| First independent RPC | [PublicNode](https://ethereum.publicnode.com/), `ethereum-rpc.publicnode.com` |
| Second independent RPC | [Nodely](https://nodely.io/docs/ethereum), `eth.nodely.dev` |
| Independent agreement | **Yes**, on chain ID, block hash/time, on-chain total supply, decimals, bytecode length and SHA-256 |

The immutable input and observed facts are preserved as a [public JSON observation](observations/paxg_ethereum_block_26315983.json) committed to this repository. An observation timestamp is **when the two node reads completed**, not the block timestamp. The numerical token balance comes from the contract state at the pinned block, not the issuer's marketing material.

### Sources establishing what was queried

- [Paxos official PAXG smart contract repository](https://github.com/paxosglobal/paxos-gold-contract) publishes the exact Ethereum proxy address and `totalSupply()`/`decimals()` ERC-20 interface. Its README says the V2 implementation is in the linked `paxos-token-contracts` submodule.
- [Ethereum JSON-RPC standard](https://ethereum.org/developers/docs/apis/json-rpc/) defines `eth_chainId`, `eth_getBlockByNumber`, `eth_call` and `eth_getCode`.
- [PublicNode](https://ethereum.publicnode.com/) and [Nodely](https://nodely.io/docs/ethereum) independently operate public Ethereum interfaces. Both returned identical supply and bytecode details when queried at the fixed block.

**Important:** two RPC operators are independent *observers of the same consensus state*. They do not constitute two independent audits of physical gold, token economic rights, actual legal title or the issuer's complete financial obligations.

## How to run this without a wallet or credentials

From a public clone (Python 3.10+ standard library):

```bash
# Current latest finalised block; pins the second node to the first node's exact height
python3 research/paxg_chain_observer.py

# Reproduce this historical observation, if BOTH chosen nodes still have archival state
python3 research/paxg_chain_observer.py --block 26315983

# Run only focused, local mocked network tests
python3 -m unittest discover -s research -p 'test_*.py' -v
```

No blockchain transaction, signing operation, wallet address, personal data, paid RPC, proprietary SDK, access token or external package is required. The verifier **only permits read-only RPC method names**. It fails on different chain IDs, block hashes, timestamps, supply, decimals, or contract code. It does **not** average disagreeing supplies or count one endpoint twice.

**Historical retrieval limit:** public RPCs may prune older state. Nodely's published documentation says historical contract-state calls beyond its pruned range are unavailable; an old pinned observation may therefore need two independently operated **archive-capable** RPCs. This is a tool availability limitation, not evidence of ledger inconsistency. The preserved JSON observation remains readable without the network. To inspect a fresh actual state, run the command without `--block`.

## An independently supported next layer exists but was NOT checked in this observation

The [Paxos public holder-to-bar allocation lookup](PUBLIC_BAR_ALLOCATION_EVIDENCE.md) links issuer-reported bar shares with supported wallet addresses. Separate [PAXG monthly attestations](https://www.paxos.com/paxg-transparency) present independent accountant evidence at each stated cutoff. But this observed block is **31 October 2026 at 23:18:47 UTC**; a September attestation cannot be blindly compared to that later supply number without accounting for intervening issuance/redemption and defining the exact audit cutoff.

To establish a specific reserve-supply relation at a monthly cutoff, a researcher would need an independent chain snapshot at the **same relevant time**, the accountant's dated report and its stated scope. Determining that the total issued PAXG token count matches a quantity in a report is not the same as personally verifying each bar's physical location, legal encumbrances, creditor priority, or a recipient's practical right to redeem.

### What the current observation proves and does not prove

| Statement | Status |
| --- | --- |
| PAXG ERC-20 `totalSupply()` at block 26,315,983 was consistently reported by two unrelated nodes | **Directly observed and cross-checked** |
| On-chain contract address/bytecode metadata are the same at the exact block | **Directly observed and cross-checked** |
| Paxos had at least 442,885.899659 troy ounces of physically available gold at that moment | **Not independently verified** |
| Issued PAXG and all off-chain or wrapped liabilities were fully backed by unencumbered gold | **Not independently verified** |
| Every PAXG holder had irrevocable, enforceable, practical physical redemption rights | **Not independently verified** |
| ORD owns PAXG or has an operating universal dividend | **False**; no assets or universal fund are claimed |
| No transaction or private-wallet request was performed | **Verified by restricted method set and recorded command** |

The public gold contract itself includes issuer-administered roles and corresponding powers; it should **not** be characterised as a neutral monetary asset merely because on-chain supply is reproducible. Exact contractual terms remain central to the economic-rights evaluation.

## Next economically meaningful validation

The next material proof layer is not another synthetic token model. It is **a dated, independent accountant's PAXG reserve attestation paired to chain supply at the exact reporting cutoff**, with explicit evidence for whether the accountant verified vault inventories, legal rights and the *entirety of liabilities*. Until that is established, ORD cannot conclude physical backing from this chain observation alone.

This documentation and tool neither seek financial provider approval nor authorise any purchase, deposit, sandbox transaction or live redemption. They preserve a narrow, independently reproducible external observation for open community review.

Related: [External issuers' contractual limitations](EXISTING_PROJECTS_DUE_DILIGENCE.md) · [Per-holder allocation](PUBLIC_BAR_ALLOCATION_EVIDENCE.md) · [Issuer-neutral distribution RFC](RFC_0002_ISSUER_NEUTRAL_DISTRIBUTION.md) · [Research methods](../RESEARCH_METHOD.md).
