# Introducción a los ciclos while

'''
    Los ciclos while son una estructura de control que permite repetir un bloque de código mientras 
    se cumpla una condición. 
'''

# La sintaxis básica de un ciclo while es la siguiente:

# while condicion:
    # Código a ejecutar mientras la condición sea verdadera

'''
    El ciclo while evalúa la condición y, si es verdadera, ejecuta el bloque de código. 
    Luego vuelve a evaluar la condición y repite el proceso hasta que la condición sea falsa.
'''

# Ejemplos de ciclos while

# Ejemplo 1: Contador
# Este es un ejemplo simple de un ciclo while que actúa como un contador:

contador = 0

while contador < 5:
    print(contador)
    contador += 1

'''
    En este código, el ciclo while se ejecuta mientras la variable contador sea menor que 5. 
    En cada iteración del ciclo, se imprime el valor del contador y luego se incrementa en 1.
'''

# Ejemplo 2: Suma de números

'''
    Este ejemplo muestra cómo puedes usar un ciclo while para sumar números ingresados por el 
    usuario hasta que el usuario ingrese un 0:
'''

numero = int(input('Ingresa un número: '))
suma = 0
while numero != 0:
    suma += numero
    numero = int(input('Ingresa otro número: '))
print(f'La suma de los números ingresados es {suma}')

'''
    En este código, el ciclo while se ejecuta mientras el número ingresado por el usuario sea diferente de 0.
    En cada iteración del ciclo, se suma el número ingresado a la variable suma y se pide al usuario que 
    ingrese otro número. Cuando el usuario ingresa un 0, el ciclo se detiene y se imprime la suma de los 
    números ingresados.
'''
