PREGUNTA_NOMBRE = "Ingresa tu nombre.Por favor : "
nombre = input (PREGUNTA_NOMBRE)
print(f"Hola {nombre}.Espero que estés muy bien")
PREGUNTA_DEACUERDO = '''
        Si - ¿Te vuelvo a saludar?
        No - Me despido 
'''
decision = input (PREGUNTA_DEACUERDO)
MENSAJE_SALUDO = f"Hola {nombre}.Te saludo nuevamente"
MENSAJE_DESPEDIDA = f"Hasta luego, {nombre}.Espero verte de nuevo."
MENSAJE_FALLASTE = 'Ese no es el número. Sigue intentando...'
MENSAJE_GANASTE = '¡Bien! Acertaste el número'

while (decision == 'Si') :
    print(MENSAJE_SALUDO)
    decision = input(PREGUNTA_DEACUERDO)
print (MENSAJE_DESPEDIDA)

numero_secreto = 9
PREGUNTA_NUMERO = 'Ingrese un número entero entre el 1 y el 10. Por favor : '
numero_escogido = int (input(PREGUNTA_NUMERO))
while (numero_escogido != numero_secreto) :
    print (MENSAJE_FALLASTE)
    numero_escogido = int (input( PREGUNTA_NUMERO))
print(MENSAJE_GANASTE)



#----Ejercicios While----#
#Leer números enteros de teclado, hasta que el usuario ingrese 0. Finalmente,mostrar la sumatoria de todos los número ingresados.
#----Mensajes----#
MENSAJE_SALUDO2= 'Hola. Es un placer interactuar contigo,espero que te encuentres bien'
MENSAJE_DESPEDIDA2 = 'Hasta luego. Ten un bonito día'
MENSAJE_FALLASTE2 = '¡Ups! Ese no era el número. Sigue intentando...'
numero_oculto2 = 0
MENSAJE_GANASTE2 = f'¡Muy bien! El número {numero_oculto2} era el correcto.'

#----Entrada al código----#
print(MENSAJE_SALUDO2)
PREGUNTA_NUMERO2 = 'Ingresa un número entero de una cifra. Por favor : '
numero_escogido2 = int(input(PREGUNTA_NUMERO2))

while (numero_escogido2 != numero_oculto2):
    print(MENSAJE_FALLASTE2)
    numero_escogido2= int (input(PREGUNTA_NUMERO2))
print(MENSAJE_GANASTE2) 

#Escriba dos números enteros.El segundo debe ser mayor que el primero.
#----Mensajes----#
MENSAJE_SALUDO = 'Hola.Es un placer interactuar contigo'
MENSAJE_DESPEDIDA = 'Que tengas un feliz día'
MENSAJE_ERROR = 'El número que ingresaste no es válido.Inténtelo de nuevo'
print (MENSAJE_BIENVENIDA)

#----Entradas al código----#
PREGUNTA_NUMERO_A ='Ingrese un número entero A, por favor: ' 
PREGUNTA_NUMERO_B ='Ingrese un número entero B, por favor: '
numeroA = int(input(PREGUNTA_NUMERO_A))
numeroB = int(input(PREGUNTA_NUMERO_B))
while (numeroB <= numeroA) :
    print (MENSAJE_ERROR)
    numeroB = int(input(PREGUNTA_NUMERO_B))
print ('Los números que ingresaste fueron:',numeroA, 'y',numeroB,MENSAJE_DESPEDIDA)

#Escribir un número entero, siempre y cuando uno sea mayor que el anterior
#----Saludos----#
MENSAJE_BIENVENIDA3: 'Hola.Espero que te encuentres bien,es un placer interactuar contigo. Vas a ingresar números enteros cualquieras,pero solo te mostraré estos,si los ingresas uno mayor al anterior.'
MENSAJE_ADVERTENCIA :'¡UPS! El número ingresado no es válido. Intenta nuevamente...'
MENSAJE_DESPEDIDA3 = 'Muchas gracias por tu participación. Ten un bonito día.'
print (MENSAJE_BIENVENIDA3)
#----Entrada al código----#
PREGUNTA_NUMERO = 'Ingresa un número entero,por favor : '
numero_ingresado = int(input(PREGUNTA_NUMERO))
numero_permitido = numero_permitido > numero_ingresado 
while (numero_permitido <= numero_ingresado):
    print (MENSAJE_ADVERTENCIA)
    numero_ingresado = int(input(PREGUNTA_NUMERO))
print(MENSAJE_DESPEDIDA3)