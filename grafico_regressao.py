import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_regressao.csv', sep='\t')

plt.figure(figsize=(8, 6))
sns.regplot(
    x='renda_mensal',
    y='gasto_mensal',
    data=df,
    scatter_kws={'alpha': 0.5},
    line_kws={'color': 'red'},
)
plt.title('Regressão: Renda Mensal vs Gasto Mensal')
plt.xlabel('Renda Mensal')
plt.ylabel('Gasto Mensal')
plt.tight_layout()
plt.show()