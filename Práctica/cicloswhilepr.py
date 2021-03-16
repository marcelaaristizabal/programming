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
sumatoria = 0
MENSAJE_GANASTE2 = f'¡Muy bien! El número {sumatoria} era el correcto.'

#----Entrada al código----#
print(MENSAJE_SALUDO2)
PREGUNTA_NUMERO2 = 'Ingresa un número entero de una cifra o 0 para terminar. Por favor : '
numero_escogido2 = int(input(PREGUNTA_NUMERO2))
while (numero_escogido2 != 0):
    sumatoria += numero_escogido2
    print(MENSAJE_FALLASTE2)
    numero_escogido2= int (input(PREGUNTA_NUMERO2))
print (sumatoria)
print(MENSAJE_GANASTE2) 

#Escriba dos números enteros.El segundo debe ser mayor que el primero.
#----Mensajes----#
MENSAJE_SALUDO = 'Hola.Es un placer interactuar contigo'
MENSAJE_DESPEDIDA = 'Que tengas un feliz día'
MENSAJE_ERROR = 'El número que ingresaste no es válido.Inténtelo de nuevo'
print (MENSAJE_SALUDO)

#----Entradas al código----#
PREGUNTA_NUMERO_A ='Ingrese un número entero A, por favor: ' 
PREGUNTA_NUMERO_B ='Ingrese un número entero B mayor al número A, por favor: '
numeroA = int(input(PREGUNTA_NUMERO_A))
numeroB = int(input(PREGUNTA_NUMERO_B))
while (numeroB <= numeroA) :
    print (MENSAJE_ERROR)
    numeroB = int(input(PREGUNTA_NUMERO_B))
print ('Los números que ingresaste fueron:',numeroA, 'y',numeroB,MENSAJE_DESPEDIDA)

#Escribir un número entero, siempre y cuando uno sea mayor que el anterior
#----Saludos----#
MENSAJE_ENTRADA = 'Hola.Espero que te encuentres bien,es un placer interactuar contigo. Vas a ingresar números enteros cualquieras,pero solo te mostraré estos,si los ingresas uno mayor al anterior.'
MENSAJE_DESPEDIDA3 = 'Muchas gracias por tu participación. Ten un bonito día.'
print (MENSAJE_ENTRADA)
#----Entrada al código----#
PREGUNTA_NUMERO1= 'Ingresa un número entero,por favor : '
PREGUNTA_NUMERO2= 'Ingresa un número entero mayor al número anterior,por favor : '
numero_ingresado1 = int(input(PREGUNTA_NUMERO1))
numero_ingresado2 = int(input(PREGUNTA_NUMERO2))
MENSAJE_ADVERTENCIA =f'¡UPS! El número ingresado no es válido.El número debe ser mayor a {numero_ingresado1} Intenta nuevamente...'

while (numero_ingresado2 <= numero_ingresado1):
    print (MENSAJE_ADVERTENCIA)
    numero_ingresado2 =int(input(PREGUNTA_NUMERO1))
print(MENSAJE_DESPEDIDA3)

#Ingresar montos de compras de un cliente  (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
# Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
#----Preguntas----#
PREGUNTA_MONTO = 'Ingrese la cantidad o montos totales de las compras. Por favor : '
#----Mensajes----#
MENSAJE_DESCUENTO= 'El monto de comprar superó los $1000. Se aplicará un descuento del 10%.'
MENSAJE_FALLA= 'El monto ingresado no es válido.Verifique e ingréselo nuevamente.'
#----Entrada al código----#
valor = float(input(PREGUNTA_MONTO))
acumulado = 0 

while (valor != 0):
    if (valor <= 0):
        print (MENSAJE_FALLA)
    else: 
        acumulado += valor 
    valor = float(input(PREGUNTA_MONTO))
if (acumulado > 1000):
    descuento = acumulado - (acumulado*0.10)
    print (MENSAJE_DESCUENTO)
    MENSAJE_DA= f'El monto total a cancelar es: {descuento}'
    print (MENSAJE_DA)
print ('Muchas gracias por su compra.Regrese.')