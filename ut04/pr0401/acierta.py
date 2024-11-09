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
