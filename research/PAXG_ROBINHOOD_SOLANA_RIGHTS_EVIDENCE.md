# Three independently observed PAXG networks, and Solana's actual holder-control rights

**Source research and live public readbacks · 1 November 2026 · No financial activity or user wallet access**

This investigation advances the four-network September KPMG attestation study. The original report describes **Ethereum, Base, Robinhood Chain and Solana** PAXG supply at **2026-09-30 21:00 UTC**. It is an independent accountants' examination of a particular management assertion, not proof of affordable, irrevocable ownership for all holders.

## Robinhood Chain: formerly missing historical supply, now independently corroborated

The Robinhood Chain [official mainnet guide](https://docs.robinhood.com/chain/connecting/) identifies EVM chain **4663**, and KPMG Exhibit A identifies PAXG contract `0x121BbE58fe4684057FB66d2dd535A19e16B4f66F`.

After earlier no-archive failures, **three separate providers** were located that served historical token state at the same cutoff:

- [Pinax public RPC](https://robinhood.rpc.pinax.network), `robinhood.rpc.pinax.network`
- [dRPC Robinhood](https://robinhood.drpc.org), `robinhood.drpc.org`
- [Pocket Network](https://robinhood.api.pocket.network), `robinhood.api.pocket.network`

**All three independently returned**:

| Exact on-chain item | September 30, 2026 |
| --- | --- |
| Last block before 21:00 UTC | **76,821,239** at **20:59:59 UTC** |
| Last block hash | `0x84fda2283dd7f328d2c8487b2337567a1c69418aba53b4b774c34dde68cf8365` |
| Following block | **76,821,240** at exactly **21:00:00 UTC** |
| Following hash | `0x2ea4e53598d56d57032abe4a283ec1f3c69aed15ac58059d67e8aec793e0e210` |
| Contract decimals | 18 |
| Historical `totalSupply()` | `5000602000000000000` atomic units |
| **Actual PAXG supply** | **5.000602 PAXG** |
| Contract code | 2,052 bytes, SHA-256 `20a6d3df9e472dc509b5e3bb553e2186605401a16f018058f0cefd23e1033d70` |
| KPMG displayed quantity | **5 whole PAXG** |

The difference to KPMG's displayed whole token quantity is **+0.000602**. As with Ethereum and Base, it is compatible with a *hypothetical* nearest-whole presentation, but **the accountant's actual rounding rule has not been established**.

Evidence preserved in [the separate September Robinhood receipt](observations/paxg_robinhood_block_76821239.json). The existing [read-only EVM verifier](paxg_other_evm_cutoff.py) now defaults to two confirmed independent archive-capable operators for Robinhood. A third independent provider was used as an extra cross-check. This reuses the existing verification tool rather than starting a new Robinhood accounting engine.

An initial Pocket RPC result had been intermittent; it was previously correctly rejected. **Later successful, repeatable and independently corroborated three-provider state changes the conclusion.** The earlier dated negative finding remains in the prior [research receipt](observations/paxg_remaining_networks_20260930.json) as historical evidence of the investigation, not current truth.

## Solana: live multi-operator metadata proves an important governance characteristic

The fourth KPMG-listed PAXG mint is `5GgRAEmv8ZxF2PR5hY72Qs5x1bnQ6UK2RbTPoqJ3wSwW`. Three independent public Solana RPC services—Solana Labs, Pocket Network and PublicNode—returned matching **contemporary** mint state around **2026-11-01 00:44:30 UTC** at slots **463,894,814–816**.

- Mainnet genesis hash `5eykt4UsFv8P8NJdTREpY1vzqKqZKvdpKuc147dw2N9d`.
- Mint owned by official Solana **Token-2022** program `TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb`.
- Observed total supply: **3,215.284434 PAXG** (raw `3215284434`, 6 decimals), not the historical September figure.
- Current mint authority: `vrmi2ELTKnUYZnNMiv6nkZv5SKptA2uu9nFSYrehgj1`.
- **Permanent delegate and freeze authority:** `2apBGMsS6ti9RyF5TwQTDswXBWskiJP2LD4cUEDqYJjk`.
- The same delegate address is also the observed authority for transfer-hook configuration and fee configuration; the currently reported transfer-hook program is **unset** and transfer fee **0 basis points**. These current settings may be changed by the permitted authorities; an unset hook is not proof the ability to configure one has been irrevocably relinquished.

Under the [official Solana Permanent Delegate specification](https://solana.com/docs/tokens/extensions/permanent-delegate), a mint-level permanent delegate may **transfer or burn token balances from any holder account without that account holder's own signature**, and ordinary account holders cannot revoke the mint's permanent delegate. The issuer/controller's **capability** is observable and relevant to ORD's aspiration of property under the holder's voluntary control. **No actual misuse, unauthorised transfer, exercise of the delegate's power, or ownership-law violation has been demonstrated.** It may be necessary for lawful financial compliance, but its effect must be understood before considering the instrument for an issuer-independent economic entitlement.

Evidence is preserved in [the source-labelled Solana mint observation](observations/paxg_solana_mint_rights_20261101.json) and can be reproduced from [the read-only standard-library observer](paxg_solana_mint_rights.py). Repeated responses from different provider backends confirm the contemporary mint metadata, **not** the September state.

### Why the September Solana quantity is still unresolved

KPMG reported **2,560 whole PAXG on Solana** at 2026-09-30 21:00 UTC. The available normal `getTokenSupply` and `getAccountInfo` requests return **current** mint state. Solana's [official mint inspection guide](https://solana.com/uk/developers/cookbook/tokens/get-token-mint) describes reading the mint state; it does not confer a historic point-in-time supply on an ordinary RPC call.

[Alchemy's Solana Account Archive](https://www.alchemy.com/docs/solana/account-archive) explicitly provides `getAccountInfo(pubkey, {"slot": S})` as a real archival tool but its **historical slot parameters are on paid plans, not free**. A paid/free API entitlement has **not** been requested or represented as an existing ORD capability.

An exploratory read-only `getSignaturesForAddress` of the current mint-authority address yielded 146 records extending back to September 25, of which 145 were after the report cutoff. Most of a bounded transaction retrieval suffered rate-limiting, and different authorised burn paths may not reference this mint authority. **That incomplete replay cannot certify September's mint supply**, so no such historical number is published as independently verified.

A serious next contribution is a lawful archive-supported **historical mint-account snapshot at an exact Solana slot bracketing 21:00 UTC**, or a complete independently evidenced replay of all mint and burn instructions across every valid authority. Do not infer historical mint supply by subtracting a few mint-authority events from current supply.

## Revised independent evidence coverage at the September cutoff

| Chain | Original KPMG Exhibit A | Independent same-cutoff on-chain observation | Status |
| --- | ---: | ---: | --- |
| Ethereum | 432,506 whole | **432,505.935219** | Two archival RPC providers agree |
| Base | 235 whole | **235.001500** | Two archival RPC providers agree |
| Robinhood Chain | 5 whole | **5.000602** | **Three archival RPC providers agree** |
| Solana | 2,560 whole | **Not independently recovered** | Current mint verified; historical quantity unresolved |
| Total | **435,306 whole** | **Not independently complete** | KPMG's independently examined management assertion remains distinct |

The exact verified sum for Ethereum + Base + Robinhood is **432,745.937321 PAXG** at the same report cutoff. This **partial sum is not a whole-system supply figure** and cannot be compared with all-network gold reserves without an independently observed Solana liability quantity and a verified report rounding policy.

None of this establishes physical bar allocation, absence of liens, holder title on custodian insolvency, small-quantity direct redemption or an actual source of worldwide philanthropic funding.

## Reproduce without keys, money or user data

```bash
python3 research/paxg_other_evm_cutoff.py --chain Robinhood
python3 research/paxg_other_evm_cutoff.py --chain Base
python3 research/paxg_attestation_ethereum_check.py
python3 research/paxg_solana_mint_rights.py
python3 -m unittest discover -s research -p 'test_*.py'
```

All programs are read-only Python standard library operations. A complete four-chain proof and a real asset-admission decision remain **unachieved**; no external issuer approval, physical custody or financing has been implied.

Sources and previous work: [KPMG original report examination](KPMG_SEPTEMBER_2026_ATTESTATION.md) · [independent Ethereum archival readback](PAXG_ARCHIVE_ETHEREUM_CUTOFF.md) · [Base verification](PAXG_BASE_AND_OTHER_NETWORKS.md) · [open issue #19](https://github.com/Christopher-Charman/open-resource-dividend/issues/19).
