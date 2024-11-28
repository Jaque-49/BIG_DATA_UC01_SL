#Programa que mostra o uso de listas
nome_01 = "Alessandro, Maria, Eduarda"
nome_02 = ["Alessandro", "Maria", "Eduarda"]
print (nome_01)
print (nome_02)
print(nome_02[1])
print(len(nome_02))
print ("Listagem dos elementos do Vetor")
n=1
for i in range(len(nome_02)):
    print(f"{n}° - {nome_02 [i]}")
    n +=1