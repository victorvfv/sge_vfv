def removeChar(param1):
    list=[]
    iter=[]
    cadena=param1
    for char in cadena:
        list.append(char)
        iter.append(char)

    list.reverse()

    for char in iter: 
        if list.count(char)>=2:
            list.remove(char)
        
    list.reverse()

    salida="".join(list)
    print(salida)

removeChar(input())