#Programa para traa erro de entrada de dados
idade = 0
maior_idade = 0
feminino_18_35 = 0 
olhos_verdes_cabelos_louros = 0
sexo = 0
for i in range(2):
    idade = int(input("Digite a sua idade:"))
    sexo = input("Digite o sexo (masculino ou feminino):")
    olhos = input("Digite a cor dos olhos (azuis,verdes ou castanhos) :")
    cabelos = input("Digite a cor do seu cabelo (louros,castanhos ou pretos):")
    if idade > maior_idade: 
        maior_idade = idade
    if sexo == "feminino" and 18 <= idade <= 35:
        feminino_18_35 += 1
    if olhos == "verdes" and cabelos == "louros": 
        olhos_verdes_cabelos_louros += 1
print(f"A maior idade dos habitantes é: {maior_idade}") 
print(f"A quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos é: {feminino_18_35}") 
print(f"A quantidade de indivíduos que têm olhos verdes e cabelos louros é: {olhos_verdes_cabelos_louros}")