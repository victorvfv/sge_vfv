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