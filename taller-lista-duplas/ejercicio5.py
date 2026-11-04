n = int(input("¿Cuantas letras? "))
letras = []

for i in range(1, n + 1):
    letra = input(f"Letra #{i}:")
    letras.append(letra)

vocales = ["a", "e", "i", "o", "u"]

for vocal in vocales:
    print(f"Cantidad vocal {vocal}= {letras.count(vocal)}")