import pandas as pd
df = pd.read_csv('Churn_Modelling.csv')
df['Balance'] = df['Balance'].round().astype(int)
df['EstimatedSalary'] = df['EstimatedSalary'].round().astype(int)
nome_ficheiro_saida = 'churn_sanitized.csv'
df.to_csv(nome_ficheiro_saida, index=False)

