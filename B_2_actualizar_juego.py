from A_1_ingresar_videojuego import juegos;

def actualizar_juego(juegos):
    while True: 
        print()
        for idx, datos in enumerate(juegos, start=1):
            print(f"{idx}- {datos["nombregame"]}")
        entrada = input("\nQue juego desea actualizar?: ")
        try:
            if not entrada:
                print("Este campo no puede estar vacio")
                continue
            if not entrada.isdigit():
                print("Solo se aceptan numeros")
                continue
            opcion = int(entrada)
            juego = juegos[opcion -1]
            print(f"Has seleccionado: {juego['nombregame']}")

            print("\n¿Qué deseas actualizar?")
            print("1 - Todo")
            print("2 - Solo género")
            print("3 - Solo precio")
            seleccion = int(input("Opción: "))
            if seleccion == 1:
                nuevo_nombre = input("Nombre: ")
                juego['nombregame'] = nuevo_nombre
                nuevo_genero = input("Genero: ")
                juego['genero'] = nuevo_genero
                nuevo_precio = int(input("Precio: "))
                juego['precio'] = nuevo_precio
                print("juego actualizado")
                print(f"{idx}- {datos["nombregame"]} | {datos["genero"]} | {datos["precio"]}")
                break
            elif seleccion == 2:
                genero_nuevo = input("Genero: ")
                juego['genero'] = genero_nuevo
                print("Genero actualizado")
                print(f"{idx}- {datos["nombregame"]} | {datos["genero"]} | {datos["precio"]}")
                break
            elif seleccion == 3:
                precio_nuevo = int(input("Precio: "))
                juego['precio'] = precio_nuevo
                print("precio actualizado")
                print(f"{idx}- {datos["nombregame"]} | {datos["genero"]} | {datos["precio"]}")
                break

                                                                
        except ValueError:
            print("ERROR!!")
            




    