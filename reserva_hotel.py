print("*** Sistema de Reserva de Hotel ***")

tarifa_sin_vista = 150.50
tarifa_con_vista = 190.50

nombre = input('Nombre del cliente: ')
dias = int(input('Dias de estadia: '))
vista_mar_txt = input('¿Vista al mar? (Si/No): ')
vista_al_mar = vista_mar_txt.strip().lower() == 'si'


if vista_al_mar:
    costo = dias * tarifa_con_vista
else:
    costo = dias * tarifa_sin_vista


print(f'Nombre del cliente: {nombre}')
print(f'Dias de estadia: {dias}')
print(f'¿Vista al mar?: {'Si' if vista_al_mar else 'No'}')
print(f'Total de estancia: ${costo:.2f}')
