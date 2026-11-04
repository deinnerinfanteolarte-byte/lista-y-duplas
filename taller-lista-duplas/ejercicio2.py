print("Ingrese las canciones que va a colocar, cuando termine la lista escriba: listo")
lista_canciones = []
while True:
    musica = input("Canciones: ")
    if musica.lower() == "listo":
        break
    lista_canciones.append(musica)


primero = lista_canciones[0:3]
ultimo = lista_canciones[-1:-3:-1]

tercera_cuarta_quinta = lista_canciones[2:5]

print("El primer producto es: ", primero)
print("El ultimo producto es: ", ultimo)
print("La cantidad de productos a comprar es de: ", tercera_cuarta_quinta)