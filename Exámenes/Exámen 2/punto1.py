listaCentigrados = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
PREGUNTA_TEMPERATURA ='''
    F- Mostrar en grados Fahrenheit
    K- Mostrar en temperatura a escala Kelvin
    C- No es necesaria la conversión
'''
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



