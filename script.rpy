# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen", color="#33fff0")
define a = Character("[Jugador]")


# El juego comienza aquí.

#label start:  

  #$ Jugador = renpy.input("Cual es tu nombre?")

  #$ Jugador = Jugador.strip()

  #if Jugador == "":
# $ Jugador = "Jugador"

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

#scene bg 

    # Presenta las líneas del diálogo.


    # Finaliza el juego:

label start:

    $ Jugador = renpy.input("Cual es tu nombre?")
    $ Jugador = Jugador.strip()

    if Jugador == "":
        $ Jugador = "Jugador"
    image bg BUG="HRR.jpg"
    scene bg BUG

    e "Has creado un nuevo juego Ren'Py."
    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"
    a "Dafok"

    return


    return


 
 
