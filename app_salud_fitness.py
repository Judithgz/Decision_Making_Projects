print('*** Aplicacion de Salud y Fitness *** ')

# Constantes
meta_pasos_diario = 10000
calorias_por_paso = 0.04

# Pedimos los valores
nombre = input('Escribe tu nombre: ')
pasos_diarios = int(input('¿Cuantos pasos caminaste hoy?: '))

# Verificar si el usuario alcanzo la meta
meta_alcanzada = pasos_diarios >= meta_pasos_diario
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'
# Calculamos calorias
calorias_quemadas = pasos_diarios * calorias_por_paso

# Mostrar info
print(f'\nUsuario: {nombre}')
print(f'Pasos dados hoy: {pasos_diarios}')
print(f'Calorias quemadas: {calorias_quemadas} kcal')
print(f'Meta de pasos diario alcanzada: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de: {meta_pasos_diario}')