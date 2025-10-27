# Projeto 14: Analisando Gastos da COVID-19 📊

## O Cenário 👨‍💼

Você é um(a) Cientista de Dados Júnior recém-contratado(a) pelo governo de São Paulo. Sua primeira grande tarefa é mergulhar em uma enorme planilha que detalha cada item comprado emergencialmente durante a pandemia de COVID-19.

Os dados são brutos, confusos e cheios de linhas. É impossível tirar conclusões apenas olhando para a tabela. Seu gestor pediu a você que "faça a mágica dos dados acontecer". Ele quer um relatório visual que responda a uma pergunta fundamental: **"Para onde foi o dinheiro?"**.

Sua missão é usar Python, Pandas e Matplotlib para transformar essa massa de dados em um gráfico claro e informativo, destacando os maiores gastos e os principais fornecedores.

### Ah! Não se esqueça de verificar a planílha `covid-19-contratos-emergenciais-dicionario-de-dados.xlsx` para saber qual coluna você deve procurar em `contrato_item.xlsx`.

## 📋 Requisitos da Missão

Seu gestor precisa de um visual impactante para a apresentação do relatório. Seu script deve realizar uma análise completa e gerar um gráfico para responder às seguintes perguntas:

1.  **Carregar os Dados do Excel:** O script deve ler o arquivo `contrato_item.xlsx` e carregá-lo em um DataFrame do Pandas.
2.  **Explorar e Limpar os Dados:** Dados do mundo real nunca são perfeitos. Temos a sorte de contar com um dicionário `covid-19-contratos-emergenciais-dicionario-de-dados.xlsx` indicando o que significa cada coluna. Você precisará verificar os tipos de dados (as colunas de valor provavelmente serão lidas como texto) e convertê-los para números para poder fazer cálculos.
3.  **Realizar a Análise Principal:** Seu script deve responder a estas duas perguntas:
      * **Quais foram os 10 itens individuais mais caros adquiridos?**.
      * **Quais foram os 10 fornecedores que mais receberam dinheiro no total?**.
4.  **Gerar um Gráfico:** Crie um gráfico de barras que mostre o resultado de uma das análises acima (sugestão: Top 10 fornecedores). O gráfico deve ser claro e bem legendado.
5.  **Salvar o Relatório Visual:** O script deve salvar o gráfico final como uma imagem (`analise_contratos_covid.png`), pronta para ser enviada para a equipe de design do jornal.

## 💡 Roteiro Sugerido para o Sucesso

1.  **Instale as Bibliotecas**: Se necessário, instale as ferramentas para a missão.
    ```bash
    pip install pandas matplotlib openpyxl
    ```
2.  **Importe os Módulos**: Comece seu script Python importando as bibliotecas.
    ```python
    import pandas as pd
    import matplotlib.pyplot as plt
    ```
3.  **Carregue a Planilha**: Use a função `read_excel` do Pandas.
    ```python
    df = pd.read_excel('contrato_item.xlsx')
    ```
4.  **Investigue os Dados (Passo Crucial\!)**: Antes de qualquer cálculo, entenda seus dados\!
    ```python
    print(df.head()) # Veja as primeiras linhas
    print(df.info()) # Veja os tipos de cada coluna. Os valores da coluna procurada é um número (float) ou texto (object)?
    ```
5.  **Limpe os Dados**: Se a coluna procurada for do tipo `object`, ela precisa ser convertida para um número.
    ```python
    # Agrupa por fornecedor, soma o 'VALOR TOTAL' de cada um, ordena e pega os 10 maiores
    top_10_fornecedores = df.groupby('NOME FORNECEDOR')['VALOR TOTAL'].sum().sort_values(ascending=False).head(10)
    print(top_10_fornecedores)
    ```
7.  **Crie e Salve o Gráfico**: Transforme sua análise em um visual profissional.
    ```python
    plt.figure(figsize=(12, 8))
    top_10_fornecedores.plot(kind='barh') # Gráfico de barras horizontais
    plt.title('Top 10 Fornecedores por Valor Total em Contratos')
    plt.xlabel('Valor Total (R$)')
    plt.ylabel('Fornecedor')
    plt.gca().invert_yaxis() # Inverte a ordem para o maior ficar em cima
    plt.tight_layout()
    plt.savefig('analise_contratos_covid.png')
    print("Gráfico salvo com sucesso!")
    ```
