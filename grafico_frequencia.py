import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_frequencia.csv', sep='\t')
freq = df['tipo_atendimento'].value_counts()

plt.figure(figsize=(8, 5))
sns.barplot(x=freq.index, y=freq.values, palette='viridis')
plt.title('Frequência por Tipo de Atendimento')
plt.xlabel('Tipo de Atendimento')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()