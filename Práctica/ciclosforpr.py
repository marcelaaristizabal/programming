#Sumatoria de todos los números entre el 0 y el 100.
#----Entrada al código----#
sumatoria = 0 
for iteracion in range (0,101) :
    sumatoria += iteracion
    print (iteracion)  
print (sumatoria)

#Dado un número entero positivo, mostrar su factorial.
#----Mensajes----#
MENSAJE_BIENVENIDA = 'Hola.Es un placer interactuar contigo.Soy una calculadora de factoriales'
#----Preguntas----#
PREGUNTA_FACTORIAL= 'Ingresa el número entero al que le quieras calcular el factorial : '

#----Entrada al código----#
print(MENSAJE_BIENVENIDA)
numero_factorial= int(input(PREGUNTA_FACTORIAL))
factorial = 1
for iteracion in range (numero_factorial):
    factorial = factorial * (iteracion + 1)
print (factorial)

#Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. 
# Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
#----Mensajes----#
MENSAJE_SALUDO = 'Hola. Espero que te encuentres bien,realmente es un placer interactuar contigo'
MENSAJE_EXPLICACION = 'Hoy podrás ingresar 6 números enteros cualquiera (negativos o positivos) y finalmente te daré un promedio de los números positivos y una sumatoria de los números negativos que ingresaste.'
MENSAJE_SUMATORIA = 'La sumatoria de los números negativos es : '
MENSAJE_PROMEDIO = 'El promedio de los números positivos es : '

#----Preguntas----#
Numero_1: 'Ingresa el primer número : '
Numero_2: 'Ingresa el segundo número : '
Numero_3: 'Ingresa el tercer número : '
Numero_4: 'Ingresa el cuarto número : '
Numero_5: 'Ingresa el quinto número : '
Numero_6: 'Ingresa el sexto número : '

#----Entrada al código----#
print (MENSAJE_SALUDO)
print (MENSAJE_EXPLICACION)

numero_1 = int(input(Numero_1))
numero_2 = int(input(Numero_2))
numero_3 = int(input(Numero_3))
numero_4 = int(input(Numero_4))
numero_5 = int(input(Numero_5))
numero_6 = int(input(Numero_6))

sumatoriaNEGATIVOS = 0
sumatoriaPOSITIVOS= 0
totalPOSITIVOS = 0

for iteracion in range (6):
    numero_1 = int(input(Numero_1))
    numero_2 = int(input(Numero_2))
    numero_3 = int(input(Numero_3))
    numero_4 = int(input(Numero_4))
    numero_5 = int(input(Numero_5))
    numero_6 = int(input(Numero_6))
    if (numero_1 > 0):
        sumatoriaPOSITIVOS= sumatoriaPOSITIVOS + numero_1
        totalPOSITIVOS += 1
    elif (numero_2 > 0):
        sumatoriaPOSITIVOS= sumatoriaPOSITIVOS + numero_2
        totalPOSITIVOS += 1
    elif (numero_3 > 0):
        sumatoriaPOSITIVOS= sumatoriaPOSITIVOS + numero_3
        totalPOSITIVOS += 1
    elif (numero_4 > 0):
        sumatoriaPOSITIVOS= sumatoriaPOSITIVOS + numero_4
        totalPOSITIVOS += 1
    elif (numero_5 > 0):
        sumatoriaPOSITIVOS= sumatoriaPOSITIVOS + numero_5
        totalPOSITIVOS += 1
    elif (numero_6 > 0):
        sumatoriaPOSITIVOS= sumatoriaPOSITIVOS + numero_6
        totalPOSITIVOS += 1
    else: 
        sumatoriaNEGATIVOS = sumatoriaNEGATIVOS + numero_1
        sumatoriaNEGATIVOS = sumatoriaNEGATIVOS + numero_2
        sumatoriaNEGATIVOS = sumatoriaNEGATIVOS + numero_3
        sumatoriaNEGATIVOS = sumatoriaNEGATIVOS + numero_4
        sumatoriaNEGATIVOS = sumatoriaNEGATIVOS + numero_5
        sumatoriaNEGATIVOS = sumatoriaNEGATIVOS + numero_6
print(MENSAJE_SUMATORIA ,':', sumatoriaNEGATIVOS)
if (totalPOSITIVOS != 0 ):
    print(MENSAJE_PROMEDIO, sumatoriaPOSITIVOS /totalPOSITIVOS)
else:
    print('NO SE DETECTÓ INGRESO DE NÚMEROS POSITIVOS')