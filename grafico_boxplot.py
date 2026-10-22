import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_boxplot.csv', sep='\t', header=None)
df.columns = ['departamento', 'valor']

plt.figure(figsize=(9, 6))
sns.boxplot(x='departamento', y='valor', data=df, palette='Set2')
plt.title('Distribuição por Departamento (Boxplot)')
plt.xlabel('Departamento')
plt.ylabel('Valores')
plt.tight_layout()
plt.show()