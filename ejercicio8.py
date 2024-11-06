# Solicita al usuario que ingrese dos números y un carácter
nota = float(input("Ingresa la nota: "))
edad = int(input("Ingresa la edad: "))
sexo = input("Ingresa el sexo (F o M): ")

# Verifica las condiciones y muestra el mensaje correspondiente
if nota >= 5 and edad >= 18:
    if sexo.upper() == 'F':
        print("ACEPTADA")
    elif sexo.upper() == 'M':
        print("POSIBLE")
    else:
        print("Sexo no válido")
else:
    print("NO ACEPTADA")
