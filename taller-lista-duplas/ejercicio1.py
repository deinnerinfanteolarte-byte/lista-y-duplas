print("Ingrese los productos que desea compar, cuando termine la lista escriba: listo")
comprar = []
while True:
    mercado = input("Escribe los productos a comprar: ")
    if mercado.lower() == "listo":
        break
    comprar.append(mercado)


primero = comprar[0]
ultimo = comprar[-1]

total = len(mercado)

print("El primer producto es: ", primero)
print("El ultimo producto es: ", ultimo)
print("La cantidad de productos a comprar es de: ", total)