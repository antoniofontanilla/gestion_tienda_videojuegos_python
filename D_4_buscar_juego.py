from A_1_ingresar_videojuego import juegos
def buscar_juego(juegos):

    while True:
    
        juego = input("Que juego desea buscar? (salir) para terminar: ")
        if juego.lower() == "salir":
            print("Búsqueda finalizada.")
            break
    
        if not juego:
            print("El campo no puede estar vacío")
            continue
        if juego.isdigit():
            print("no se permiten numeros")
            continue
        
        juego_normalizado = juego.lower()
        encontrado = False  
        contador = 1
        for datos in juegos:
            try:     
                if juego_normalizado in datos['nombregame'].lower():
                    print(f"{contador}- {datos['nombregame']} | {datos['genero']} | {datos['precio']}")
                    encontrado = True
                    break
            except Exception as a:
                print(f"Error en: {a}") 
            contador+=1 
        if not encontrado:
            print("el juego no existe en la lista")      
