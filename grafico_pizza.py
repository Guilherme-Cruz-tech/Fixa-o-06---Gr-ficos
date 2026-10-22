import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dados_pizza.csv')

plt.figure(figsize=(7, 7))
plt.pie(
    df['faturamento'],
    labels=df['canal_venda'],
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('pastel'),
)
plt.title('Faturamento por Canal de Venda')
plt.tight_layout()
plt.show()