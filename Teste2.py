#Temperatura dos finais de semana de um mês
soma = 0
media = 0
n1 = 0
n2 = 0
n3 = 0
for i in range(4):
    n1 = float(input("informe a temperatura da sexta-feira:"))
    n2 = float(input("informe a temperatura da Sabado:"))
    n3 = float(input("informe a temperatura da Domingo:"))
    media = (n1 + n2 + n3) / 3
    if n1 > n2 and n1 > n3:
     print("A primeira temperatura é  maior:") 
    elif  n2 > n1 and n2 > n3:
      print("A segunda temperatura é  maior:")   
    else:
     print(" O terceiro número é maior:")
    print (f"A média das temperaturas:{media}")