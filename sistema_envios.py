print('*** Sistema de Envios ***')

tarifa_nacional = 10
tarifa_internacional = 20
costo = 0

tipo_envio = input('¿El envio es nacional o internacional?: ')
tipo_envio = tipo_envio.strip().lower()

peso = float(input('Introduce el peso del paquete: '))

if tipo_envio == 'nacional':
    costo = tarifa_nacional * peso
elif tipo_envio == 'internacional':
    costo = tarifa_internacional * peso
else:
    print('Destino invalido')


print(f'El costo del envio es: {costo}')



