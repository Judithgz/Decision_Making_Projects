print(' *** Sistema de Autenticacion *** ')

usuario_valido = 'judithgzz'
password_valido = 'Hola123'

usuario = input('Introduce tu usuario: ')
password = input('Introduce tu contraseña: ')

if usuario == usuario_valido and password == password_valido:
    print(f'Bienvenido al sistema')
elif usuario != usuario_valido:
    print(f'Introduce tu usuario nuevamente: ')
elif password != password_valido:
    print(f'Introduce tu contraseña nuevamente')
else:
    print(f'Usuario y contraseña incorrectos, vuelve a introducirlos')
