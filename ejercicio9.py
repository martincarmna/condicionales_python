# Solicita al usuario que ingrese tres números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

# Crea una lista con los números ingresados
numeros = [numero1, numero2, numero3]

# Ordena la lista de mayor a menor
numeros.sort(reverse=True)

# Muestra los números ordenados
print("Números ordenados de mayor a menor:")
for numero in numeros:
    print(numero)
