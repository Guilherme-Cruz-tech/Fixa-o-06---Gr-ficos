import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_dispersao.csv')

plt.figure(figsize=(8, 6))
sns.scatterplot(
    x='altura_cm', y='peso_kg', hue='sexo', data=df, palette='deep'
)
plt.title('Dispersão: Altura vs Peso por Sexo')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.legend(title='Sexo')
plt.tight_layout()
plt.show()