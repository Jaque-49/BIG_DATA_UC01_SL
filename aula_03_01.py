#
idade = int(input("Informe a idade:"))
if idade >= 65:
    print("você é maior de idade. Acesso Liberado, aprecie com moderação")
elif idade >= 18:
    print("você é menor de idade. Acesso liberado:")
else:
    print("você é menor de idade. Acesso negado:")