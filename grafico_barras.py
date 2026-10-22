import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_barras.csv', sep='\t')

plt.figure(figsize=(10, 6))
sns.barplot(
    x='categoria', y='vendas_medias', hue='regiao', data=df, palette='muted'
)
plt.title('Vendas Médias por Categoria e Região')
plt.xlabel('Categoria')
plt.ylabel('Vendas Médias')
plt.legend(title='Região')
plt.tight_layout()
plt.show()