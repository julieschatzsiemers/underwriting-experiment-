import numpy as np, pandas as pd, os, matplotlib.pyplot as plt
os.makedirs("results", exist_ok=True)

np.random.seed(42); n = 1000
users = pd.DataFrame({"user_id": range(n),
                      "income": np.random.normal(75_000, 20_000, n).clip(20_000, 200_000)})
users["group"] = np.random.choice(["A","B"], size=n)
users["limit"] = np.where(users["group"]=="A", users["income"]*0.30, users["income"]*0.25)
users["utilization"] = np.random.beta(2,5,n)
users["default"] = (users["utilization"]>0.6).astype(int)

summary = users.groupby("group").agg(
    avg_limit=("limit","mean"),
    avg_util=("utilization","mean"),
    default_rate=("default","mean")
).round(3)
print(summary)

summary.to_csv("results/summary.csv", index=False)
summary["default_rate"].plot(kind="bar", rot=0, title="Default Rate by Group")
plt.tight_layout(); plt.savefig("results/default_rate_by_group.png", dpi=200, bbox_inches="tight")
