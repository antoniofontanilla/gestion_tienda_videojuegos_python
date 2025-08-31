from A_1_ingresar_videojuego import juegos
def imprimir_lista(juegos):
    try:
        print()
        if not juegos:
            print("No hay juegos en la lista")
            return
        for idx, datos in enumerate(juegos, start=1):
            print(f"{idx}- {datos['nombregame']} | {datos['genero']} | {datos['precio']}")
   
    except Exception as a:
        print("Error en {a}")
