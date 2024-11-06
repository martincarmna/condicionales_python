# Diccionario que asocia cada mes con su número de días
dias_del_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Solicita al usuario que ingrese un número entre 1 y 12
numero_mes = int(input("Ingresa un número entero entre 1 y 12: "))

# Verifica si el número está en el rango válido y muestra el número de días correspondiente o un mensaje de error
if 1 <= numero_mes <= 12:
    print(f"El mes {numero_mes} tiene {dias_del_mes[numero_mes]} días.")
else:
    print("ERROR: número incorrecto.")
