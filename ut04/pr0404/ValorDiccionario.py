frutas = {
    "manzana": 1.20,
    "banana": 0.50,
    "cereza": 2.00,
    "naranja": 0.80,
    "uva": 3.00
}

frutaBuscada = input("Ingrese el nombre de una fruta: ").lower()

print(f"El precio de "+ frutaBuscada + " es " + str(frutas.get(frutaBuscada,"no esta")) )
