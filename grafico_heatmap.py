import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_heatmap.csv', sep='\t', header=None)
df.columns = ['departamento', 'valor']

df['indice'] = df.groupby('departamento').cumcount()
pivot_df = df.pivot(index='indice', columns='departamento', values='valor')

plt.figure(figsize=(10, 6))
sns.heatmap(pivot_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Mapa de Calor (Heatmap de Correlação)')
plt.tight_layout()
plt.show()