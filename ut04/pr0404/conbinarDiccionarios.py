def combinarDiccionarios(param1, param2):
    combinado = param1  
    for producto, precio in param2.items():
        if producto in combinado:
            combinado[producto] += precio 
        else:
            combinado[producto] = precio 
    print (combinado)




combinarDiccionarios({"manzana": 1.20, "banana": 0.50, "pera": 1.50}, {"banana": 0.30, "pera": 1.20, "naranja": 0.80})
