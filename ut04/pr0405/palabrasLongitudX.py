palabras = ["perro", "gato", "elefante", "oso", "jirafa"]

def longitudX (elemento):
    return  len(elemento)>5

palabrasLongitudX = list(filter(longitudX,palabras))

palabrasLongitudX =list(map(lambda x: x.swapcase(),palabrasLongitudX))
print(palabrasLongitudX)