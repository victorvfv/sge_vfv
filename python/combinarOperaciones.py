from functools import reduce

numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]

def positivo(numero):
    return numero>0

iter= list(reduce(lambda x,valor: x + list(filter(positivo,valor)) ,numeros, []))
suma= reduce(lambda acc,valor: acc+valor,iter)
print(suma)
