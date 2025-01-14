import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados Financeira
endereco_dados = 'Bases\Financeira.csv'

# Criando o DataFrame Financeira
df_financeira = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')
df_resumido = df_financeira[['Id_cliente','Renda','Vlr_emprestado']]

# Exibindo a base de dados Financeira
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_financeira)
print(df_resumido.head())

# Criando o array do valor da renda e valor emprestado do cliente
array_renda = np.array(df_resumido['Renda'])
array_valor_emprestado = np.array(df_resumido['Vlr_emprestado'])

# Obtendo a média do valor da renda e do valor emprestado ao cliente
media_renda = np.mean(array_renda)
media_valor_emprestado = np.mean(array_valor_emprestado)

# Obtendo a mediana do valor da renda e do valor emprestado ao cliente
mediana_renda = np.median(array_renda)
mediana_valor_emprestado = np.median(array_valor_emprestado)

# Obtendo o máximo e o mínimo do valor da renda e do valor emprestado ao cliente
maximo_renda = np.max(array_renda)
maximo_valor_emprestado = np.max(array_valor_emprestado)
minimo_renda = np.min(array_renda)
minimo_valor_emprestado = np.min(array_valor_emprestado)

# Obtendo a distância entre a média e a mediana do valor da renda e do valor emprestado ao cliente
distancia_renda = abs((media_renda - mediana_renda) / mediana_renda) * 100
distancia_valor_emprestado = abs((media_valor_emprestado - mediana_valor_emprestado) / mediana_valor_emprestado) * 100

# Obtendo a amplitude do valor da renda e do valor emprestado ao cliente
amplitude_renda = maximo_renda - minimo_renda
amplitude_valor_emprestado = maximo_valor_emprestado - minimo_valor_emprestado


# Obtendo os Quartis da renda e do valor emprestado ao cliente  - Método weibull
q1_renda = np.quantile(array_renda, 0.25, method='weibull')
q2_renda = np.quantile(array_renda, 0.50, method='weibull')
q3_renda = np.quantile(array_renda, 0.75, method='weibull')
iqr_renda = q3_renda - q1_renda

q1_valor_emprestado = np.quantile(array_valor_emprestado, 0.25, method='weibull')
q2_valor_emprestado = np.quantile(array_valor_emprestado, 0.50, method='weibull')
q3_valor_emprestado = np.quantile(array_valor_emprestado, 0.75, method='weibull')
iqr_valor_emprestado = q3_valor_emprestado - q1_valor_emprestado

# Identificando os outliers superiores e inferiores da passagem e da idade
limite_superior_renda = q3_renda + (1.5 * iqr_renda) #50% acima o 1.5
limite_inferior_renda = q1_renda - (1.5 * iqr_renda) #50% abaixo o 1.5

limite_superior_valor_emprestado = q3_valor_emprestado + (1.5 * iqr_valor_emprestado)
limite_inferior_valor_emprestado = q1_valor_emprestado - (1.5 * iqr_valor_emprestado)

# Filtrando o DataFrame titanic
df_renda_outliers_superiores = df_resumido[df_resumido['Renda'] > limite_superior_renda]
df_renda_outliers_inferiores = df_resumido[df_resumido['Renda'] < limite_inferior_renda]

df_valor_emprestado_outliers_superiores = df_resumido[df_resumido['Vlr_emprestado'] > limite_superior_valor_emprestado]
df_valor_emprestado_outliers_inferiores = df_resumido[df_resumido['Vlr_emprestado'] < limite_inferior_valor_emprestado]


# Exibindo os dados sobre o valor da RENDA
print("\n-- OBTENDO INFORMAÇÕES SOBRE A RENDA DOS CLIENTES --")
print(f"\n O valor médio da renda dos clientes é {media_renda:.2f}")
print(f"O valor da mediana da renda dos clientes é {mediana_renda:.2f}")
print(f"A distância entre a média e a mediana das rendas dos clientes  é {distancia_renda:.2f} %")
print(f"O valor mínimo da renda dos clientes é {minimo_renda:.2f}")
print(f"O valor máximo da renda dos clientes  é {maximo_renda:.2f}")
print(f"A amplitude dos valores da renda dos clientes  é {amplitude_renda:.2f}")
print(f"O valor do q1 - 25% do valor da renda dos clientes  é {q1_renda:.2f}")
print(f"O valor do q2 - 50% do valor da renda dos clientes  é {q2_renda:.2f}")
print(f"O valor do q3 - 75% do valor da renda dos clientes  é {q3_renda:.2f}")
print(f"O valor do iqr = q3 - q1 do valor da renda dos clientes  é {iqr_renda:.2f}")
print(f"O limite inferior do valor da renda dos clientes  é {limite_inferior_renda:.2f}")
print(f"O limite superior do valor da renda dos clientes  é {limite_superior_renda:.2f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_renda_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_renda_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_renda_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_renda_outliers_superiores)

# Exibindo os dados sobre o valor da VALOR EMPRESTADO

print("\n-- OBTENDO INFORMAÇÕES SOBRE dos valores emprestados aos clientes --")
print(f"\n Os valores médios emprestados dos clientes é {media_valor_emprestado:.2f}")
print(f"O valor da mediana dos valores emprestados aos clientes é {mediana_valor_emprestado:.2f}")
print(f"A distância entre a média e a mediana dos valores emprestados aos clientes é {distancia_valor_emprestado:.2f} %")
print(f"O valor mínimo  valores emprestados clientes é {minimo_valor_emprestado:.2f}")
print(f"O valor máximo dos valores emprestados clientes  é {maximo_valor_emprestado:.2f}")
print(f"A amplitude dos valores emprestados aos clientes  é {amplitude_valor_emprestado:.2f}")
print(f"O valor do q1 - 25% dos valores emprestados clientes  é {q1_valor_emprestado:.2f}")
print(f"O valor do q2 - 50% dos valores emprestadosclientes  é {q2_valor_emprestado:.2f}")
print(f"O valor do q3 - 75% dos valores emprestados clientes  é {q3_valor_emprestado:.2f}")
print(f"O valor do iqr = q3 - q1 dos valores emprestados  aos clientes  é {iqr_valor_emprestado:.2f}")
print(f"O limite inferior dos valores emprestados aos clientes  é {limite_inferior_valor_emprestado:.2f}")
print(f"O limite superior dos valores emprestados clientes  é {limite_superior_valor_emprestado:.2f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_valor_emprestado_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_valor_emprestado_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_valor_emprestado_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_valor_emprestado_outliers_superiores)