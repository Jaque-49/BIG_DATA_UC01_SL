#Conectivos
n = input("Digite o seu nome:")
s = input("Sexo:")
i = int(input("Qual a sua idade?"))
if (i >= 18) and (s == "M" or s == "m"):
    CERIFICAD = int(input("Informe o certificado de reservista"))
elif i >= 18:
     print("você é maior de idade")
else:
    print("você é menor de idade")