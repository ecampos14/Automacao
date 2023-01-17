import pandas as pd

#importar a base de dados

tabelasVendas = pd.read_excel('Vendas.xlsx')

#visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabelasVendas)

# faturamento por loja 
faturamento = tabelasVendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# quantidade de protudos
quantidade = tabelasVendas[['Id Loja', 'Quantidade']].groupby('ID Loja').sum()

# tickt medio por loja
ticket = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
# enviar um email com relatorio
