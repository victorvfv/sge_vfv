## Ejercicios de programación funcional

## 1.- Filtrado de una lista de números
Usa filter para obtener solo los números pares de una lista de enteros.

```python  

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Par(numero):
    return numero %2==0

numerosPares = list(filter(Par,numeros))
print(numerosPares)

``` 

## 2.- Mapeo de temperaturas
Dada una lista de temperaturas en Celsius, usa map para convertirlas a Fahrenheit.

```python 

celsius = [0, 20, 37, 100]
fahrenheit= list(map(lambda x:(x*9/5)+32,celsius))
print(fahrenheit)

``` 

## 3.- Suma acumulativa
Utiliza reduce para obtener la suma acumulativa de una lista de números.

```python 

from functools import reduce
numeros = [1, 2, 3, 4, 5]

suma_Acumulativa = reduce(lambda acc, valor: acc + valor, numeros)
print(suma_Acumulativa)

```

## 4.- Palabras con cierta longitud
Dada una lista de palabras, usa filter para encontrar las que tienen más de cinco letras y luego map para convertirlas en mayúsculas.

```python 

palabras = ["perro", "gato", "elefante", "oso", "jirafa"]

def longitudX (elemento):
    return  len(elemento)>5

palabrasLongitudX = list(filter(longitudX,palabras))

palabrasLongitudX =list(map(lambda x: x.swapcase(),palabrasLongitudX))
print(palabrasLongitudX)

```

## 5.- Multiplicación de pares
Dada una lista de números, utiliza filter, map y reduce para obtener el producto de los números pares.

```python 

from functools import reduce
numeros = [1, 2, 3, 4, 5, 6]

def Par(numero):
    return numero %2==0
numerosPares = list(filter(Par,numeros))

multiplos = reduce(lambda acc, valor: acc*valor,numerosPares)

print(multiplos)

```

## 6.- Combinar operaciones en listas anidadas
Dada una lista de listas de enteros, usa map, filter, y reduce para obtener la suma de todos los números positivos.

```python 

from functools import reduce

numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]

def positivo(numero):
    return numero>0

iter= list(reduce(lambda x,valor: x + list(filter(positivo,valor)) ,numeros, []))
suma= reduce(lambda acc,valor: acc+valor,iter)
print(suma)

```