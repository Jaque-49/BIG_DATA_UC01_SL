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

# Exibindo a base de dados sobre crimes violentos letais intencionais
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_cvli.head())

# Criando o array sobre crimes violentos letais intencionais
array_cvli = np.array(df_cvli['cvli'])

# Obtendo a média sobre crimes violentos letais intencionais
media_cvli = np.mean(array_cvli)

# Obtendo a mediana sobre crimes violentos letais intencionais
mediana_cvli = np.median(array_cvli)

# Obtendo a distância entre a média e a mediana sobre crimes violentos letais intencionais
distancia_cvli = abs((media_cvli - mediana_cvli) / mediana_cvli) * 100

# Obtendo o máximo e o mínimo sobre crimes violentos letais intencionais
maximo_cvli = np.max(array_cvli)
minimo_cvli = np.min(array_cvli)

# Obtendo a amplitude sobre crimes violentos letais intencionais
amplitude_cvli = maximo_cvli - minimo_cvli

# Obtendo os Quartis sobre crimes violentos letais intencionais - Método weibull
q1_cvli = np.quantile(array_cvli, 0.25, method='weibull')
q2_cvli = np.quantile(array_cvli, 0.50, method='weibull')
q3_cvli = np.quantile(array_cvli, 0.75, method='weibull')
iqr_cvli = q3_cvli - q1_cvli

# Identificando os outliers superiores e inferiores sobre crimes violentos letais intencionais
limite_superior_cvli = q3_cvli + (1.5 * iqr_cvli)
limite_inferior_cvli = q1_cvli - (1.5 * iqr_cvli)

# Filtrando o DataFrame sobre crimes violentos letais intencionais
df_cvli_outliers_superiores = df_cvli[df_cvli['cvli'] > limite_superior_cvli]
df_cvli_outliers_inferiores = df_cvli[df_cvli['cvli'] < limite_inferior_cvli]

# Obtendo as medidas de dispersão sobre crimes violentos letais intencionais
variancia_cvli = np.var(array_cvli)
distancia_var_cvli = variancia_cvli / (media_cvli**2)

desvio_padrao_cvli = np.std(array_cvli)
coeficiente_var_cvli = desvio_padrao_cvli / media_cvli


# Exibindo os dados sobre as sobre crimes violentos letais intencionais
print("\n Obtendo informações sobre crimes violentos letais intencionais")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média dos crimes violentos letais intencionais é {media_cvli:.0f}")
print(f"A mediana dos crimes violentos letais intencionais é {mediana_cvli:.0f}")
print(f"A distância entre a média e a mediana é dos crimes violentos letais intencionais é {distancia_cvli:.2f} %")
print(f"O menor valor dos crimes violentos letais intencionais é {minimo_cvli:.0f}")
print(f"O maior valor dos crimes violentos letais intencionais é {maximo_cvli:.0f}")
print(f"A amplitude dos valores dos crimes violentos letais intencionais é {amplitude_cvli:.0f}")
print(f"O valor do q1 - 25% dos crimes violentos letais intencionais é {q1_cvli:.0f}")
print(f"O valor do q2 - 50% dos crimes violentos letais intencionais é {q2_cvli:.0f}")
print(f"O valor do q3 - 75% dos crimes violentos letais intencionais é {q3_cvli:.0f}")
print(f"O valor do iqr = q3 - q1 dos crimes violentos letais intencionais é {iqr_cvli:.0f}")
print(f"O limite inferior dos crimes violentos letais intencionais é {limite_inferior_cvli:.0f}")
print(f"O limite superior dos crimes violentos letais intencionais é {limite_superior_cvli:.0f}")
print(f"A variância dos crimes violentos letais intencionais é {variancia_cvli:.0f}")
print(f"A distância da variância X média dos crimes violentos letais intencionais é {distancia_var_cvli:.0f}")
print(f"O desvio padrão dos crimes violentos letais intencionais é {desvio_padrao_cvli:.0f}")
print(f"O coeficiente de variação dos crimes violentos letais intencionais é {coeficiente_var_cvli:.0f}")
print('\n- Verificando a existência de outliers inferiores -')

#




# Visualizando os dados sobre 
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre sobre crimes violentos letais intencionais no Município do Rio de Janeiro')

if len(df_cvli_outliers_superiores) != 0 or len(df_cvli_outliers_inferiores) != 0:

# Posição 01: Gráfico dos crimes violentos letais intencionais
    plt.subplot(2,2,1)
    plt.title('BoxPlot dos crimes violentos letais intencionais')
    plt.boxplot(array_cvli,vert=False,showmeans=True)

    # Posição 02: Histograma dos crimes violentos letais intencionais
    plt.subplot(2,2,2)
    plt.title('Histograma dos crimes violentos letais intencionais')
    plt.hist(array_cvli,bins=100,edgecolor='black')

    # Posição 03: Lista de Municípios com Outliers
    df_cvli_outliers_superiores_order = df_cvli_outliers_superiores.sort_values(by='cvli',ascending=True)
    plt.subplot(2,2,3)
    plt.title('Ranking dos Municípios com Outliers Superiores')
    plt.barh(df_cvli_outliers_superiores_order['aisp'],df_cvli_outliers_superiores_order['cvli'])

    # Posição 04: Medidas Descritivas dos crimes violentos letais intencionais
    plt.subplot(2,2,4)
    plt.title('Medidas Descritivas dos crimes violentos letais intencionais')
    plt.axis('off')
    plt.text(0.1,0.9,f'A média dos crimes violentos letais intencionais é {media_cvli:.0f}',fontsize=12)
    plt.text(0.1,0.8,f'A mediana dos crimes violentos letais intencionais é {mediana_cvli:.0f}',fontsize=12)
    plt.text(0.1,0.7,f'A distância entre a média e a mediana é dos crimes violentos letais intencionais é {distancia_cvli}',fontsize=12)
    plt.text(0.1,0.6,f'O menor valor dos crimes violentos letais intencionais é {minimo_cvli:.0f}',fontsize=12)
    plt.text(0.1,0.5,f'O maior valor dos crimes violentos letais intencionais é {maximo_cvli:.0f}',fontsize=12)
    plt.text(0.1,0.4,f'A amplitude dos valores dos crimes violentos letais intencionais é {amplitude_cvli:.0f}',fontsize=12)
    plt.text(0.1,0.3,f'O valor do q3 - 75% dos crimes violentos letais intencionais é {q3_cvli:.0f}',fontsize=12)
    plt.text(0.1,0.2,f'O valor do iqr = q3 - q1 dos crimes violentos letais intencionais é {iqr_cvli:.0f}',fontsize=12)
    plt.text(0.1,0.1,f'O limite superior dos crimes violentos letais intencionais é {limite_superior_cvli:.0f}',fontsize=12)
else:
    # Posição 01: Gráfico dos crimes violentos letais intencionais
    df_cvli_order = df_cvli.sort_values(by='cvli',ascending=True)
    plt.subplot(2,2,1)
    plt.title('Acumulado dos Valores dos crimes violentos letais intencionais')
    plt.bar(df_cvli_order['aisp'].astype(str),df_cvli_order['cvli'])

    # Posição 02: Histograma dos crimes violentos letais intencionais
    plt.subplot(2,2,2)
    plt.title('Histograma dos crimes violentos letais intencionais')
    plt.hist(array_cvli,bins=100,edgecolor='black')

    # Posição 03: Medidas Descritivas dos crimes violentos letais intencionais
    plt.subplot(2,2,3)
    plt.title('Medidas Descritivas dos crimes violentos letais intencionais')
    plt.axis('off')
    plt.text(0.1,0.9,f'A média dos crimes violentos letais intencionais é {media_cvli:.0f}',fontsize=12)
    plt.text(0.1,0.8,f'A mediana dos crimes violentos letais intencionais é {mediana_cvli:.0f}',fontsize=12)
    plt.text(0.1,0.7,f'A distância entre a média e a mediana é dos crimes violentos letais intencionais é {distancia_cvli}',fontsize=12)
    plt.text(0.1,0.6,f'O menor valor dos crimes violentos letais intencionais é {minimo_cvli:.0f}',fontsize=12)
    plt.text(0.1,0.5,f'O maior valor dos crimes violentos letais intencionais é {maximo_cvli:.0f}',fontsize=12)
    plt.text(0.1,0.4,f'A amplitude dos valores dos crimes violentos letais intencionais é {amplitude_cvli:.0f}',fontsize=12)
    plt.text(0.1,0.3,f'Distância entre a Variância e Média dos crimes violentos letais intencionais {distancia_var_cvli:.2f}',fontsize=12)
    plt.text(0.1,0.2,f'Coeficiente de variação dos crimes violentos letais intencionais {coeficiente_var_cvli:.2f}',fontsize=12)

    # Posição 04: Vazio
    plt.subplot(2,2,4)
    plt.axis('off')

# Exibindo o Painel
plt.tight_layout()
plt.show()
