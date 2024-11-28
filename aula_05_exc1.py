#
numeros = [10,30,40,60,15,33,80,12,74,52]
qtd_par = 0
qtda_impar = 0
for i in range(len(numeros)):
    if numeros [i] % 2 == 0:
         qtd_par +=1
    else:
         qtda_impar += 1
print(f" A quantidade de números pares é: {qtd_par}")
print(f" A quantidade de números impares é: {qtda_impar}")
print ("Ordem de criação")
print(numeros)
print("Ordem Reversa")
numeros.reverse()
print(numeros)
print("Ordem crescente")
numeros.sort()
print(numeros)



