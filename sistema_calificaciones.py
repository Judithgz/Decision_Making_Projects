print('*** Sistema de calificaciones *** ')

calificacion = float(input('Escribe la calificacion (0-10): '))
calificacion_letra = None

if 9 <= calificacion <= 10:
    calificacion_letra = 'A'
elif 8 <= calificacion < 9:
    calificacion_letra = 'B'
elif 7 <= calificacion < 8:
    calificacion_letra = 'C'
elif 6 <= calificacion < 7:
    calificacion_letra = 'D'
elif 0 <= calificacion < 6:
    calificacion_letra = 'F'
else:
    calificacion_letra = 'Calificacion incorrecta'


print(f'Calificacion {calificacion} es equivalente a {calificacion_letra}')