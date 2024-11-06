'''Programa que pida dos numeros e indique Cual es el mayor
si los dos soniguales que muestreel mensaje son iguales'''

num1 = int(input("introduce el primer numero: "))
num2 = int(input("introduce el segundo numero: "))
if num1 > num2:
 print(f"el mayor es: {num1}")
elif num1 < num2:
 print(f"el numero mayor es igual a: {num2}") 
else:
 print("son iguales")

