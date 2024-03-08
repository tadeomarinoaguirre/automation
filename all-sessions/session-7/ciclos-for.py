# Session 7 - Python Automation #

# REPASO Sintaxis

for i in range(5):
    print(i)

''' 
    Este código imprimirá los números del 0 al 4. La función range(5) genera una secuencia de números del 0 al 4, 
    y el ciclo for recorre esta secuencia, asignando cada número a i y ejecutando el bloque de código dentro del ciclo. 
'''

# for: Esta es la palabra clave que inicia un ciclo for en Python.
# i: Esta es la variable que usamos para iterar. En cada iteración del ciclo, i tomará un valor diferente.
# in: Esta es otra palabra clave de Python que se usa en un ciclo for. Se utiliza para especificar que la 
#     variable i tomará sus valores de la secuencia que viene después de in.
# range(5): range(5) genera una secuencia de números del 0 al 4. En cada iteración del ciclo, i tomará el 
#           siguiente valor en esta secuencia.
# : Este símbolo se utiliza para indicar el inicio del bloque de código que se ejecutará en cada iteración
#   del ciclo.
# print(i): Esta es la instrucción que se ejecuta en cada iteración del ciclo. En este caso, 
#           simplemente imprime el valor actual de i.

# USO BASICO
    
# Cómo se puede usar un ciclo for para automatizar tareas repetitivas.
    
''' 
    Por ejemplo, podrías tener una lista de nombres y quieres saludar a cada persona por su nombre.
    Este código imprimirá un saludo personalizado para cada nombre en la lista.
'''
    
nombres = ["Ana", "Juan", "Carlos", "María"]
for nombre in nombres:
    print(f"Hola, {nombre}!")

''' 
    La f antes de "Hola, {nombre}!" le da formato a la cadena de texto. Indica que es una f-string. 
    {nombre} es una expresión que se sustituye por el valor de la variable nombre. 
    Por lo tanto, para cada nombre en la lista nombres, se imprime "Hola, " seguido del valor de nombre.
'''

# EJERCICIOS PRÁCTICOS

# 1. Suma de los números en una lista:

numeros = [5, 3, 2, 4, -1, 6, 5]
suma = 0
for numero in numeros:
    suma += numero # suma = suma + numero
print(f"La suma de los números en la lista es {suma}")

# CONDICIONALES DENTRO DEL CICLO

# 2. Filtrando Listas:

''' Modifica el código de saludo para que solo salude a los nombres que comienzan con una letra determinada.
    Por ejemplo, solo los nombres que comienzan con ‘A’. '''
    
nombres = ["Ana", "Juan", "Carlos", "María"]
for nombre in nombres:
    if nombre[0] == 'A':
        print(f"Hola, {nombre}!")

''' En este ejercicio, el ciclo for recorre una lista de nombres. Dentro del ciclo, usamos la indexación de 
    cadenas para verificar si el nombre actual comienza con la letra ‘A’. Si es así, se imprime un saludo personalizado para ese nombre. '''

# 3.a Contar la contidad de letras 'o' dentro de la cadena:

cadena = "Hola, ¿cómo estás?"
letra = 'o'
contador = 0
for caracter in cadena:
    if caracter == letra:
        contador += 1
print(f"La letra '{letra}' aparece {contador} veces en la cadena.")

# 3.b Crear una lista con los números pares de otra lista:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(f"Los números pares son {pares}")

'''
    numero % 2: Aquí, el operador % es el operador de módulo, que devuelve el resto de la división de 
    numero por 2. Si numero es par, entonces numero % 2 será 0 porque los números pares son divisibles 
    por 2 sin dejar residuo.
'''

# 3. Cortando el Ciclo 'break'

# Escribimos un Ciclo FOR que recorra una lista de números y detenga el ciclo cuando encuentre un número negativo.

'''
    La declaración break en Python termina el ciclo actual y reanuda la ejecución en la siguiente instrucción
    después del ciclo. Se utiliza cuando queremos terminar un ciclo prematuramente, por ejemplo, cuando ya
    hemos encontrado lo que estábamos buscando. Aquí tienes un ejemplo de cómo se usa break:
'''

numeros = [5, 3, 2, 4, -1, 6, 5]
for numero in numeros:
    if numero < 0:
        break
    print(numero)

''' En este ejercicio, el ciclo for recorre una lista de números. Dentro del ciclo, usamos la declaración break para detener el ciclo 
    si encontramos un número negativo. La declaración break termina el ciclo por completo, sin importar cuántas iteraciones quedan. 
    En este caso, cuando se encuentra el número -1, el ciclo se detiene y no se imprimen más números. '''

# 4. Saltando iteración con 'continue'