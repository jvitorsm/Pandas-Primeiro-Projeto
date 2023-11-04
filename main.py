# pandas
import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")



# atualizando a coluna com os novos valores

tabela.loc[tabela["Tipo"] == "Serviço", " Multiplicador Imposto"] = 1.5

tabela["Preço Base Original"] =  tabela["Multiplicador Imposto"] * tabela["Preço Base Reais"]

tabela.to_excel('ProdutosPandas')


