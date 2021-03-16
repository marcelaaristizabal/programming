
PREGUNTA_NUMERO = ''' Ingrese alguna de estas opciones 
    1. Hacer conversión de Dólares a Pesos colombianos o Euros
    2. Mostrar lista de clasificación de ingresos mensuales (bajos,medios,altos y elevados) 
    3. Mostrar valor de ingreso más alto,más bajo y promedio de ingresos.
    4. Salir
'''
PREGUNTA_MONEDA ='''
    C- Mostrar en pesos colombianos
    D- Mostrar original en Dólares
    E- Mostrar en Euros
'''
#----Mensajes----#
MENSAJE_DOLARES = 'Mostrando lista original'
MENSAJE_PESOS = 'Mostrando lista en pesos colombianos'
MENSAJE_EURO ='Mostrando lista en euros'
MENSAJE_ERROR = 'INGRESO NO VÁLIDO'
MENSAJE_DESPEDIDA = 'Gracias por usar el programa. Que tengas un feliz día'
MENSAJE_INGRESOS_BAJOS = '¡Uyy! Estos ingresos son bajos--->'
MENSAJE_INGRESOS_MEDIOS = 'Bien. Estos ingresos son medios'
MENSAJE_INGRESOS_ALTOS ='¡Genial! Estos ingresos son altos'
MENSAJE_INGRESOS_ELEVADOS= '¡OMG! Estos si que son ingresos elevados--->'
MENSAJE_PROMEDIO= 'El promedio es --->'

listaDolares =  [20000,30000,4000,2500,1000,7600]

listaEuros = []
for elemento in listaDolares:
    euros = elemento * 0.84
    listaEuros.append(euros)
listaPesos = []
for elemento in listaDolares:
    pesos = elemento * 3700
    listaPesos.append(pesos)
listaClasificacion= []


opcion_escogida= int(input(PREGUNTA_NUMERO))
while (opcion_escogida != 4) :
    #----------------Opción 1----------------#
    if (opcion_escogida == 1) :
        opcion_moneda = input(PREGUNTA_MONEDA)
        if (opcion_moneda == 'C') :
            print(MENSAJE_PESOS)
            print (listaPesos)
        elif (opcion_moneda == 'D'):
            print (MENSAJE_DOLARES)
            print(listaDolares)
        elif (opcion_moneda == 'E') :
            print(MENSAJE_EURO)
            print (listaEuros)
        else :
            print(MENSAJE_ERROR)
    #-----------------Opción 2-----------------#
    elif (opcion_escogida == 2):
        for elemento in listaDolares :
            clasificacion = ''
            if (elemento < 1000 ):
                clasificacion = '¡Uyy! Estos ingresos son bajos'
            elif (elemento >= 1000 and elemento < 7000 ):
                clasificacion = 'Bien. Estos ingresos son medios'
            elif (elemento >= 7000 and elemento < 20000 ):
                clasificacion = '¡Genial! Estos ingresos son altos'
            else:
                clasificacion = '¡OMG! Estos si que son ingresos elevados'
            listaClasificacion.append (clasificacion)
        print (listaClasificacion)
    #-----------------Opción 3 ------------------#
    elif (opcion_escogida == 3):
        mas_alto = max (listaDolares)
        mas_bajo = min (listaDolares)
        print (MENSAJE_INGRESOS_ELEVADOS,mas_alto)
        print (MENSAJE_INGRESOS_BAJOS, mas_bajo)
        acumulado =0
        for elemento in listaDolares:
            acumulado += elemento
        promedio = sum (listaDolares)/len (listaDolares)
        promedio_dolares = round (promedio,2)
        print(MENSAJE_PROMEDIO,promedio_dolares)
    #-----------------Opcion 4----------------------#
    else:
        print (MENSAJE_ERROR)
    opcion_escogida = int(input(PREGUNTA_NUMERO))

print (MENSAJE_DESPEDIDA)