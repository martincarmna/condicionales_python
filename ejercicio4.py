# Solicita al usuario que ingrese dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Verifica si el segundo número es cero
if numero2 != 0:
    resultado = numero1 / numero2
    print(f"La división de {numero1} entre {numero2} es {resultado}.")
else:
    print("El segundo número no puede ser cero. No se puede realizar la división.")
