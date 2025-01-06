# Importando a Biblioteca
import pandas as pd

# Criando a Tabela com Dados de Segurança Pública do RJ
ocorrencias = [
['Rio de Janeiro',6775561,35000],
['Niteroi',515317,2500],
['São Gonçalo',1091737,15000],
['Duque de Caxias',924624,12000],
['Nova Iguaçu',821128,10000],
['Belford Roxo',513118,9000],
['São João de Meriti',471906,8500],
['Petrópolis',306678,1000],
['Volta Redonda',273988,2000],
['Campos dos Goytacazes',507548,4000],
]
# Criando as Colunas
colunas = ['Municipio', 'Populacao', 'Roubo']

# Criando o DataFrame Dados de Segurança
df_ocorrencias = pd.DataFrame(ocorrencias,columns=colunas)

#Realizando os Calculos
soma_roubo = df_ocorrencias['Roubo'].sum()
media_roubo = df_ocorrencias['Roubo'].mean()
soma_populacao = df_ocorrencias['Populacao'].sum()
media_populacao = df_ocorrencias['Populacao'].mean()
maior_roubo = df_ocorrencias['Roubo'].max()
menor_roubo = df_ocorrencias['Roubo'].min()
maior_populacao = df_ocorrencias['Populacao'].max()
menor_populacao = df_ocorrencias['Populacao'].min()
nome_municipio_maior = df_ocorrencias[df_ocorrencias['Roubo'] == maior_roubo]['Municipio']
nome_municipio_menor = df_ocorrencias[df_ocorrencias['Roubo'] == menor_roubo]['Municipio']
taxa = df_ocorrencias ['Roubo'] /df_ocorrencias ['Populacao']


print("\n----Tabela com Dados de Segurança Pública do RJ---")
print(df_ocorrencias)
print("\n----Dados Solicitados---")
print(f"A quantidade total de roubos a pedestres foi {soma_roubo}")
print(f"A quantidade média dos roubos a pedestres foi {media_roubo}")
print(f"A quantidade total da População foi {soma_populacao}")
print(f"A quantidade média da População foi {media_populacao}")
print(f"A maior roubo de pedestres foi {maior_roubo}")
print(f"A menor roubo de pedestres foi {menor_roubo}")
print(f"A maior valor referente a População foi {maior_populacao}")
print(f"O menor valor referente a População foi {menor_populacao}")
print(f"O município com o maior índice de roubos foi(a) é {nome_municipio_maior.values[0]} que teve a qtdade de roubos {maior_roubo}")
print(f"O município com o menor índice de roubos foi(a) é {nome_municipio_menor.values[0]} que teve a qtdade de roubos {menor_roubo}")
print(taxa)