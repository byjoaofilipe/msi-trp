import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data from your table
data = {
    "k": [5, 5, 10, 10, 15],
    "t": [0.15, 0.20, 0.15, 0.20, 0.15],
    "score": [25.12, 3.20, 25.12, 3.20, 25.12]
}

df = pd.DataFrame(data)

# Pivot table for heatmap
pivot = df.pivot(index="k", columns="t", values="score")

# Plot
plt.figure(figsize=(8, 5))
sns.heatmap(pivot, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Max Score (%) variation across k and t")
plt.xlabel("t")
plt.ylabel("k")

plt.savefig("heatmap.png", dpi=300, bbox_inches="tight")