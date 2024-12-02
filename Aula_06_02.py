#Programa para traa erro de entrada de dados
nome = input("Informe o seu nome:")
while True:
    Sexo = input("Digite o sexo (M ou F):")
    if Sexo == "M" or Sexo == "F":
        break
    else:    
        print("Informe apenas M ou F para o sexo")
while True:
    try:
        Idade = int(input("Digite a sua idade:"))
    except ValueError:  
        print("Verifique se o campo foi preenchido com corretamente com números")
    else:
        print(f" Seja bem-Vindojaque {nome}")
        break      
