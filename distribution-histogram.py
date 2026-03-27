import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Churn_Modelling.csv')

fig, axes = plt.subplots(4, 2, figsize=(14, 20))
fig.suptitle('Distribuição dos Atributos do Dataset', fontsize=18, fontweight='bold', y=0.98)

# 1. CreditScore
ax = axes[0, 0]
ax.hist(df['CreditScore'], bins=30, color='#2E75B6', edgecolor='white', alpha=0.85)
ax.axvline(df['CreditScore'].mean(), color='#C0392B', linestyle='--', linewidth=1.5, label=f'Média: {df["CreditScore"].mean():.1f}')
ax.set_title('CreditScore', fontsize=13, fontweight='bold')
ax.set_xlabel('CreditScore')
ax.set_ylabel('Frequência')
ax.legend(fontsize=9)

# 2. Geography
ax = axes[0, 1]
geo_counts = df['Geography'].value_counts()
bars = ax.bar(geo_counts.index, geo_counts.values, color=['#2E75B6', '#27AE60', '#E67E22'], edgecolor='white')
for bar, val in zip(bars, geo_counts.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50, str(val), ha='center', fontsize=10, fontweight='bold')
ax.set_title('Geography', fontsize=13, fontweight='bold')
ax.set_ylabel('Frequência')

# 3. Gender
ax = axes[1, 0]
gen_counts = df['Gender'].value_counts()
bars = ax.bar(gen_counts.index, gen_counts.values, color=['#2E75B6', '#E74C3C'], edgecolor='white')
for bar, val in zip(bars, gen_counts.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50, str(val), ha='center', fontsize=10, fontweight='bold')
ax.set_title('Gender', fontsize=13, fontweight='bold')
ax.set_ylabel('Frequência')

# 4. Age
ax = axes[1, 1]
ax.hist(df['Age'], bins=40, color='#2E75B6', edgecolor='white', alpha=0.85)
ax.axvline(df['Age'].mean(), color='#C0392B', linestyle='--', linewidth=1.5, label=f'Média: {df["Age"].mean():.1f}')
ax.set_title('Age', fontsize=13, fontweight='bold')
ax.set_xlabel('Idade (anos)')
ax.set_ylabel('Frequência')
ax.legend(fontsize=9)

# 5. Tenure
ax = axes[2, 0]
ax.hist(df['Tenure'], bins=11, color='#2E75B6', edgecolor='white', alpha=0.85, rwidth=0.85)
ax.set_title('Tenure', fontsize=13, fontweight='bold')
ax.set_xlabel('Tenure (anos)')
ax.set_ylabel('Frequência')
ax.set_xticks(range(0, 11))

# 6. Balance
ax = axes[2, 1]
ax.hist(df['Balance'], bins=40, color='#2E75B6', edgecolor='white', alpha=0.85)
ax.set_title('Balance', fontsize=13, fontweight='bold')
ax.set_xlabel('Saldo (€)')
ax.set_ylabel('Frequência')

# 7. NumOfProducts
ax = axes[3, 0]
np_counts = df['NumOfProducts'].value_counts().sort_index()
bars = ax.bar(np_counts.index.astype(str), np_counts.values, color='#2E75B6', edgecolor='white')
for bar, val in zip(bars, np_counts.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50, str(val), ha='center', fontsize=10, fontweight='bold')
ax.set_title('NumOfProducts', fontsize=13, fontweight='bold')
ax.set_xlabel('Número de Produtos')
ax.set_ylabel('Frequência')

# 8. EstimatedSalary
ax = axes[3, 1]
ax.hist(df['EstimatedSalary'], bins=30, color='#2E75B6', edgecolor='white', alpha=0.85)
ax.set_title('EstimatedSalary', fontsize=13, fontweight='bold')
ax.set_xlabel('Salário Estimado (€)')
ax.set_ylabel('Frequência')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('histogramas_distribuicao.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.show()