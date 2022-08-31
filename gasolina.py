# código de geração do gráfico
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv('gasolina.csv')
data.head()

gasolina = sns.lineplot(x = 'dia',y='venda',data=data)
gasolina.set_title("Variação do preço da gasolina em São Paulo")
plt.legend(labels=["Preço"])
plt.savefig('gasolina.png')
