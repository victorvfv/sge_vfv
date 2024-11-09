def palindromo(param1):
    c=len(param1)
    n=[]
    for num in range (c):
        n.append(param1[num])
    
    n.reverse()
    b="".join(n)
    if (b==param1):
        print("es un palindromo")
    else:
        print("no es un palindromo")

palindromo("ana")