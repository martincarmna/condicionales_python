# Diccionario para convertir números a letras
numeros_a_letras = {
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis"
}

# Diccionario para encontrar la cara opuesta del dado
caras_opuestas = {
    1: 6,
    2: 5,
    3: 4,
    4: 3,
    5: 2,
    6: 1
}

# Solicita al usuario que ingrese el resultado del dado
resultado = int(input("Ingresa el resultado del dado (1-6): "))

# Verifica si el resultado está en el rango válido
if resultado < 1 or resultado > 6:
    print("ERROR: número incorrecto.")
else:
    cara_opuesta = caras_opuestas[resultado]
    print(f"El número opuesto a {resultado} es {numeros_a_letras[cara_opuesta]}.")
