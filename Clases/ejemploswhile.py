
#----Entradas----#
MENSAJE_BIENVENIDA = "Muy buenos días. Despierte que está en clase de 6 am"
MENSAJE_ERROR = 'Ingrese una ipción válida'
PREGUNTA_MENU = '''Ingrese
    1 - Para mostrar los números del 1 al 5
    2- Para preguntar tu nombre 
    3- Para mostrar el año en el que estamos
    4- Salir

'''
PREGUNTA_NOMBRE = 'Ingrese su nombre por favor : '

#___
entrada = 1
while (entrada >= 1 or entrada <= 3) :
    entrada = int (input(PREGUNTA_MENU))
    if (entrada ==1 ) :
        print (1, 2, 3 ,4, 5)
    elif (entrada == 2) :
        nombre = input (PREGUNTA_NOMBRE)
        print (f'Bienvenido {nombre} a este menú. Emplea las otras opciones' )
    elif (entrada == 3) :
        print (' Estamos en el año 2021')
    elif (entrada == 4) :
        print ('Muchas gracias por usar el programa. Feliz día')
    else :
        entrada = 1 
        print (MENSAJE_ERROR)