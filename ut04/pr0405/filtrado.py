numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Par(numero):
    return numero %2==0

numerosPares = list(filter(Par,numeros))
print(numerosPares)