#Programa Calcular Idade
import datetime
data_atual=datetime.date.today()
num1 = int(input("Informe o ano de nascimento:"))
ano_atual=data_atual.year
idade = ano_atual - num1
print(f" A sua idade é {idade} anos.")