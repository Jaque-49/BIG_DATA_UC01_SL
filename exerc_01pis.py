def pode_doar_sangue(idade, peso, horas_de_sono):
    if 16 <= idade <= 69 and peso > 50 and horas_de_sono >= 6:
        return "Você pode doar sangue!"
    else:
        return "Você não pode doar sangue."

# Solicitando informações do usuário
idade = int(input("Qual é a sua idade? "))
peso = float(input("Qual é o seu peso em kg? "))
horas_de_sono = float(input("Quantas horas você dormiu nas últimas 24 horas? "))

# Verificando se a pessoa pode doar sangue
resultado = pode_doar_sangue(idade, peso, horas_de_sono)
print(resultado)