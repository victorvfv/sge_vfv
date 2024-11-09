def sumarLista(param1):
    salida=int(0)
    for elem in param1:
        salida+=elem
    return salida

def contarElemento(param1,param2):
    i=param1.count(param2)
    print(i)

def mayorMenor(param1):
    param1.sort()
    mayor=param1[-1]
    menor=param1[1]
    print ("el numero mas grande es: " + str(mayor) + " el numero mas pqueño es: " + str(menor))

def filtrarPares(param1):
    lista=[]
    for elem in param1:
        if(elem%2==0):
            lista.append(elem)
    print(lista)

def ConcatenarListas(param1,param2):
    lista=[]
    rango=len(param2)
    if (len(param1)>rango):
        rango=len(param1)

    for i in range(rango):

        if(i<len(param1)):
            lista.append(param1[i])

        if(i<len(param2)):
            lista.append(param2[i])
    print(lista)

def Dividir(param1):
    mayor=[]
    menor=[]
    media =sumarLista(param1)/len(param1)
    print(media)
    for i in param1:
        if (i>=media):
            mayor.append(i)
        else:
            menor.append(i)
    print(mayor)
    print(menor)
    
def ListaDeListas():
    matriz=[[1,2,3],[2,3,1],[3,1,2]]
    for elemento in matriz:
        
        print(elemento)
    i=1
    for elemento in matriz:
        
        print("la suma de la " + str(i) + " fila es: "+str(sumarLista(elemento)))
        i+=1
    


ListaDeListas()