#
while True: #infinito (atender uma solicitação do cliente para que se tiver um erro ele retorne para que o usuário digite novamente)
    try: 
        n1 = (int(input("fornecer o número 1:")))
        n2 = (int(input("fornecer o número 2:")))
        divisao = n1 / n2
    except ZeroDivisionError:
        print("Verifique o segundo valor digitado, pois ele não pode ser zero")
    else:
        print(f"O resultado da divisão é {divisao}")
        break