# Session 7 - Python Automation #

# REPASO Sintaxis

for i in range(5):
    print(i)

''' 
    Este código imprimirá los números del 0 al 4. La función range(5) genera una secuencia de números del 0 al 4, 
    y el ciclo for recorre esta secuencia, asignando cada número a i y ejecutando el bloque de código dentro del ciclo. 
'''

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

# CONDICIONALES DENTRO DEL CICLO
    
''' Modifica el código de saludo para que solo salude a los nombres que comienzan con una letra determinada.
    Por ejemplo, solo los nombres que comienzan con ‘A’. '''
    
nombres = ["Ana", "Juan", "Carlos", "María"]
for nombre in nombres:
    if nombre[0] == 'A':
        print(f"Hola, {nombre}!")

''' En este ejercicio, el ciclo for recorre una lista de nombres. Dentro del ciclo, usamos la indexación de 
    cadenas para verificar si el nombre actual comienza con la letra ‘A’. Si es así, se imprime un saludo personalizado para ese nombre. '''

# Escribimos un Ciclo FOR que recorra una lista de números y detenga el ciclo cuando encuentre un número negativo.
        
numeros = [5, 3, 2, 4, -1, 6, 5]
for numero in numeros:
    if numero < 0:
        break
    print(numero)

''' En este ejercicio, el ciclo for recorre una lista de números. Dentro del ciclo, usamos la declaración break para detener el ciclo 
    si encontramos un número negativo. La declaración break termina el ciclo por completo, sin importar cuántas iteraciones quedan. 
    En este caso, cuando se encuentra el número -1, el ciclo se detiene y no se imprimen más números. '''