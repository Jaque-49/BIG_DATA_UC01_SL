# código usando listas
import pandas as pd
n1 = pd.Series([10,20,30,40,50,60,70,80,90,100])
n2 = pd.Series([12,25,34,42,53,62,72,85,94,98])
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
print("----Soma---")
print(soma)
print("----Subtração---")
print(sub)
print("----Mult---")
print(mult)
print("----Divisão---")
print(div)