import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados Financeira
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame Delegacias

df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_veiculo = df_ocorrencias[['cisp', 'roubo_veiculo']]
# DF Consolidado
df_roubo_veiculo = df_roubo_veiculo.groupby(['cisp']).sum(['roubo_veiculo']).reset_index()

print('\n-----------exibindo---------')
print(df_ocorrencias.head())
print(df_roubo_veiculo)