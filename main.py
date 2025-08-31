from A_1_ingresar_videojuego import ingresar_juego, juegos
from B_2_actualizar_juego import actualizar_juego
from C_3_eliminar_juego import eliminar_juego
from D_4_buscar_juego import buscar_juego
from E_5_imprimir_lista import imprimir_lista
def menu():
    while True:
        print("\n======MENÚ PRINCIPAL======")
        print("\nA_1- Ingresar video juego")
        print("B_2- Actualizar juego")
        print("C_3- Eliminar juego")
        print("D_4- Buscar juego")
        print("H_5- Mostrar lista de juegos")
        
        try:
            entrada = input("\nIngresa la opcion que deseas: ")
            if entrada == "A" or (entrada.isdigit()) and (int(entrada)) == 1:
                ingresar_juego(juegos)
            elif entrada == "B" or (entrada.isdigit()) and (int(entrada)) == 2:
                actualizar_juego(juegos)
            elif entrada == "C" or (entrada.isdigit()) and (int(entrada)) == 3:
                eliminar_juego(juegos)
            elif entrada == "D" or (entrada.isdigit()) and (int(entrada)) == 4:
                buscar_juego(juegos)
            elif entrada == "E" or (entrada.isdigit()) and (int(entrada)) == 5:
                imprimir_lista(juegos)
            
        except ValueError:
            print("Error")

if __name__ == "__main__":
    menu()

