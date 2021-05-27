MENSAJE_SALUDO = 'Hola,soy tu convertidora de monedas ONLINE. En el día de hoy podrás ingresar cuánto dinero tienes en dólares y te lo convertiré en euros.'
PREGUNTA_DOLARES = 'Ingresa la cantidad de dinero en dólares (US) : '
MENSAJE_EUROS = 'Mostrando cantidad ingresada en euros...'

isCorrectInfo = False
while (isCorrectInfo == False):
    try: 
        cantidadDolares= float (input(PREGUNTA_DOLARES))
        isCorrectInfo = True
    except ValueError : 
        print ('Ingresaste un dato no válido.')

euros = cantidadDolares * 0.82
cantidadEuros = euros
print(MENSAJE_EUROS)
print (cantidadEuros)

isCorrectInfo = False
while (isCorrectInfo == False):
    try : 
        PREGUNTA_NOMBRE ='Por favor,ingrese su nombre : '
        nombre= (input(PREGUNTA_NOMBRE))
        assert (nombre.isalpha())
        isCorrectInfo = True
    except AssertionError: 
            print ('Ingresaste un dato no válido')
isCorrectInfo = False