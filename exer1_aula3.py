#Programa para calcular idade e peso
nome = input( "Qual o seu nome:" )
idade = int(input("Qual a sua idade?"))
peso = float(input("Qual o seu peso?"))
sono = int(input("Quanto dormiu nas última 24h?"))
if (idade >=16) or (idade <=69):
    if (peso >= 50):
        if (sono >=6):
            print ("Vc pode doar sangue")
else:
    print(f"{nome}Você não pode doar sangue")