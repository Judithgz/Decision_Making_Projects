print('*** Cada de los Espejos ***')

edad = int(input('¿Cual es tu edad?: '))
miedo_oscuridad = input('¿Tienes miedo a la oscuridad? (Si/No): ')
miedo_oscuridad = miedo_oscuridad.strip().lower() == 'si'

if not miedo_oscuridad and edad >= 10:
    print('Puedes entrar a la casa de los espejos')
else:
    print('La casa de los espejos puede darte miedo.')