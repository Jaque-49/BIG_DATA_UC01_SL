# Importando a Biblioteca Pandas e Numpy
import pandas as pd
import numpy as np

# Importando a Base de Dados
endereco_dados = 'Bases\Titanic.csv'

# Criando o DataFrame Ocorrências
df_passageiros = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')

# Criando um array do Fare
array_passageiros_fare = np.array(df_passageiros['Fare'])

# Criando um array da Age
array_passageiros_age = np.array(df_passageiros['Age'])

# Criando um array da Ticket
array_passageiros_ticket = np.array(df_passageiros['Ticket'])

# Obtendo os resultados solicitados Fare
media_fare = np.mean(array_passageiros_fare)
maior_fare = np.max(array_passageiros_fare)
menor_fare = np.min(array_passageiros_fare)
mediana_fare = np.median(array_passageiros_fare)
distancia_fare = abs((media_fare - mediana_fare) / mediana_fare)
amplitude_fare = maior_fare - menor_fare

# Obtendo os resultados solicitados Age
media_age = np.mean(array_passageiros_age)
mediana_age = np.median(array_passageiros_age)
media_age = np.mean(array_passageiros_age)
maior_age = np.max(array_passageiros_age)
menor_age = np.min(array_passageiros_age)
distancia_age = abs((media_age - mediana_age) / mediana_age)
amplitude_age = maior_age - menor_age

# Exibindo o DataFrame Fare
print("------- Tabela Tarifas ------")
print(f"A média das tarifas dos passageiros do Titanic é {media_fare:.0f}.")
print(f"A mediana das tarifas dos passageiros do Titanic é {mediana_fare:.0f}.")
print(f"A maior tarifa dos passageiros do Titanic é {maior_fare:.0f}.")
print(f"A menor tarifa dos passageiros do Titanic é {menor_fare:.0f}.")
print(f"A distância entre a média e a mediana das tarifas é {distancia_fare:.0f}.")
print(f"A amplitude das tarifas é {amplitude_fare:.0f}.")

#Exibindo o DataFrame Age
print("------- Tabela Idades Passageiros ------")
print(f"A média das idades dos passageiros do Titanic é {media_age:.0f}.")
print(f"A mediana das idades dos passageiros do Titanic é {mediana_age:.0f}.")
print(f"A maior idade dos passageiros do Titanic é {maior_age:.0f}.")
print(f"A menor idade dos passageiros do Titanic é {menor_age:.0f}.")
print(f"A distância entre a média e a mediana das idades é {distancia_age:.0f}.")
print(f"A amplitude das idades é {amplitude_age:.0f}.")
