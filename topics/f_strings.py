name = 'Ana'
year = 2000
text = f'Hola {name}'
print(text)

text_sum = f'Hola, {name} tu tienes {2026-year} años'
print(text_sum)

# Funciones o metodos

text_func = f'Hola {name.upper()}'
print(text_func)

# Condicionales

edad = 16
text_if = f'Hola {name}, eres {'mayor' if edad >= 18 else 'menor'} de edad'
print(text_if)

# Acceso a diccionarios

datos = {"ciudad": "Lima"}
texto = f"Vives en {datos['ciudad']}"
print(texto)

# Posibilidad de usar modificadores de formato, dandole a la variable dos puntos
# :, Leer numeros grandes

bank_balance = 1200000000
text = f'Tu saldo en la cuenta bancaria es: {bank_balance:,}'

# Separador decimales
# :.1f Muestra un valor despues del punto

stock_price = 1.405
text = f'El valor del stock price: {stock_price:.1f}'

# Agregar ceros a la izquierda
# :03d agrega ceros a la izquierda

user_id = 1
text = f'Su id es: {user_id:03d}'

# Formatear en una tabla

product = 'laptop'
price = 1000

# Alinear el texto
# :>15

# Interaaccion y enlistar muchas productos

text = f'Producto: {product:>5} | price: {price}'
print(f'{text}\n{text}')

# Imprimir fechas

from datetime import datetime  # noqa: E402

date = datetime(2025, 5, 30, 12)
text = f'La fecha completa es: {date: %A %d}'
print(text)

# Formateadores: reto, crear en una linea de codigo formatear porcentaje y numero cientifico
