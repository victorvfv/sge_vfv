from functools import reduce
numeros = [1, 2, 3, 4, 5]

suma_Acumulativa = reduce(lambda acc, valor: acc + valor, numeros)
print(suma_Acumulativa)