import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias

df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_cvli = df_ocorrencias[['aisp','ano','cvli']]

# Criando o DataFrame sobre crimes violentos letais intencionais de 2023 e 2024
df_cvli = df_cvli[df_cvli['ano'].isin([2023,2024])]
df_cvli = df_cvli.groupby(['aisp']).sum(['cvli']).reset_index()


# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_cvli)

# Criando o array sobre crimes violentos letais intencionais
array_cvli = np.array(df_cvli['cvli'])

# Obtendo a média sobre crimes violentos letais intencionais
media_cvli = np.mean(array_cvli)

# Obtendo a mediana sobre crimes violentos letais intencionais
mediana_cvli = np.median(array_cvli)

# Obtendo a distância entre a média e a mediana dos crimes violentos letais intencionais
distancia_cvli = abs((media_cvli - mediana_cvli) / mediana_cvli) 

# Obtendo o máximo e o mínimo dos crimes violentos letais intencionais
maximo_cvli = np.max(array_cvli)
minimo_cvli = np.min(array_cvli)

# Obtendo a amplitude dos crimes violentos letais intencionais
amplitude_cvli = maximo_cvli - minimo_cvli

# Obtendo os Quartis dos crimes violentos letais intencionais - Método weibull
q1_cvli = np.quantile(array_cvli, 0.25, method='weibull')
q2_cvli = np.quantile(array_cvli, 0.50, method='weibull')
q3_cvli = np.quantile(array_cvli, 0.75, method='weibull')
iqr_cvli = q3_cvli - q1_cvli

# Identificando os outliers superiores e inferiores dos crimes violentos letais intencionais
limite_superior_cvli = q3_cvli + (1.5 * iqr_cvli)
limite_inferior_cvli = q1_cvli - (1.5 * iqr_cvli)

# Filtrando o DataFrame dos crimes violentos letais intencionais
df_cvli_outliers_superiores = df_cvli[df_cvli['cvli'] > limite_superior_cvli]
df_cvli_outliers_inferiores = df_cvli[df_cvli['cvli'] < limite_inferior_cvli]


# Obtendo as medidas dos crimes violentos letais intencionais
variancia_cvli = np.var(array_cvli)
distancia_cvli = variancia_cvli / (media_cvli**2)

desvio_padrao_cvli = np.std(array_cvli)
coeficiente_var_cvli = desvio_padrao_cvli / media_cvli



# Exibindo os dados dos crimes violentos letais intencionais
print("\n--------- OBTENDO INFORMAÇÕES dos crimes violentos letais intencionais -----------")
print(f"A média dos crimes violentos letais intencionais é {media_cvli:.0f}")
print(f"A mediana dos crimes violentos letais intencionais  é {mediana_cvli:.0f}")
print(f"A distância entre a média e a mediana dos crimes violentos letais intencionais é {distancia_cvli}")
print(f"O menor valor dos crimes violentos letais intencionais é {minimo_cvli:.0f}")
print(f"O maior valor dos crimes violentos letais intencionais é {maximo_cvli:.0f}")
print(f"A amplitude dos crimes violentos letais intencionaiss é {amplitude_cvli:.0f}")
#print(f"O valor do q1 - 25% dos crimes violentos letais intencionais é {q1_cvli:.0f}")
#print(f"O valor do q2 - 50% dos crimes violentos letais intencionais é {q2_cvli:.0f}")
#print(f"O valor do q3 - 75% dos crimes violentos letais intencionais é {q3_cvli:.0f}")
#print(f"O valor do iqr = q3 - q1 dos crimes violentos letais intencionais é {iqr_cvli:.0f}")
print(f"O limite inferior dos crimes violentos letais intencionais é {limite_inferior_cvli:.0f}")
print(f"O limite superior dos crimes violentos letais intencionais é {limite_superior_cvli:.0f}")
print(f"O coeficinte dos crimes violentos letais intencionais é {coeficiente_var_cvli:.0f}")
print(f"O Desvio Padrão dos crimes violentos letais intencionais é {desvio_padrao_cvli:.0f}")


print('\n- Verificando a existência de outliers inferiores -')
if len(df_cvli_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_cvli_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_cvli_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_cvli_outliers_superiores)

# Visualizando os dados  dos crimes violentos letais intencionais
print("\nVISUALIZANDO OS DADOS...")
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados dos crimes violentos letais intencionais')

# Posição 01: Gráfico dos Dados dos crimes violentos letais intencionais
plt.subplot(2,2,1)
plt.title('BoxPlot  dos crimes violentos letais intencionais')
plt.boxplot(array_cvli,vert=False,showmeans=True)

# Posição 02: Histograma dos crimes violentos letais intencionais
plt.subplot(2,2,2)
plt.title('Histograma dos crimes violentos letais intencionais')
plt.hist(array_cvli,bins=100,edgecolor='black')

# Posição 03: Lista dos crimes violentos letais intencionais
df_cvli_outliers_superiores_order = df_cvli_outliers_superiores.sort_values(by='cvli',ascending=True)
plt.subplot(2,2,3)
plt.title('Ranking dos crimes violentos letais intencionais')
plt.barh(df_cvli_outliers_superiores_order['aisp'].astype(str),df_cvli_outliers_superiores_order['cvli'])


# Posição 04: Medidas Descritivas dos crimes violentos letais intencionais
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos crimes violentos letais intencionais')
plt.axis('off')
plt.text(0.1,0.9,f'A média dos crimes violentos letais intencionais é {media_cvli:.0f}',fontsize=12)
plt.text(0.1,0.8,f'A mediana dos crimes violentos letais intencionais é {mediana_cvli:.0f}',fontsize=12)
plt.text(0.1,0.7,f'A distância entre a média e a mediana dos crimes violentos letais intencionais é {distancia_cvli}',fontsize=12)
plt.text(0.1,0.6,f'O menor valor dos crimes violentos letais intencionais é {minimo_cvli:.0f}',fontsize=12)
plt.text(0.1,0.5,f'O maior valor dos crimes violentos letais intencionaisé {maximo_cvli:.0f}',fontsize=12)
plt.text(0.1,0.4,f'A amplitude dos valores dos crimes violentos letais intencionais é {amplitude_cvli:.0f}',fontsize=12)
#plt.text(0.1,0.3,f'O valor do q3 - 75% dos crimes violentos letais intencionais é {q3_cvli:.0f}',fontsize=12)
plt.text(0.1,0.3,f'A distância dos crimes violentos letais intencionais é {desvio_padrao_cvli:.0f}',fontsize=12)
#plt.text(0.1,0.2,f'O valor do iqr = q3 - q1 dos crimes violentos letais intencionais é {iqr_cvli:.0f}',fontsize=12)
plt.text(0.1,0.2,f'O coeficiente dos crimes violentos letais intencionais é {coeficiente_var_cvli:.0f}',fontsize=12)
plt.text(0.1,0.1,f'O limite superior dos crimes violentos letais intencionais é {limite_superior_cvli:.0f}',fontsize=12)

# Posição 04: Vazio
plt.subplot(2,2,4)
plt.axis('off')

# Exibindo o Painel
plt.tight_layout()
plt.show()
