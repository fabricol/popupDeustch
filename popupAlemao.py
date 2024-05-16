# Dia 15/05/2024 
'''Primeira interação com esse programa,
1. Fazer esse arquivo ler uma planilha com diversas palavras em Alemão
2. Ele irá trazer uma palavra aleatória desse array
3. Desse array iremos colocar uma tradução, que deve ficar salva nesse arquivo
'''
print("Hello world!")
import openpyxl
import pandas as pd



tabela_lista_palavras_alemao = '../lista_palavras_alemao.xlsx'

tabela_lista_palavras_alemao = pd.read_excel(tabela_lista_palavras_alemao)

print(tabela_lista_palavras_alemao)

