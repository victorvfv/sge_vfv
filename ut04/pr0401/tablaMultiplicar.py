print("dime la base: ")
n=input()
print("Dime cuantas veces quieres multiplicar: ")
k=input()
n=int(n)
k=int(k)

for num in range(k+1):
        o=(n * num)
        print(str(n) +" * "+ str(num) +" = " + str(o) )
        
  
