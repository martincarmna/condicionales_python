# Función para determinar el ganador
def determinar_ganador(opcion1, opcion2):
    if opcion1 == opcion2:
        return "Empate"
    elif (opcion1 == "piedra" and opcion2 == "tijera") or \
         (opcion1 == "papel" and opcion2 == "piedra") or \
         (opcion1 == "tijera" and opcion2 == "papel"):
        return "Gana jugador 1"
    else:
        return "Gana jugador 2"

# Solicita las opciones de los dos jugadores
opcion1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
opcion2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

# Verifica si las opciones son válidas
opciones_validas = ["piedra", "papel", "tijera"]
if opcion1 in opciones_validas and opcion2 in opciones_validas:
    resultado = determinar_ganador(opcion1, opcion2)
    print(resultado)
else:
    print("Opción incorrecta")
