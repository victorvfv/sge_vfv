## Ejercicios basicos

## Lectura de un número válido
Crea un programa que solicite un número por pantalla al usuario y siga pidiéndolo hasta que el usuario introduzca un número válido.

´´´Python 

import random

def numeroValido():
    x= random.randint(1,100000)
    y=""
    while(y!=x):
        print("dime el numero: " + str(x))
        y=int(input())
    print("muchas gracias")

numeroValido()

´´´Python 

## Tabla de multiplicar
Crea un programa que solicite un número n y un valor k y que muestre por la terminal los primeros k elementos de la tabla de multiplicar de n.

´´´Python 

print("Dime el tamaño de la base: ")
k=input()
k=int(k)

for num in range(1,k+1):
   
    print("*"*num)

´´´Python 

## Triángulo de asteriscos
Crea un programa que solicite un número al usuario y dibuje un triángulo con asteriscos cuya base sea el número introducido.

Ejemplo: si el número introducido es 5 el resultado será:

´´´Python 

print("Dime el tamaño de la base: ")
k=input()
k=int(k)

for num in range(1,k+1):
   
    print("*"*num)

´´´Python 

##  Pirámide de asteriscos
Modifica el programa anterior para que en lugar de crear un triángulo cree una pirámide. Si el usuario introduce un número par se lo volverá a pedir hasta que introduzca un número par.

Ejemplo: si el número introducido es 9 el resultado será:

´´´Python

k=int(input(("Dime el tamaño de la base(tiene que ser inpar): ")))
t=True
while(t):
    if((k%2)==0):
        print("ha de ser inmpar")
        k=int(input())
    else:
        t=False

for i in range(1,k+1,2):
    espacios=(k-i)//2
    print(" " * espacios + "*" * i)

´´´Python

##  Número mayor y menor
Crea un programa que pida al usuario que introduzca 5 números y luego le diga cuál es el mayor y el menor de todos ellos de la forma: El número mayor es "mayor" y el menor es "menor"

´´´Python

i=int(0)

mayor=int(0)
menor=int(0)
while(i<5):
    print("introduce un numero")
    k=int(input())
    i=i+1
    if k>mayor:
        mayor=k
        
    if k<menor or menor==0:
        menor=k
   
print("El número mayor es "+str(mayor) + " y el menor es " + str(menor))

´´´Python

## Acierta el número
Crea un programa que genere un número aleatorio entre 0 y 100 y el usuario tenga que adivinarlo. Cada vez que el usuario introduzca un número el programa le dirá si el número es más alto o más bajo.

Para generar un número aleatorio puedes utilizar la función randint(a, b) que devuelve un entero aleatorio entre a y b. Para poder utilizar esta función antes tienes que importar la librería con la orden from random import *

´´´Python

from random import *

k=randint(1,1000)
t=True
print("Introduce un numero a ver si aciertas")
while(t):
    n=int(input())
    if(n==k):
        print("acertaste")
        t=False
    elif(n<k):
        print("el numero es mas grande")
        print("vuelve a intentarlo")
    else:
        print("el numero es mas pequeño")
        print("vuelve a intentarlo")

´´´Python

## Piedra, papel o tijeras
Crea un programa que implemente el clásico juego de piedra, papel, tijeras, lagarto y spock.

´´´Python

from random import *

m=int(0)
u=int(0)
num=int(0)
b=True
while(b):
    k=randint(1,5)
    
    if (k==1):
        jm="piedra"
    elif(k==2):
        jm="lagarto"
    elif(k==3):
        jm="spock"
    elif(k==4):
        jm="papel"
    elif(k==5):
        jm="tijeras"
    
    t=True
    while(t):
        ju=input("Dime tu jugad piedra, papel, tijeras, lagarto o spock? ")
        if(ju=="piedra" or ju=="papel" or ju=="tijeras" or ju=="lagarto" or ju=="spock"):
            t=False
        else:
            print("di una jugada valida")
    
    if(ju==jm):
        print("emapte ambos habeis jugado " + jm)

    elif(ju=="piedra" and jm=="lagarto"):
        print("ganaste la maquina uso " +jm )
        u+=1

    elif(ju=="piedra" and jm=="tijeras"):
        print("ganaste la maquina uso " +jm )
        u+=1

    elif(ju=="lagarto" and jm=="spock"):
        print("ganaste la maquina uso " +jm )
        u+=1

    elif(ju=="lagarto" and jm=="papel"):
        print("ganaste la maquina uso " +jm )
        u+=1

    elif(ju=="spock" and jm=="tijeras"):
        print("ganaste la maquina uso " +jm )
        u+=1
    elif(ju=="spock" and jm=="piedra"):
        print("ganaste la maquina uso " +jm )
        u+=1

    elif(ju=="tijeras" and jm=="papel"):
        print("ganaste la maquina uso " +jm )
        u+=1
    elif(ju=="tijeras" and jm=="lagarto"):
        print("ganaste la maquina uso " +jm )
        u+=1

    elif(ju=="papel" and jm=="piedra"):
        print("ganaste la maquina uso " +jm )
        u+=1

    elif(ju=="papel" and jm=="spock"):
        print("ganaste la maquina uso " +jm )
        u+=1


    elif(ju=="piedra" and jm=="papel"):
        print("perdiste la maquina uso " +jm )
        m+=1

    elif(ju=="piedra" and jm=="spock"):
        print("perdiste la maquina uso " +jm )
        m+=1

    elif(ju=="lagarto" and jm=="piedra"):
        print("perdiste la maquina uso " +jm )
        m+=1

    elif(ju=="lagarto" and jm=="tijeras"):
        print("perdiste la maquina uso " +jm )
        m+=1

    elif(ju=="spock" and jm=="lagarto"):
        print("perdiste la maquina uso " +jm )
        m+=1
    
    elif(ju=="spock" and jm=="papel"):
        print("perdiste la maquina uso " +jm )
        m+=1

    elif(ju=="spock" and jm=="lagarto"):
        print("perdiste la maquina uso " +jm )
        m+=1

    elif(ju=="tijeras" and jm=="piedra"):
        print("perdiste la maquina uso " +jm )
        m+=1

    elif(ju=="tijeras" and jm=="spock"):
        print("perdiste la maquina uso " +jm )
        m+=1

    elif(ju=="papel" and jm=="lagarto"):
        print("perdiste la maquina uso " +jm )
        m+=1

    elif(ju=="papel" and jm=="tijeras"):
        print("perdiste la maquina uso " +jm )
        m+=1

    else:
        print("has usado " + ju + " la maquina ha usado " + jm)

    print()
    if(m==5):
        b=False
    elif(u==5):
        b=False
    print("marcadores: jugador " + str(u) + " maquina " + str(m) )

if(m==5):
    print("perdite")
else:
    print("ganaste")
    

´´´Python

## Secuencia de Fibonacci
Crea un programa que genere los primeros n números de la secuencia de Fibonacci. Recuerda que la secuencia de Fibonacci es:

´´´Python

def generar_fibonacci(n):
    secuencia = [1, 1]
    
    
    for i in range(2, n):
        siguiente_numero = secuencia[i - 1] + secuencia[i - 2]
        secuencia.append(siguiente_numero)
    
    return secuencia

n = 200  
print(generar_fibonacci(n))

´´´Python