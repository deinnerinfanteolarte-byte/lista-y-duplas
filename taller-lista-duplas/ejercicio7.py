"""
El IDEAM registra N temperaturas en un municipio. Se desea calcular la temperatura media y
determinar, entre todas las temperaturas registradas, cuántas son superiores o iguales a esa media.
También se quiere ver cuáles son.
"""

n = int(input("Ingrese la cantidad de temperaturas registradas: "))
temperaturas = []
suma = 0

for i in range(n):
    temp = float(input(f"Ingrese la temperatura #{i + 1}: "))
    temperaturas.append(temp)

    suma += temp


media = suma / len(temperaturas)

superiores = []

for temp in temperaturas: 
    if temp >= media:
        superiores.append(temp)

print(f"cantidad de temperatura superior o igual a media es: {len(superiores)}")
print(f"cuales son: {superiores}")

    