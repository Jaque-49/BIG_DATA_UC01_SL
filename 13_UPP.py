import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados Financeira
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/UppEvolucaoMensalDeTitulos.csv'

# Criando o DataFrame Delegacias

df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_hom_doloso = df_ocorrencias[['upp','hom_doloso']]
# DF Consolidado
df_hom_doloso = df_hom_doloso.groupby(['upp']).sum(['hom_doloso']).reset_index()

# Criando o array

array_hom_doloso = np.array(df_hom_doloso['hom_doloso'])


#HOM_DOLOSO

q1_hom_doloso = np.quantile(array_hom_doloso,0.25, method='weibull')
q2_hom_doloso = np.quantile(array_hom_doloso,0.50, method='weibull')
q3_hom_doloso = np.quantile(array_hom_doloso,0.75, method='weibull')
iqr_hom_doloso = q3_hom_doloso - q1_hom_doloso
limite_superior_hom_doloso = q3_hom_doloso + (1.5 * iqr_hom_doloso)
limite_inferior_hom_doloso = q1_hom_doloso - (1.5 * iqr_hom_doloso)
df_outliers_inferiores_hom_doloso = df_hom_doloso[df_hom_doloso['hom_doloso'] < limite_inferior_hom_doloso]
df_outliers_superiores_hom_doloso = df_hom_doloso[df_hom_doloso['hom_doloso'] > limite_superior_hom_doloso]

print('\n-----------exibindo---------')
print(df_ocorrencias.head())
print(df_hom_doloso)

#print dos resultados

# HOM_ DOLOSO
print(f"-------------Dados para análise outliers (Homicídios dolosos)--------------")
print(f"O valor do quartil 1 é {q1_hom_doloso}")
print(f"O valor do quartil 2 é {q2_hom_doloso}")
print(f"O valor do quartil 3 é {q3_hom_doloso}")
print(f"O valor do IQR é {iqr_hom_doloso}")
print(f"O limite inferior é {limite_inferior_hom_doloso}")
print(f"O limite superior é {limite_superior_hom_doloso}")

if len(df_outliers_inferiores_hom_doloso) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_outliers_inferiores_hom_doloso)

if len(df_outliers_superiores_hom_doloso) == 0:
    print("Não existem outliers superiores")
else:
    print(df_outliers_superiores_hom_doloso)