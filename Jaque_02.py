#Programa Prestação em Atraso
num1 = float(input("Prestação:"))
num2 = float(input("Taxa:"))
num3 = int(input("dias:"))
Valorfinal=num1+(num1*(num2/100)*num3)
print(f"valor final para pagamento:{Valorfinal: .2f}")