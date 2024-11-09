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
