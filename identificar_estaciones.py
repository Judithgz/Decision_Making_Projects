print("*** Estaciones del Año ***")

mes = int(input('Introduce un mes para identificar la estación: '))

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Estacion desconocida'

print(f'En el mes {mes} la estación es {estacion}')
