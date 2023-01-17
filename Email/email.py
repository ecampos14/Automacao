import pandas as pd
import win32com.client as win32

#importar a base de dados

tabelasVendas = pd.read_excel('Vendas.xlsx')

#visualizar a base de dados
pd.set_option('display.max_columns', None)

# faturamento por loja 
faturamento = tabelasVendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()

# quantidade de protudos
quantidade = tabelasVendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

# tickt medio por loja
ticket = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()

# enviar um email com relatorio
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'eumanudcampos@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''

<p>Caros Funcionarios,</p>

<p>Segue o Relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att.,</p>
<p>Emanuele</p>
'''

mail.Send()
print('Email Enviado')