from functools import reduce
numeros = [1, 2, 3, 4, 5, 6]

def Par(numero):
    return numero %2==0
numerosPares = list(filter(Par,numeros))

multiplos = reduce(lambda acc, valor: acc*valor,numerosPares)

print(multiplos)