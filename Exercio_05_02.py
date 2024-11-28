#
acertos = 0
erros = 0
#resp = []
#for i in range(5)
   # resp.append(input("informe as alternativas:"))
gabarito = ["A", "B", "B", "D", "E"]
RESPOSTA = ["A","B","C","D","E"]
for i in range(len(RESPOSTA)):
    if RESPOSTA[i] == gabarito[i]:
         acertos +=1
    else:
        erros +=1
print(f"A quantidade de acertos foi: {acertos}")
print(f"A quantidade de erros foi: {erros}")