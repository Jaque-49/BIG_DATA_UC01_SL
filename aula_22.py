#Programa para calcular a velocidade média
cm = 12
d = float(input("Informe a distância percorrida (KM):"))
t = float(input("Informe o tempo da viagem (horas):"))
vm = d / t
l = d / cm
print (f" A velocidade média do veículo foi {vm} km/h.")
print (f" A quantidade gasta de combustível foi {l} litros.")