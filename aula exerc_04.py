#
soma = 0#
media = 0#
nota1 = 0#
nota2 = 0#
for i in range(2):
    nome = input("Infome o nome:")
    nota1 = float(input("informe a nota 1:"))
    nota2 = float(input("informe a nota 2:"))
    media = (nota1 + nota2) / 2
    if media >= 70:
        soma = soma + (nota1 + nota2)#
        media = soma / (i + 1)#
        print("ATENDIDO")
    elif media >= 30 and media < 70: # n precisa < 70
        print("PARCIALMENTE ATENDIDO")
    else:
      print("N ATENDIDO")