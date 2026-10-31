# Per-holder physical allocation: actual public evidence and its limits

**Public market research · 31 October 2026 · NOT an independent audit of an issuer or an accepted ORD asset**

Earlier ORD research correctly distinguished a real token transfer from enforceable property title, but it underdescribed what existing commodity issuers already expose. Paxos now provides **address-based gold-bar allocation lookup** and publishes the approach used to keep allocations aligned to token events. This is a more relevant technical predecessor than a generic reserves dashboard. It does **not** remove the need to validate external custodial inventory, law, creditor priority, real redemption, economics, or eligibility.

## 1. The public evidence actually available

| Layer | Primary reference | What someone can inspect | What it still cannot independently certify |
| --- | --- | --- | --- |
| **External token ownership** | [Paxos PAXG terms §§4–5](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions), public Ethereum token records | Blockchain balances and transfers for a specified address/network, to the extent the wallet is visible and the relevant token/network is genuine | Gold is physically at the claimed site; beneficial title is enforceable under a particular jurisdiction; identity of a human beneficiary |
| **Holder-to-bar assignment** | [Paxos Gold Allocation Lookup](https://www.paxos.com/pax-gold) and [official allocation support guide](https://support.paxos.com/articles/7204091747-paxg-allocation-and-physical-gold-bar-details-representing-my-paxg-tokens), updated 27 March 2026 | For supported self-custody on-chain addresses, Paxos can show the *issuer-reported* bar serial number, fineness and weights for the corresponding PAXG holdings; an account holder can inspect their Paxos dashboard | A provider's own lookup is not an **independent** warehouse assay or title opinion. Exchange/custodial omnibus addresses may not identify individual beneficial holders. Allocations change over time |
| **Reconciliation implementation** | [Paxos engineering blog, 13 August 2026](https://www.paxos.com/blog/paxg-delta-based-allocation) | The issuer explains an event-driven allocation system for transfers/mints/burns, transactional deduplication, periodic bar-fragment optimisation and hourly holder reconciliation against indexed chain balances | This is an issuer account of its internal implementation, **not source code independently audited by ORD**, nor evidence that each externally visible allocation is backed by legally segregated metal in real time |
| **Aggregate bullion reserve attestation** | [PAXG monthly transparency index](https://www.paxos.com/paxg-transparency) | Provider-published independent accountant reports at dated cutoffs and their disclosed examination scopes; [Paxos gold page](https://www.paxos.com/pax-gold) links to it | A monthly reserve report does not assert that every on-chain intermediate event had a corresponding legally effective title transfer, nor prove every future delivery will succeed |
| **Actual right to leave through metal delivery** | [Paxos current PAXG terms §§11,14,15](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions) | Contractual restrictions on who can redeem, direct bar-size minimum, charges and freeze/upgrade/fee adjustment powers | Transferability at token level does not make small personal physical redemption cheap or permissionless |

**No live address is inspected here**, because no holder has volunteered an address or provided a relevant independent asset-ownership claim. The research does not ask contributors to provide personal wallets, buy tokens or identify themselves.

## 2. Why the engineering precedent matters

Paxos's August 2026 engineering account describes **delta-based bar allocations**: incoming transfer/mint/burn events update the affected holders' bar shares; a periodic optimiser reduces fragmentation; and reconciliation compares each holder's recorded allocation with on-chain balances. It describes unique bar capacities, partial bar ownership, repeated independent chain-event processing and correction of drift. <https://www.paxos.com/blog/paxg-delta-based-allocation>

The architectural lesson for ORD is **not** “copy Paxos's allocator.” It is to make a public, independently witnessable distinction between:
- a token movement on the external ledger;
- an issuer's bar/lot allocation assertion at a specific time;
- an independent legal/physical assurance statement for those bars; and
- the holder's enforceable and economically practical ability to leave.

Paxos's internal event deduplication and reconciliation are useful *design precedents* but cannot make its own custody claims independent. ORD should not introduce its own rival issuance ledger merely to regenerate an allocation index already maintained by an asset provider.

## 3. Read-only replication path available today, without financial activity

A voluntary investigator with their **own public non-exchange Ethereum or Solana PAXG address** may compare three legitimate sources, subject to the provider's actual supported networks and site availability:

1. Record a **chain/network, token contract, block height/time and observed balance** from a reputable independent blockchain reader. Public balances do not independently identify a legal human or custody vault.
2. Use the **issuer-operated public bar lookup** for that same address at approximately the same time. Record its *asserted* bar serial, fineness, assigned fine weight and observation time. If the address is an exchange omnibus account, do not claim individual owner assignment.
3. Compare apparent totals with the **relevant period's** independently issued monthly attestation, taking care to respect its date, scope and any interim mints/redemptions. A current balance cannot be directly compared with a historical reserve snapshot as if both were simultaneous.
4. Evaluate holder rights and minimums against the **current Paxos agreement**. Mark physical possession, future redemption success, insolvency priority and individual beneficial-title determination **not independently verified** unless separately evidenced.

**Do not publish someone else's address-linked holdings without their informed agreement.** No public no-credential JSON API schema for the bar-lookup UI was independently established in this review; a public web form is not automatically a supported third-party machine endpoint. Do not invent an API route or scrape private dashboard data.

## 4. Current fee and ownership rules matter more for small universal shares

[The Paxos PAX Gold Fees page, updated 19 August 2026](https://support.paxos.com/articles/2899561282-PAX-Gold-Fees), states **no current gold storage fee**. It also describes:
- a **redemption/destruction fee** schedule effective 1 September 2026, calculated marginally on rolling 30-day net redemption value; the *first $2m net redemption band* uses **0.125%**, with higher marginal bands above it;
- a **5 basis-point in-kind conversion fee**, effective 1 September 2026, for conversion from PAXG into allocated or unallocated gold;
- separate creation/trading and account charges under their respective documented conditions.

Meanwhile [PAXG terms §15.2](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions) reserve the ability to finance **future** storage fees by issuing new tokens, which may dilute existing holders; §14 describes freezing/upgrading powers and §11.4 the **430 PAXG** physical bar minimum. The contradiction is only apparent: **zero currently charged storage fees does not mean no contractually permitted future fee or dilution**.

**Technical consequence:** an asset's auditability and current fees are insufficient if the original goal includes *protection from unilateral rule changes*. The community must distinguish legally required compliance actions from discretionary economic rights and decide what credible independent exit/alternative custody exists. No PAXG integration has been accepted or recommended.

## 5. Proposed contributor acceptance record

A valuable public research submission for any metal-claim issuer could supply a **source-cited, appropriately privacy-protected** record with:

| Category | Evidence |
| --- | --- |
| `token_proof` | Network, contract/asset, dated chain height, independent reader and amount |
| `issuer_allocation` | Exact issuer, dated bar/lot reference(s), grade/weight, observed source and any reassignment window |
| `independent_physical_audit` | Independent firm, engagement scope, cutoff time, reserve-to-liability reconciliation and limitations |
| `legal_title_analysis` | Governing law, who owns the bar, third-party liens, bankruptcy priority, transfer mechanism and qualified independent interpretation |
| `exit_terms` | Physical vs cash withdrawal, minimums, currency of fees, jurisdiction/KYC eligibility, unilateral changes and actual settlement conditions |
| `funding_origin` | Evidence the distributor legitimately received existing rights from a consenting owner; future projected wealth alone is not funding |
| `recipient_privacy` | Informed permission for any public wallet evidence, avoidance of personal identity leakage and clearly specified unverifiable fields |

Such a record can be *reviewed*, but must not be labelled a completed ORD financial integration without real authorised source and destination checks. No future mint or physical warehouse move is implied by this academic design.

## Status and next evidence

**Established from sources:** documented holder-bar lookup, issuer-described allocation architecture, dated aggregate independent attestation reports, current fee schedule and contractual redemption/dilution rights.

**Not established:** a public supported bar lookup API for automated reads, authorised dual-party sandbox tests, independent live lot-level proof, global retail delivery economics, eligibility/privacy and a legally funded universal pool. No provider has been accepted as a universal ORD issuer, no real asset is held or transferred.

Related: [Transfer interface diligence](TRANSFER_INTERFACE_FINDINGS.md) · [Interoperability spec](INTEROPERABILITY_SPEC.md) · [Title/custody research](TITLE_AND_CUSTODY.md) · [Prior art](../PRIOR_ART.md).

**No endorsement, partnership, investment product, legal assurance or live financial operation is claimed.**
