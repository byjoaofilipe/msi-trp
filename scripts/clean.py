import pandas as pd

# 1. Carregar o dataset original (substitui 'churn.csv' pelo nome do teu ficheiro)
print("A carregar o dataset...")
df = pd.read_csv('Churn_Modelling.csv')



# 3. Converter Balance e EstimatedSalary para Inteiros (removendo as casas decimais)
print("A converter dados financeiros para inteiros...")
# Usamos o round() para arredondar corretamente antes de converter para int
df['Balance'] = df['Balance'].round().astype(int)
df['EstimatedSalary'] = df['EstimatedSalary'].round().astype(int)

# 4. Guardar o novo dataset sanitizado
nome_ficheiro_saida = 'churn_sanitized.csv'
df.to_csv(nome_ficheiro_saida, index=False)

