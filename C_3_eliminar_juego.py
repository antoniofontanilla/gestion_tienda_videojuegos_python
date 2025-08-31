from A_1_ingresar_videojuego import juegos
def eliminar_juego(juegos):
    if not juegos:
         print("No hay datos en la lista")
         return
    for idx, datos in enumerate(juegos, start=1):
            print(f"{idx}- {datos['nombregame']}")
    juego_para_eliminar = int(input("Que juego desea eliminar: "))
    try:
        if juego_para_eliminar < 1 or juego_para_eliminar > len(juegos):
            print("Opción fuera de rango.")
            return 
        juego = juegos[juego_para_eliminar -1]
        print(f"Has seleccionado: {juego['nombregame']}")
        del juegos[juego_para_eliminar - 1]
        print("Juego eliminado con éxito.")

    except ValueError:
         print("Error, menú inválido")