def generar_fibonacci(n):
    secuencia = [1, 1]
    
    
    for i in range(2, n):
        siguiente_numero = secuencia[i - 1] + secuencia[i - 2]
        secuencia.append(siguiente_numero)
    
    return secuencia

n = 200  
print(generar_fibonacci(n))