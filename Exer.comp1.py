#salário
HT = float(input ("Informe as horas trabalhadas no mês:"))
VH = float(input("Insira o valor da hora trabalhada:"))

PD = float(input("Insira o percentual de desconto:"))
SB= HT*VH
DES = (PD/100)
SL = SB - DES
print(f" Sálário líquido do funcionário é:{SL: .2f}")