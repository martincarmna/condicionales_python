# Solicita al usuario que ingrese la duración de la llamada en minutos y el día de la semana
duracion = int(input("Ingresa la duración de la llamada en minutos: "))
dia_semana = input("Ingresa el día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo): ").capitalize()
turno = input("Ingresa el turno (mañana o tarde): ").lower()

# Calcula el costo de la llamada sin impuestos
if duracion <= 5:
    costo_llamada = duracion * 1
elif duracion <= 8:
    costo_llamada = 5 * 1 + (duracion - 5) * 0.8
elif duracion <= 10:
    costo_llamada = 5 * 1 + 3 * 0.8 + (duracion - 8) * 0.7
else:
    costo_llamada = 5 * 1 + 3 * 0.8 + 2 * 0.7 + (duracion - 10) * 0.5

# Calcula el impuesto según el día de la semana y el turno
if dia_semana == "Domingo":
    impuesto = 0.03
else:
    if turno == "mañana":
        impuesto = 0.15
    elif turno == "tarde":
        impuesto = 0.10
    else:
        impuesto = 0
        print("Turno no válido. No se aplicará ningún impuesto adicional.")

# Calcula el costo total incluyendo el impuesto
costo_total = costo_llamada + (costo_llamada * impuesto)

# Muestra el costo total a pagar y el costo por cada concepto
print(f"Costo de la llamada sin impuestos: {costo_llamada:.2f} euros.")
print(f"Impuesto aplicado: {impuesto * 100:.0f}%.")
print(f"Costo total a pagar: {costo_total:.2f} euros.")
