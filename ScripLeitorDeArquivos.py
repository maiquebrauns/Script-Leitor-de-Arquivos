import os
import pandas as pd     
import plotly.express as px


#Listando e importando os arquivos.

lista_arquivo = os.listdir("C:\\Users\\Maique\\Documents\\Python\\Python-Projects\\Base-Dados\\Vendas")

tabela_total = pd.DataFrame()

for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"C:\\Users\\Maique\\Documents\\Python\\Python-Projects\\Base-Dados\\Vendas\\{arquivo}")
        tabela_total = pd.concat([tabela_total, tabela])


#Produto mais vendido(em quantidade).

tabela_produtos = tabela_total.groupby('Produto').sum(True)
tabela_produtos = tabela_produtos[["Quantidade Vendida", "Preco Unitario"]].sort_values(by="Quantidade Vendida", ascending=False)
print(tabela_produtos)

#Produto que mais faturou.
print("-----------------------------------------------")

tabela_total['Faturamento'] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby('Produto').sum(True)
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(tabela_faturamento)

#Loja que mais vendeu
print("------------------------------------------")

tabela_lojas = tabela_total.groupby('Loja').sum(True)
tabela_lojas = tabela_lojas[["Faturamento"]].sort_values(by="Faturamento", ascending=False) 
print(tabela_lojas)

#Criando gráfico para melhor visualização.

grafico = px.bar(tabela_lojas, x=tabela_lojas.index,y='Faturamento')
grafico.show()



