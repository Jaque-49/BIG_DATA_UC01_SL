#Qual o número maior dos três números
n1 = int(input("Digie o primeiro número:"))
n2 = int(input("Digie o segundo número:"))
n3 = int(input("Digie o terceiro número:"))
if n1 > n2 and n1 > n3: 
    print("O primeiro número é maior:") 
elif n2 > n1 and n2 > n3:
     print("O segundo número é maior:")   
else:
     print(" O terceiro número é maior:")