import pandas as pd

df_orig = pd.read_csv('churn_sanitized.csv', sep=',')
df_m1 = pd.read_csv('modelo1.csv', sep=',')
df_m2 = pd.read_csv('modelo2.csv', sep=',')

bins = [18, 25, 35, 45, 55, 100]
labels = ['[18,25[', '[25,35[', '[35,45[', '[45,55[', '[55,93[']
df_orig['Faixa_Etaria'] = pd.cut(df_orig['Age'], bins=bins, labels=labels, right=False)

media_orig = df_orig.groupby('Faixa_Etaria', observed=True)['CreditScore'].mean().reset_index()
media_orig.columns = ['Faixa Etária', 'CS_Original']

df_m1['CreditScore'] = pd.to_numeric(df_m1['CreditScore'], errors='coerce')
df_m2['CreditScore'] = pd.to_numeric(df_m2['CreditScore'], errors='coerce')

df_m1_valido = df_m1[df_m1['Age'] != '*']
df_m2_valido = df_m2[df_m2['Age'] != '*']

media_m1 = df_m1_valido.groupby('Age')['CreditScore'].mean().reset_index()
media_m1.columns = ['Faixa Etária', 'CS_Modelo1']

media_m2 = df_m2_valido.groupby('Age')['CreditScore'].mean().reset_index()
media_m2.columns = ['Faixa Etária', 'CS_Modelo2']

resultado = media_orig.merge(media_m1, on='Faixa Etária', how='left')
resultado = resultado.merge(media_m2, on='Faixa Etária', how='left')

resultado['Dif_M1'] = resultado['CS_Modelo1'] - resultado['CS_Original']
resultado['Dif_M2'] = resultado['CS_Modelo2'] - resultado['CS_Original']

tabela_final = resultado[['Faixa Etária', 'CS_Original', 'CS_Modelo1', 'Dif_M1', 'CS_Modelo2', 'Dif_M2']]
tabela_final = tabela_final.round(2)

print("\n=== COMPARAÇÃO DE CREDIT SCORE MÉDIO ===")
print(tabela_final.to_string(index=False))