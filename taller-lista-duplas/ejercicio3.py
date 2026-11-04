# Pedir los datos de la camper
codigo = input("Código: ")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
dia = int(input("Día de nacimiento: "))
mes = int(input("Mes de nacimiento: "))
anio = int(input("Año de nacimiento: "))

# Construir las tuplas (inmutables)
fecha_nacimiento = (dia, mes, anio)
camper = (codigo, nombre, apellido, fecha_nacimiento)

# 1. Nombre completo
print("\nNombre completo:", camper[1], camper[2])

# 2. Año de nacimiento
print("Año de nacimiento:", camper[3][2])

# 3. Cantidad de elementos de la tupla del registro
print("Elementos en el registro:", len(camper))

# 4. Cuarto elemento de la tupla (índice 3)
print("Cuarto elemento:", camper[3])