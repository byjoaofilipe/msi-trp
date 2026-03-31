import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

data = {
    'k': [5, 10, 15, 18],
    'Loss Score (%)': [1.55, 2.74, 2.79, 0.00],
    'Highest Risk (%)': [20.00, 10.00, 6.25, 1.61],
    'Suppressed Records (%)': [1.52, 2.69, 2.74, 0.00]
}

df = pd.DataFrame(data)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(df['k'], df['Highest Risk (%)'], marker='o', color='#e74c3c', linewidth=2.5, markersize=8, label='Highest Risk (%)')
axes[0].set_title('Redução do Risco de Reidentificação', fontsize=14, fontweight='bold', pad=15)
axes[0].set_xlabel('Valor de k', fontsize=12)
axes[0].set_ylabel('Highest Risk (%)', fontsize=12)
axes[0].set_xticks(df['k'])
axes[0].set_ylim(0, 25)
axes[0].legend(fontsize=11)

axes[0].axvline(x=15, color='gray', linestyle='--', alpha=0.7)
axes[0].text(14.5, 15, 'Configuração\nÓtima (k=15)', color='gray', ha='right', va='center', fontsize=10)

axes[1].plot(df['k'], df['Loss Score (%)'], marker='s', color='#3498db', linewidth=2.5, markersize=8, label='Loss Score (%)')
axes[1].plot(df['k'], df['Suppressed Records (%)'], marker='^', color='#f39c12', linewidth=2.5, markersize=8, label='Suppressed Records (%)')
axes[1].set_title('Impacto na Utilidade e Supressão', fontsize=14, fontweight='bold', pad=15)
axes[1].set_xlabel('Valor de k', fontsize=12)
axes[1].set_ylabel('Percentagem (%)', fontsize=12)
axes[1].set_xticks(df['k'])
axes[1].set_ylim(0, 5) 
axes[1].legend(fontsize=11)

axes[1].annotate('Colapso de\nUtilidade (Age)', xy=(18, 0), xytext=(16.5, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=6),
            fontsize=10, ha='center')
axes[1].axvline(x=15, color='gray', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('tradeoff_k_anonymity.png', dpi=300, bbox_inches='tight')
print("Gráfico 'tradeoff_k_anonymity.png' gerado com sucesso!")