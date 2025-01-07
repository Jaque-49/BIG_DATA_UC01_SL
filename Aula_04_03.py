 # Importando a Biblioteca Pandas
import pandas as pd

#Importando a Base de Dados
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame Ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')


# Criando um DataFrame homicídio doloso por município
df_hom_doloso_munic = df_ocorrencias[['munic','hom_doloso']]

# Consolidando O DataFrame Homicídio Doloso por Município
df_hom_doloso_munic = df_hom_doloso_munic.groupby(['munic']).sum(['hom_doloso']).reset_index()


#Exibindo o DataFrame
print(df_ocorrencias.head())
print("\n Base de Dados - Município e Homicídio Doloso")
print(df_hom_doloso_munic.head())