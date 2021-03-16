listaCentigrados = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
listaDiagnostico = []
PREGUNTAR_TEMPERATURA = 'Ingrese la temperatura en ºC : '
if (opcion_escogida == 2):
    temperatura_ingresada = float (input(PREGUNTAR_TEMPERATURA))
    for temperatura in listaCentigrados:
        diagnostico= ''
        if (temperatura < 36):
            diagnostico= 'PRECAUCIÓN: Muy baja temperatura. Probrablemente sea hipotermia'
        elif (temperatura >= 37.6):
                diagnostico = '¡CUIDADO! Muy alta temperatura.Si no baja pronto,causará el paciente puede convulsionar.'
        else :
                diagnostico = 'No hay de qué preocuparse. La temperatura está normal'
        listaDiagnostico.append (diagnostico)
        print (listaClasificacion)