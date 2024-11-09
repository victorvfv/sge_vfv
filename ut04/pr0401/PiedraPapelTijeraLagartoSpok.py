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
    
    