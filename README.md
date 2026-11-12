# Genghis payment evidence

Every crypto payment Genghis has settled through its payment processor, from the first sale on 3 October 2025 to 11 November 2026. Published as traction evidence for the Genghis Stellar Community Fund application.

## Headline

| | |
|---|---|
| Settled payments | 2,371 |
| Settled value | $262,715 |
| Period | 3 October 2025 to 11 November 2026 |
| Crypto assets customers paid with | 47 |

Our application cites 1,395 payments worth $106,879. That is this dataset as first published, which ended on 20 September 2026 at 14:28. This update adds the payments settled since then and changes no earlier row.

Monthly totals are in [data/monthly_summary.csv](data/monthly_summary.csv). Every payment behind them is in [data/payments.csv](data/payments.csv).

## Where the data comes from

Genghis takes payment through a licensed crypto payment processor. The data is the processor's own payment export, and from 23 October 2026 its payment API, filtered to payments with the status "finished". It covers every customer, retail and business, so the monthly figures are total payment volume, not retail revenue alone.

## How the USD value is set

- Settled in a stablecoin (USDT or USDC on any network): the settled amount.
- Settled in another asset: the invoice value in USD.

24 payments settled at a small fraction of their invoice (for example, a $57.93 invoice that settled $0.10). They stay in `payments.csv` with a flag and are left out of every total.

Also left out: 32 partially paid payments and 3 payments invoiced in Japanese yen and settled in a volatile asset, which have no reliable USD value.

## What we removed, and why

- Customer payment addresses and transaction hashes. Published next to a purchase record, they would link a customer's wallet to what they bought.
- Exact crypto amounts. An exact amount on a known date can be matched on-chain and leads back to the customer's wallet, so each payment keeps only the asset used and the settled value in whole dollars.
- Order and processor payment IDs, which mean nothing outside our systems.
- Our own settlement wallet addresses.

Reviewers of the Stellar Community Fund can request the complete export, transaction hashes included, from claudio@genghis.pro.

## Recompute it yourself

```bash
python3 summarize.py
```

It reads `data/payments.csv` and rebuilds `data/monthly_summary.csv`. The totals above come from it.

## Related

- [genghis-stellar-poc](https://github.com/genghisecommerce/genghis-stellar-poc): the Stellar testnet proof of concept
- [genghis-stellar-docs](https://github.com/genghisecommerce/genghis-stellar-docs): the technical architecture
- [genghis.pro](https://www.genghis.pro): the live marketplace
