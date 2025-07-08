print("*** Sistema de Descuentos ***")

monto_compra_desc = 1000

compra = float(input("Ingresa el monto de tu compra: "))
miembro = input("¿Eres miembro de la tienda? (si/no): ")

descuento = 0

if compra >= monto_compra_desc and miembro.strip().lower() == 'si':
    descuento = 0.1 # Descuento del 10%
elif miembro.strip().lower() == 'si':
    descuento = .05 # Descuento del 5%
elif compra >= monto_compra_desc:
    descuento = .03 # Descuento del 3%
else:
    descuento = 0

# Calculos
if descuento != 0:
    monto_descuento = compra * descuento
    monto_final = compra - descuento
    print(f'\nFelicidades, tu descuento es del {descuento * 100:.0f}%')
    print(f'Monto de la compra: ${compra:.2f}')
    print(f'Monto del descuento: ${monto_descuento:.2f}')
    print(f'Monto final con descuento aplicado: ${monto_final:.2f}')
else:
    print('\nNo obtuviste ningun descuento')
    print(f'Monto final de la compra: ${compra}')