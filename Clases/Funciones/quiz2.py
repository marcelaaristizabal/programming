import conversorTemperatura as ct 
import funciones as fn
PREGUNTA_NUMERO = ''' Ingrese alguna de estas opciones 
    1. Convertir temperaturas
    2. Mostrar clasificación
    3. Mostrar topes
    4. Salir
'''
PREGUNTA_TEMPERATURA ='''
    K- Mostrar Kelvin
    F- Mostrar  Fahrenheit
    C- Mostrar Celsius
'''

#-------Mensajes-------#
MENSAJE_CELSIUS = 'Mostrando lista original. No es necesaria la conversión.'
MENSAJE_FAHRENHEIT = 'Mostrando lista en Fahrenheit'
MENSAJE_KELVIN ='Mostrando lista en Kelvin'
MENSAJE_DESPEDIDA = 'Que tengas un feliz día'
#-------Error-------#
MENSAJE_ERROR_ENTRADA:'Valor ingresado no válido.'

temperaturaCorporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

temperaturaCorporalFahrenheit = ct.conversionTemperatura(temperaturaCorporal, 'F')
temperaturaCorporalKelvin = ct.conversionTemperatura(temperaturaCorporal, 'K')
clasificaciónTemperaturas = ct.clasificarTemperaturas(temperaturaCorporal)

opcion_escogida= int(input(PREGUNTA_NUMERO))
while (opcion_escogida != 4 ):
    #----------------Opción1----------------#
    if (opcion_escogida == 1) :
        opcion_temperatura = input(PREGUNTA_TEMPERATURA)
        if (opcion_temperatura== 'C') :
            print(MENSAJE_CELSIUS)
            fn.mostrarLista(temperaturaCorporal)
        elif (opcion_temperatura == 'F'):
            print (MENSAJE_FAHRENHEIT)
            fn.mostrarLista(temperaturaCorporalFahrenheit)
        elif (opcion_temperatura == 'K') :
            print(MENSAJE_KELVIN)
            fn.mostrarLista(temperaturaCorporalKelvin)
        else :
            print(MENSAJE_ERROR_ENTRADA)
    #------------------Opción 2---------------#
    elif (opcion_escogida == 2 ) :
        print('Mostrando clasificación')
        print('ºC','\t','Clasificación')
        fn.mostrar2Lista(temperaturaCorporal, clasificacionTemperaturas)
    #-------------------Opción 3--------------#
    elif (opcion_escogida == 3) :
        ct.mostrarTopes(temperaturaCorporal)
    #------------------Opción no válida------------#
    else :
        print (MENSAJE_ERROR_ENTRADA)
    opcion_escogida =int(input(PREGUNTA_NUMERO))
print(MENSAJE_DESPEDIDA)