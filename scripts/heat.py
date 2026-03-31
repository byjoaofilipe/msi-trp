import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "k": [
        5, 10, 15, 20, 25,
        5, 10, 15, 20, 25,
        5, 10, 15, 20, 25
    ],
    "t": [
        0.10, 0.10, 0.10, 0.10, 0.10,
        0.15, 0.15, 0.15, 0.15, 0.15,
        0.20, 0.20, 0.20, 0.20, 0.20
    ],
    "score": [
        30.53, 30.53, 30.53, 30.53, 31.04,
        25.12, 25.12, 25.12, 25.12, 25.84,
        3.20, 3.20, 3.20, 3.38, 4.35
    ]
}

df = pd.DataFrame(data)

pivot = df.pivot(index="k", columns="t", values="score")

plt.figure(figsize=(8, 5))

sns.heatmap(pivot, annot=True, cmap="coolwarm", fmt=".2f", cbar_kws={'label': 'Loss Score (%)'})

plt.title("Loss Score (%) variation across k and t for transformation [0,0,1,3,0]")
plt.xlabel(" t-closeness (t)")
plt.ylabel("k-anonymity (k)")

plt.gca().invert_yaxis()

plt.savefig("heatmap.png", dpi=300, bbox_inches="tight")
plt.show()