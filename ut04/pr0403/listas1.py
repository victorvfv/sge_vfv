nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]

def Ordenar():
    nombres.sort()
    nombres.reverse()
    print (nombres)

def encontrar(param1):
    if(nombres.count(param1)!=0):
        print("El nombre "+param1+ " se encuentra en la posicion " + str(nombres.index(param1)))
    else:
        print("El nombre "+param1+ " no exixte ")

def primerosElemt(param1):
    i=nombres.index(param1)+1
    print(nombres[:i])

def getNumVocales():
    a=0
    e=0
    i=0
    o=0
    u=0
    for palabra in nombres:
        a+=palabra.lower().count("a")
        e+=palabra.lower().count("e")
        i+=palabra.lower().count("i")
        o+=palabra.lower().count("o")
        u+=palabra.lower().count("u")

    print("hay "+str(a)+ " a, hay " + str(e) + " e, hay " + str(i)+ " i, hay " + str(o) + " o, hay " + str(u) +  " u ")

def nombresCortos():
    for palabras in nombres:
        i = len(palabras)
        if(i<=4):
            print(palabras)

def NnombresLongitud(param1):
    salida=int(0)
    for palabras in nombres:
        i= len(palabras)
        if(i==param1):
            salida+=1
    print("Hay: "+ str(salida) + " nombres con: "+ str(param1) +" caracteres.")


primerosElemt(input())