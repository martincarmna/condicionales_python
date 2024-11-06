# Diccionario para convertir números a días de la semana
dias_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

# Solicita al usuario que ingrese un número del 1 al 7
numero_dia = int(input("Ingresa un número del 1 al 7 para conocer el día de la semana: "))

# Verifica si el número está en el rango válido y muestra el día correspondiente o un mensaje de error
if numero_dia in dias_semana:
    print(f"El día correspondiente al número {numero_dia} es {dias_semana[numero_dia]}.")
else:
    print("ERROR: número incorrecto.")
