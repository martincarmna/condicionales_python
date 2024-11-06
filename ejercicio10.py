# Solicita al usuario que ingrese el número de alumnos
num_alumnos = int(input("Ingresa el número de alumnos: "))

# Define el costo por alumno y el costo total según el número de alumnos
if num_alumnos >= 100:
    costo_por_alumno = 65
    costo_total = num_alumnos * costo_por_alumno
elif 50 <= num_alumnos < 100:
    costo_por_alumno = 70
    costo_total = num_alumnos * costo_por_alumno
elif 30 <= num_alumnos < 50:
    costo_por_alumno = 95
    costo_total = num_alumnos * costo_por_alumno
else:
    costo_por_alumno = 4000 / num_alumnos
    costo_total = 4000

# Muestra el costo total a pagar a la compañía de autobuses y el costo por alumno
print(f"El costo total a pagar a la compañía de autobuses es de {costo_total} euros.")
print(f"Cada alumno debe pagar {costo_por_alumno:.2f} euros.")
