# Diccionario de productos por categoría
productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}

numCategorias = len(productos)
print(f"Hay {numCategorias} categorías.")

totalProductos = 0
for categoria, items in productos.items():
    cantidad = len(items)
    totalProductos += cantidad
    print("Categoría "+ categoria + " tiene " + str(cantidad) +" productos.")

print(f"En total hay " + str(totalProductos) + " productos.")