"""Recompute the monthly summary from data/payments.csv. Anyone can run it."""
import csv, collections
rows = [r for r in csv.DictReader(open("data/payments.csv")) if not r["flag"]]
m = collections.defaultdict(lambda: [0, 0.0])
assets = collections.Counter()
for r in rows:
    k = r["date"][:7]; m[k][0] += 1; m[k][1] += float(r["settled_usd"])
    assets[r["paid_asset"]] += 1
with open("data/monthly_summary.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["month", "payments", "settled_usd"])
    for k in sorted(m): w.writerow([k, m[k][0], f"{m[k][1]:.2f}"])
tot = sum(v[1] for v in m.values())
print(f"{len(rows)} payments, ${tot:,.2f} settled, {len(assets)} paid assets")
for k in sorted(m): print(k, m[k][0], f"${m[k][1]:,.2f}")
print("top paid assets:", assets.most_common(10))
