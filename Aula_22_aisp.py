import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias

df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_recuperacao_veiculos = df_ocorrencias[['aisp','ano','recuperacao_veiculos']]

# Criando o DataFrame recuperação de veículos agrupado pelos anos de 2023 e 2024
df_recuperacao_veiculos = df_recuperacao_veiculos[df_recuperacao_veiculos['ano'].isin([2023,2024])]
df_recuperacao_veiculos = df_recuperacao_veiculos.groupby(['aisp']).sum(['recuperacao_veiculos']).reset_index()


# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_recuperacao_veiculos)

# Criando o array  da recuperacao de veiculos
array_recuperacao_veiculos = np.array(df_recuperacao_veiculos['recuperacao_veiculos'])

# Obtendo a média da recuperacao de veiculos
media_recuperacao_veiculos = np.mean(array_recuperacao_veiculos)

# Obtendo a mediana da recuperacao de veiculos
mediana_recuperacao_veiculos = np.median(array_recuperacao_veiculos)

# Obtendo a distância entre a média e a mediana da recuperacao de veiculos
distancia_recuperacao_veiculos = abs((media_recuperacao_veiculos - mediana_recuperacao_veiculos) / mediana_recuperacao_veiculos)

# Obtendo o máximo e o mínimo da recuperacao de veiculos
maximo_recuperacao_veiculos = np.max(array_recuperacao_veiculos)
minimo_recuperacao_veiculos = np.min(array_recuperacao_veiculos)

# Obtendo a amplitude da recuperacao de veiculos
amplitude_recuperacao_veiculo = maximo_recuperacao_veiculos - minimo_recuperacao_veiculos

# Obtendo os Quartis da recuperacao de veiculos - Método weibull
q1_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.25, method='weibull')
q2_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.50, method='weibull')
q3_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.75, method='weibull')
iqr_recuperacao_veiculos = q3_recuperacao_veiculos - q1_recuperacao_veiculos

# Identificando os outliers superiores e inferiores da recuperacao de veiculos
limite_superior_recuperacao_veiculos = q3_recuperacao_veiculos + (1.5 * iqr_recuperacao_veiculos)
limite_inferior_recuperacao_veiculos = q1_recuperacao_veiculos - (1.5 * iqr_recuperacao_veiculos)

# Filtrando o DataFrame da recuperacao de veiculos
df_recuperacao_veiculos_outliers_superiores = df_recuperacao_veiculos[df_recuperacao_veiculos['recuperacao_veiculos'] > limite_superior_recuperacao_veiculos]
df_recuperacao_veiculos_outliers_inferiores = df_recuperacao_veiculos[df_recuperacao_veiculos['recuperacao_veiculos'] < limite_inferior_recuperacao_veiculos]


# Exibindo os dados da recuperacao de veiculos
print("\n--------- OBTENDO INFORMAÇÕES da recuperacao de veiculos -----------")
print(f"A média dos recuperação de veículos é {media_recuperacao_veiculos:.0f}")
print(f"A mediana de recuperação de veículos  é {mediana_recuperacao_veiculos:.0f}")
print(f"A distância entre a média e a mediana da recuperação de veículos é {distancia_recuperacao_veiculos}")
print(f"O menor valor da recuperação de veículos é {minimo_recuperacao_veiculos:.0f}")
print(f"O maior valor da recuperação de veículos é {maximo_recuperacao_veiculos:.0f}")
print(f"A amplitude da recuperação de veículoss é {amplitude_recuperacao_veiculo:.0f}")
print(f"O valor do q1 - 25% da recuperação de veículos é {q1_recuperacao_veiculos:.0f}")
print(f"O valor do q2 - 50% da recuperação de veículos é {q2_recuperacao_veiculos:.0f}")
print(f"O valor do q3 - 75% da recuperação de veículos é {q3_recuperacao_veiculos:.0f}")
print(f"O valor do iqr = q3 - q1 da recuperação de veículos é {iqr_recuperacao_veiculos:.0f}")
print(f"O limite inferior da recuperação de veículos é {limite_inferior_recuperacao_veiculos:.0f}")
print(f"O limite superior da recuperação de veículos é {limite_superior_recuperacao_veiculos:.0f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_recuperacao_veiculos_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_recuperacao_veiculos_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_recuperacao_veiculos_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_recuperacao_veiculos_outliers_superiores)

# Visualizando os dados  da recuperação de veículos
print("\nVISUALIZANDO OS DADOS...")
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados da recuperação de veículos')

# Posição 01: Gráfico dos roubos carga
plt.subplot(2,2,1)
plt.title('BoxPlot  da recuperação de veículos')
plt.boxplot(array_recuperacao_veiculos,vert=False,showmeans=True)

# Posição 02: Histograma da recuperação de veículos
plt.subplot(2,2,2)
plt.title('Histograma dos roubos de cargas')
plt.hist(array_recuperacao_veiculos,bins=100,edgecolor='black')

# Posição 03: Lista da recuperação de veículos
df_recuperacao_veiculos_outliers_superiores_order = df_recuperacao_veiculos_outliers_superiores.sort_values(by='recuperacao_veiculos',ascending=True)
plt.subplot(2,2,3)
plt.title('Ranking da recuperacao de veiculos com Outliers Superiores')
plt.barh(df_recuperacao_veiculos_outliers_superiores_order['aisp'].astype(str),df_recuperacao_veiculos_outliers_superiores_order['recuperacao_veiculos'])


# Posição 04: Medidas Descritivas da recuperacao de veiculos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas da recuperacao de veiculos')
plt.axis('off')
plt.text(0.1,0.9,f'A média da recuperacao de veiculos é {media_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.8,f'A mediana da recuperacao de veiculos é {mediana_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.7,f'A distância entre a média e a mediana da recuperacao de veiculos é {distancia_recuperacao_veiculos}',fontsize=12)
plt.text(0.1,0.6,f'O menor valor da recuperacao de veiculos é {minimo_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.5,f'O maior valor da recuperacao de veiculosé {maximo_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.4,f'A amplitude dos valores da recuperacao de veiculos é {amplitude_recuperacao_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.3,f'O valor do q3 - 75% da recuperacao de veiculos é {q3_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.2,f'O valor do iqr = q3 - q1 da recuperacao de veiculos é {iqr_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.1,f'O limite superior da recuperacao de veiculos é {limite_superior_recuperacao_veiculos:.0f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()
