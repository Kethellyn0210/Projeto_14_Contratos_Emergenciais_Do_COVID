import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_excel('contrato_item.xlsx')

#print(df.head())
#print(df.info())

top_10_fornecedores = df.groupby("NMCONTRATADO")['VLTOTALATUAL'].sum(

).sort_values (ascending= False).head(10)
print(top_10_fornecedores)

plt.figure(figsize=(12, 8))
top_10_fornecedores.plot(kind='barh') # Gráfico de barras horizontais
plt.title('Top 10 Fornecedores por Valor Total em Contratos')
plt.xlabel('Valor Total (R$)')
plt.ylabel('Fornecedor')
plt.gca().invert_yaxis() # Inverte a ordem para o maior ficar em cima
plt.tight_layout()
plt.savefig('analise_contratos_covid.png')
print("Gráfico salvo com sucesso!")
