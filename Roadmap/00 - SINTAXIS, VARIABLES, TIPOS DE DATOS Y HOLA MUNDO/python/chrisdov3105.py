# https://www.python.org

# Esto es un comentario de una sola línea

"""
Se usan 3 comillas dobles para hacer comentarios de varias lineas
Como este comentario por ejemplo
"""

'''
Tambien vi que podemos usar 3 comillas simples 
para el mismo proposito, es decir, para hacer comentarios de
varias lineas de texto
'''

# Variables en python.
'''En python la snake_case es la convencion estandar para nombrar variables'''

''' Una variable se crea asignándole un valor usando el operador de asignación = '''

"""
Los nombres de las variables deben comenzar con una letra (mayúscula o minúscula) o un guion bajo (_). 
Después del primer carácter, pueden contener letras, números y guiones bajos. 
No se pueden utilizar palabras reservadas de Python como nombres de variables (por ejemplo, if, for, while). 
Se recomienda utilizar nombres descriptivos y en minúsculas, 
separando palabras con guiones bajos (por ejemplo, mi_variable_nombre).
"""

# Ejemplo de una variable.

edad = 30

""" 
En python no existen constantes en el sentido estricto de la palabra como en otro lenguajes
Sin embargo, se sigue una convención para simularlas: 
se utilizan nombres de variables en mayúsculas para indicar 
que el valor no debe ser modificado durante la ejecución del programa.
"""

# Ejemplo de la convencion que se suele usar para simular una constante.

EDAD = 30

# Tipos de variables en python.

''' En Python, los tipos de datos primitivos son los componentes básicos para almacenar datos. '''
''' Existen basicamente 4 tipos '''

"""
Enteros (int) representan nuemeros enteros. 
Se utilizan para contar, indexar y realizar operaciones aritméticas. 
"""
   edad = 30  # Entero que representa la edad

"""
Flotantes (float) Representan números con decimales, también positivos o negativos.
Se utilizan para cálculos que involucran fracciones o valores con precisión.
Se separan por un punto, no por una coma.
"""
   precio = 19.99  # Precio con decimales

"""
   Cadenas (str) Representan secuencias de caracteres, como texto. 
   Se utilizan para almacenar y manipular información textual. 
   Se encierra el valor de la variable entre comillas dobles o simples.
"""
   nombre = "Juan"  # Cadena de caracteres que representa un nombre

"""
Booleanos (bool) Solo pueden tener dos valores posibles, ya sea True (verdadero) o False (falso).
Se utilizan para evaluar condiciones y tomar decisiones lógicas. 
"""
   es_mayor_de_edad = True  # Booleano que indica si es mayor de edad

# Imprimiendo el nombre del lenguaje.
print ("Hola, Python!") 




