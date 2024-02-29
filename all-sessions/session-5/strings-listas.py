# session-5.py

# --------------------------
# Strings en Python
# --------------------------

# Los strings son secuencias de caracteres y se definen utilizando comillas simples o dobles.
mi_string = "¡Hola, mundo!"
print(mi_string)

# Podemos acceder a cada carácter en un string utilizando su índice.
print(mi_string[0])  # Salida: ¡
print(mi_string[-1])  # Salida: !

# Los strings en Python son inmutables, lo que significa que no puedes cambiar un carácter de un string una vez que se ha definido.
# mi_string[0] = 'h'  # Esto dará un error

# Podemos concatenar strings con el operador +.
saludo = "¡Hola, "
nombre = "mundo!"
mi_string = saludo + nombre
print(mi_string)  # Salida: ¡Hola, mundo!

# Python proporciona una serie de métodos útiles que puedes usar con strings.
print(mi_string.upper())  # Salida: ¡HOLA, MUNDO!
print(mi_string.lower())  # Salida: ¡hola, mundo!
palabras = mi_string.split()
print(palabras)  # Salida: ['¡Hola,', 'mundo!']
nuevo_string = ' '.join(palabras)
print(nuevo_string)  # Salida: ¡Hola, mundo!

# --------------------------
# Listas en Python
# --------------------------

# Las listas en Python son colecciones ordenadas de elementos.
mi_lista = ['manzana', 'banana', 'cereza']
print(mi_lista)

# Podemos acceder a cualquier elemento de la lista utilizando su índice.
print(mi_lista[0])  # Salida: 'manzana'

# Las listas son mutables, lo que significa que puedes cambiar sus elementos.
mi_lista[1] = 'naranja'
print(mi_lista)  # Salida: ['manzana', 'naranja', 'cereza']

# Podemos añadir elementos al final de la lista con el método append().
mi_lista.append('kiwi')
print(mi_lista)  # Salida: ['manzana', 'naranja', 'cereza', 'kiwi']

# Podemos eliminar elementos de la lista con el método remove().
mi_lista.remove('naranja')
print(mi_lista)  # Salida: ['manzana', 'cereza', 'kiwi']

# Podemos obtener el número de elementos en la lista con la función len().
print(len(mi_lista))  # Salida: 3
