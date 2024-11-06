# Solicita al usuario que ingrese la base y el exponente
base = float(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

# Calcula la potencia según las condiciones dadas
if exponente > 0:
    resultado = base ** exponente
    print(f"El resultado de {base} elevado a la {exponente} es {resultado}.")
elif exponente == 0:
    resultado = 1
    print(f"El resultado de {base} elevado a la {exponente} es {resultado}.")
else:
    resultado = 1 / (base ** abs(exponente))
    print(f"El resultado de {base} elevado a la {exponente} es {resultado}.")

