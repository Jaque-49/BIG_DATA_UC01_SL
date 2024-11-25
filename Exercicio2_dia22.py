#Programa para calcular idade e peso
nome = input( "Qual o seu nome:" )
idade = int(input("Qual a sua idade?"))
peso = float(input("Qual o seu peso?"))
sono = int(input("Quanto dormiu nas última 24h?"))
if 16 <=  idade <= 69 and peso > 50 and sono >= 6:
         print("Você pode doar sangue!")
else:
     print("Você não pode doar sangue.")