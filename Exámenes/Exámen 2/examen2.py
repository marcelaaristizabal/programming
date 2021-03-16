#Temperatura Corporal
listaCentigrados = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

PREGUNTA_NUMERO = ''' Ingrese alguna de estas opciones 
    1. Hacer conversión de grados centígrados a Kelvin o Fahreheit
    2. Mostrar lista de temperaturas (hipotermia,temperatura normal o fiebre)
    3. Mostrar estado de temperatura máxima,mínima y promedio de tomas de temperatura'
    4. Salir
'''
PREGUNTA_TEMPERATURA ='''
    F- Mostrar en grados Fahrenheit
    K- Mostrar en temperatura a escala Kelvin
    C- No es necesaria la conversión
'''
PREGUNTAR_TEMPERATURA = 'Ingrese la temperatura en ºC : '
MENSAJE_CENTIGRADOS = 'No es necesaria la conversión.Mostrando lista original'
MENSAJE_FAHRENHEIT = 'Mostrando lista de temperaturas en grados Fahrenheit'
MENSAJE_KELVIN ='Mostrando lista en escala Kelvin'
MENSAJE_MAXIMA='La temperatura máxima es  ---> '
MENSAJE_MINIMA ='La temperatura mínima es  ---> '
MENSAJE_HIPOTERMIA = 'PRECAUCIÓN: Muy baja temperatura. Probrablemente sea hipotermia'
MENSAJE_FIEBRE= '¡CUIDADO! Muy alta temperatura.Si no baja pronto,causará el paciente puede convulsionar.'
MENSAJE_TEMPERATURA_NORMAL = 'No hay de qué preocuparse. La temperatura está normal'
MENSAJE_ERROR = 'INGRESO NO VÁLIDO'
MENSAJE_DESPEDIDA = 'Gracias por usar el programa. Que tengas un feliz día.'

listaDiagnostico = []

#Conversión de temperatura punto 1 
promedio = 24 / len (listaCentigrados)
MENSAJE_PROMEDIO = f'La toma de temperatura promedio fue cada {promedio} horas'
listaKelvin = []
for temperatura in listaCentigrados:
    kelvin = temperatura + 273.15
    listaKelvin.append(kelvin)

listaFahrenheit = []
for temperatura in listaCentigrados:
    fahrenheit = (temperatura * 1.8)+ 32
    listaFahrenheit.append (fahrenheit)

opcion_escogida= int(input(PREGUNTA_NUMERO))
while (opcion_escogida != 4) :
    #----------------Opción1----------------#
    if (opcion_escogida == 1) :
        opcion_temperatura = input(PREGUNTA_TEMPERATURA)
        if (opcion_temperatura == 'F') :
            print(MENSAJE_FAHRENHEIT)
            print (listaFahrenheit)
        elif (opcion_temperatura == 'K'):
            print (MENSAJE_KELVIN)
            print(listaKelvin)
        elif (opcion_temperatura == 'C') :
            print(MENSAJE_CENTIGRADOS)
            print (listaCentigrados)
        else :
            print(MENSAJE_ERROR)
    #----------------Opción 2 ---------------#
    elif (opcion_escogida == 2):
        temperatura_ingresada = float (input(PREGUNTAR_TEMPERATURA))
        for temperatura in listaCentigrados:
            diagnostico= ''
            if (temperatura < 36):
                diagnostico= 'PRECAUCIÓN: Muy baja temperatura. Probrablemente sea hipotermia'
            elif (temperatura >= 37.6):
                diagnostico = '¡CUIDADO! Muy alta temperatura.Si no baja pronto,el paciente puede convulsionar.'
            else :
                diagnostico = 'No hay de qué preocuparse. La temperatura está normal'
            listaDiagnostico.append (diagnostico)
        print (listaDiagnostico)
    #-----------------Opción 3 ------------------#
    elif (opcion_escogida == 3):
        temperatura_maxima = max (listaCentigrados)
        temperatura_minima= min (listaCentigrados)
        print (MENSAJE_MAXIMA,temperatura_maxima)
        print (MENSAJE_MINIMA, temperatura_minima)
        acumulado =0
        for temperatura in listaCentigrados:
            acumulado += temperatura
        promedio = 24 / len (listaCentigrados)
        print(MENSAJE_PROMEDIO)
    #--------------Opción NO VALIDA--------------#
    else :
        print (MENSAJE_ERROR)
    opcion_escogida =int(input(PREGUNTA_NUMERO))
print (MENSAJE_DESPEDIDA)