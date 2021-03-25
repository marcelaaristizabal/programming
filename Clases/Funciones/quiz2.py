import conversorTemperatura as ct 
import funciones as fn
PREGUNTA_NUMERO = ''' Ingrese alguna de estas opciones 
    1. Convertir temperaturas
    2. Mostrar clasificación
    3. Mostrar topes
    4. Salir
'''
PREGUNTA_MONEDA ='''
    K- Mostrar Kelvin
    F- Mostrar  Fahrenheit
    C- Mostrar Celsius
'''

MENSAJE_CELSIUS = 'Mostrando lista original. No es necesaria la conversión.'
MENSAJE_FAHRENHEIT = 'Mostrando lista en Fahrenheit'
MENSAJE_KELVIN ='Mostrando lista en Kelvin'
MENSAJE_DESPEDIDA = 'Que tengas un feliz día'

temperaturaCorporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
opcion_escogida= int(input(PREGUNTA_NUMERO))
while (opcion_escogida != 4 ):
    #----------------Opción1----------------#
    if (opcion_escogida == 1) :
        opcion_temperatura = input(PREGUNTA_MONEDA)
        if (opcion_temperatura== 'C') :
            print(MENSAJE_CELSIUS)
            print (temperaturaCorporal)
        elif (opcion_temperatura == 'F'):
            print (MENSAJE_FAHRENHEIT)
            print(temperaturaCorporalFahrenheit)
        elif (opcion_temperatura == 'K') :
            print(MENSAJE_KELVIN)
            print (temperaturaCorporalKelvin)
        else :
            print(MENSAJE_ERROR)
    #------------------Opción 2---------------#
    elif (opcion_escogida == 2 ) :
        valor_ingresado = float (input(PREGUNTAR_NUMERO))
        listaPesos.append (valor_ingresado)
        print (listaPesos)
    #-------------------Opción 3--------------#
    elif (opcion_escogida == 3) :
        print (MENSAJE_MAYOR, max(listaPesos))
        print (MENSAJE_MENOR, min(listaPesos))
        print (MENSAJE_PROMEDIO, sum(listaPesos)/len (listaPesos))
    #-------------------Opción 4 ------------#
    elif (opcion_escogida == 4) :
        posicion = int (input(PREGUNTA_BORRAR_COORDENADA)) - 1
        print (listaPesos)
        listaPesos.pop (posicion)
        print (listaPesos)
    #------------------Opción no válida------------#
    else :
        print (MENSAJE_ERROR)
    opcion_escogida =int(input(PREGUNTA_NUMERO))
temperaturaCorporalFahrenheit = ct.conversionTemperatura(temperaturaCorporal, 'F')
temperaturaCorporalKelvin = ct.conversionTemperatura(temperaturaCorporal, 'K')
clasificaciónTemperaturas = ct.clasificarTemperaturas(temperaturaCorporal)
fn.linedesing(60, "")
print (temperaturaCorporalFahrenheit)
fn.linedesing(60, "#")
print (temperaturaCorporalKelvin)
fn.linedesing(60, "#")
print(clasificaciónTemperaturas)