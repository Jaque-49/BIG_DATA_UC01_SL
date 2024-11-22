#Nome e as duas notas de um aluno
n = input("Informe o seu nome")
n1 = float(input("Insira a nota 1:"))
n2 = float(input("Insira a nota 2:"))
media = (n1 + n2) / 2
if media >= 70:
    print (f"Sr(a) {n}, você está aprovado!")
elif media >= 30:
     print (f"Sr(a) {n}, você está em recuperação cabeção!")
else:
    print (f" Sr(a) {n}, você está reprovado!")