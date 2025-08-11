import numpy as np, pandas as pd, os, matplotlib.pyplot as plt
os.makedirs("results", exist_ok=True)
import matplotlib.ticker as mtick
np.random.seed(42); n = 1000
users = pd.DataFrame({"user_id": range(n),
                      "income": np.random.normal(75_000, 20_000, n).clip(20_000, 200_000)})
users["group"] = np.random.choice(["A","B"], size=n)
users["limit"] = np.where(users["group"]=="A", users["income"]*0.30, users["income"]*0.25)
users["utilization"] = np.random.beta(2,5,n)
users["default"] = (users["utilization"]>0.6).astype(int)

# Aggregate (keep 'group' as a column)
summary = (
    users.groupby("group", as_index=False)
         .agg(
             avg_limit=("limit", "mean"),
             avg_util=("utilization", "mean"),
             default_rate=("default", "mean")
         )
         .round(3)
)
print(summary)

# Write CSV with the group column included
summary.to_csv("results/summary.csv", index=False)

# Build a clearer, self-explanatory chart
labels = ["Policy A (30% of income)", "Policy B (25% of income)"]
rates = summary.set_index("group").loc[["A", "B"], "default_rate"].values

fig, ax = plt.subplots(figsize=(12, 6.27), dpi=200)  # ~1200x627
ax.bar(labels, rates)

# y-axis as percent
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))

# show % labels on top of bars
for i, v in enumerate(rates):
    ax.text(i, v + 0.002, f"{v*100:.1f}%", ha="center", va="bottom",
            fontsize=12, fontweight="bold")

# title + subtitle
ax.set_title(
    "Default Rate by Policy\nA = 30% income limit  •  B = 25% income limit",
    fontsize=16, weight="bold", pad=12
)
ax.set_ylabel("Default Rate")
plt.tight_layout()

# callout for the difference (in basis points)
delta_bps = (rates[1] - rates[0]) * 10000
ax.annotate(
    f"Δ {delta_bps:+.0f} bps",
    xy=(1, rates[1]),
    xytext=(0.5, max(rates) + 0.01),
    arrowprops=dict(arrowstyle="->", lw=1),
    ha="center", fontsize=11
)

# optional footer—edit to match your proxy definition
fig.text(0.01, 0.01, "Default proxy: utilization > 60%. Synthetic sample.", fontsize=10)

# Save images
plt.savefig("results/default_rate_by_policy.png", bbox_inches="tight")
plt.savefig("social_preview.png", bbox_inches="tight")  # upload this in GitHub → Settings → Social preview
plt.close()
