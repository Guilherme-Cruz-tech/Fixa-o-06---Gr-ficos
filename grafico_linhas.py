import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_linhas.csv', sep='\t')
df['data'] = pd.to_datetime(df['data'])

plt.figure(figsize=(12, 6))
sns.lineplot(x='data', y='vendas', hue='loja', data=df, marker='o')
plt.title('Evolução das Vendas por Loja')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()