import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame Roubo de comércio
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_comercio = df_ocorrencias[['cisp', 'ano', 'roubo_comercio']]
df_roubo_comercio = df_roubo_comercio[df_roubo_comercio['ano'].isin([2023, 2024])]
df_roubo_comercio = df_roubo_comercio.groupby(['cisp']).sum(['roubo_comercio']).reset_index()


# Exibindo a base de dados recuperação de veículos
print('\n---- Exibindo os dados referentes aos roubes em comércios -----')
print(df_roubo_comercio.head())


# Criando o array da Roubo de comércio
array_roubo_comercio = np.array(df_roubo_comercio["roubo_comercio"])

# Obtendo a média Roubo de comércio
media_roubo_comercio = np.mean(array_roubo_comercio)

# Obtendo a mediana Roubo de comércio
mediana_roubo_comercio = np.median(array_roubo_comercio)

# Obtendo a distância entre a média e a mediana -  Roubo de comércio
distancia_roubo_comercio = abs((media_roubo_comercio - mediana_roubo_comercio) / mediana_roubo_comercio) * 100

# Obtendo o máximo e o mínimo -  Roubo de comércio
maximo_roubo_comercio = np.max(array_roubo_comercio)
minimo_roubo_comercio = np.min(array_roubo_comercio)

# Obtendo a amplitude -  Roubo de comércio
amplitude_roubo_comercio = maximo_roubo_comercio - minimo_roubo_comercio

# Obtendo os Quartis -  Roubo de comércio - Método weibull
q1_roubo_comercio = np.quantile(array_roubo_comercio, 0.25, method='weibull')
q2_roubo_comercio = np.quantile(array_roubo_comercio, 0.50, method='weibull')
q3_roubo_comercio = np.quantile(array_roubo_comercio, 0.75, method='weibull')
iqr_roubo_comercio = q3_roubo_comercio - q1_roubo_comercio

# Identificando os outliers superiores e inferiores -  Roubo de comércio
limite_superior_roubo_comercio = q3_roubo_comercio + (1.5 * iqr_roubo_comercio)
limite_inferior_roubo_comercio = q1_roubo_comercio - (1.5 * iqr_roubo_comercio)

# Filtrando o DataFrame -  Roubo de comércio
df_roubo_comercio_outliers_superiores = df_roubo_comercio[df_roubo_comercio['roubo_comercio'] > limite_superior_roubo_comercio]
df_roubo_comercio_outliers_inferiores = df_roubo_comercio[df_roubo_comercio['roubo_comercio'] < limite_inferior_roubo_comercio]

# Obtendo as medidas de dispersão -  Roubo de comércio
variancia_roubo_comercio = np.var(array_roubo_comercio)
distancia_var_roubo_comercio = variancia_roubo_comercio / (media_roubo_comercio**2)

desvio_padrao_roubo_comercio = np.std(array_roubo_comercio)
coeficiente_var_roubo_comercio = desvio_padrao_roubo_comercio / media_roubo_comercio


# Obtendo a correlação entre as recuperações e os roubos de veículos
# 0.9 a 1.0 (positivo ou negativo) - muito forte
# 0.7 a 0.9 (positivo ou negativo) - forte
# 0.5 a 0.7 (positivo ou negativo) - moderada
# 0.3 a 0.5 (positivo ou negativo) - fraca
# 0.0 a 0.3 (positivo ou negativo) - não possui correlação



# Exibindo os dados sobre roubo comercio
print("\n--------- OBTENDO INFORMAÇÕES SOBRE roubo comercio-----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média dos roubos de comércio é {media_roubo_comercio:.0f}")
print(f"A mediana dos roubos de comércio é {mediana_roubo_comercio:.0f}")
print(f"A distância entre a média e a mediana dos roubos de comércio é {distancia_roubo_comercio:.2f} %")
print(f"O menor valor dos roubos de comércio é {minimo_roubo_comercio:.0f}")
print(f"O maior valor dos roubos de comércio é {maximo_roubo_comercio:.0f}")
print(f"A amplitude dos valores dos roubos de comércio é {amplitude_roubo_comercio:.0f}")
print(f"O valor do q1 - 25% dos roubos de comércio é {q1_roubo_comercio:.0f}")
print(f"O valor do q2 - 50% dos roubos de comércio é {q2_roubo_comercio:.0f}")
print(f"O valor do q3 - 75% dos roubos de comércio é {q3_roubo_comercio:.0f}")
print(f"O valor do iqr = q3 - q1 dos roubos de comércio é {iqr_roubo_comercio:.0f}")
print(f"O limite inferior dos roubos de comércio é {limite_inferior_roubo_comercio:.0f}")
print(f"O limite superior dos roubos de comércio é {limite_superior_roubo_comercio:.0f}")
print(f"A variância dos roubos de comércio é {variancia_roubo_comercio:.0f}")
print(f"A distância da variância X média dos roubos de comércio é {distancia_var_roubo_comercio:.0f}")
print(f"O desvio padrão dos roubos de comércio é {desvio_padrao_roubo_comercio:.0f}")
print(f"O coeficiente de variação dos roubos de comércio é {coeficiente_var_roubo_comercio:.0f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_roubo_comercio_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_roubo_comercio_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_roubo_comercio_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_roubo_comercio_outliers_superiores)



# Visualizando os dados sobre os roubos de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,3,figsize=(23,8))
plt.suptitle('Análise dos Dados Roubo de comércio',fontsize=16)

# posição 01: BoxPlot dos roubos de comércio
plt.subplot(2,3,1)
plt.title('BoxPlot dos roubos de comércio')
plt.boxplot(array_roubo_comercio,vert=False,showmeans=True)

# posição 02: Ranking dos Roubos de comércios
plt.subplot(2,3,2)
df_roubo_comercio_outliers_superiores_order = df_roubo_comercio_outliers_superiores.sort_values(by='roubo_comercio',ascending=True)
plt.title(' Ranking dos Roubos de comércios')
plt.barh(df_roubo_comercio_outliers_superiores_order['cisp'].astype(str),df_roubo_comercio_outliers_superiores_order['roubo_comercio'])

# posição 03: Histograma dos roubos de comércio
plt.subplot(2,3,3)
plt.title('Histograma dos roubos de comércio')
plt.hist(array_roubo_comercio,bins=100,edgecolor='black')


# posição 05: Medidas descritivas dos roubos de comércio
plt.subplot(2,3,5)
plt.title('Medidas Descritivas dos roubos de comércio')
plt.axis('off')
plt.text(0.0,0.9,f'Média dos roubos de comércio {media_roubo_comercio:.0f}',fontsize=12)
plt.text(0.0,0.8,f'Mediana dos roubos de comércio {mediana_roubo_comercio:.0f}',fontsize=12)
plt.text(0.0,0.7,f'Distância entre Média e Mediana dos roubos de comércio {distancia_roubo_comercio:.2f}%',fontsize=12)
plt.text(0.0,0.6,f'Maior valor dos roubos de comércio {maximo_roubo_comercio:.0f}',fontsize=12)
plt.text(0.0,0.5,f'Menor valor dos roubos de comércio {minimo_roubo_comercio:.0f}',fontsize=12)
plt.text(0.0,0.4,f'Distância entre a Variância e Média dos roubos de comércio {distancia_var_roubo_comercio:.2f}',fontsize=12)
plt.text(0.0,0.3,f'Coeficiente de variação dos roubos de comércio {coeficiente_var_roubo_comercio:.2f}',fontsize=12)


# Exibindo o Painel
plt.tight_layout()
plt.show()