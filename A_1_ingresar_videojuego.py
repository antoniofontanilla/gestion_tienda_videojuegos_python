juegos = [
    {
        "nombregame": "The Legend of Zelda",
        "genero": "Aventura",
        "precio": 60
    },
    {
        "nombregame": "FIFA 21",
        "genero": "Deportes",
        "precio": 50
    },
]
def ingresar_juego(juegos):
    while True:
        juego = input("Nombre del juego: ").title()
        try:
                
            if not juego:
                print("El campo no puede estar vacio")
                continue
            for idx,datos in enumerate(juegos):
                if datos["nombregame"] == juego:
                    print("este video juego ya existe")
                    break
            genero = input("Ingrese el genero: ").title()
            if not genero:
                print("El campo no puede estar vacio")
                continue
            precio = int(input("Ingresa precio: ").title())
            if not precio:
                print("El campo no puede estar vacio")
                continue
            
            juego_nuevo = {
                "nombregame": juego,
                "genero": genero,
                "precio": precio
            }
            juegos.append(juego_nuevo)
            print(f"{juego} ha sido agregado con exito")
            break
        
        except ValueError:
            print("ERROR!!")


