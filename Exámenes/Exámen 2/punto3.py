    #-----------------Opción 3 ------------------#
if (opcion_escogida == 3):
    temperatura_maxima = max (listaCentigrados)
    temperatura_minima= min (listaCentigrados)
    print (MENSAJE_MAXIMA,temperatura_maxima)
    print (MENSAJE_MINIMA, temperatura_minima)
    acumulado =0
    for temperatura in listaCentigrados:
        acumulado += temperatura
        promedio = 24 / len (listaCentigrados)
        print(MENSAJE_PROMEDIO,promedio)