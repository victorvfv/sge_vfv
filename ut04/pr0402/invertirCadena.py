def invertir(param1):
    c=len(param1)
    n=[]
    for num in range (c):
        n.append(param1[num])
    
    n.reverse()
    b="".join(n)
    print(b)

invertir("rotciv se erbmon im")