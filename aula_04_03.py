#Programa que realiza a soma dentre 5 números inteiros e fornece o maior
soma = 0
maior = 0
for i in range(5):
    #inicio do bloco
    num = int(input("informe o valor:"))
    if num > maior:
        maior = num
    soma = soma + num #acumulador
    # fim do bloco
print (f"o Resultado da soma é: {soma}") 
print (f"o maior numero encontrado é: {maior}") 