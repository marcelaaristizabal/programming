#----Preguntas----#
PREGUNTA_NUMERO = ''' Ingrese alguna de estas opciones 
    1. Hacer conversión de pesos a Dólares o Euros
    2. Agregue un valor a la lista de pesos 
    3. Mostrar valor más alto,más bajo y promedio
    4. Eliminar elemento de la lista
    5. Salir
'''
PREGUNTA_MONEDA ='''
    C- Mostrar original en pesos colombianos 
    D- Mostrar en Dólares
    E- Mostrar en Euros
'''
PREGUNTAR_NUMERO = 'Ingrese un valor en COP : '
PREGUNTA_BORRAR_COORDENADA ='Ingrese la posición que desee borrar : '
#----Mensajes----#
MENSAJE_PESOS = 'Mostrando lista original'
MENSAJE_DOLARES = 'Mostrando lista en dólares'
MENSAJE_EURO ='Mostrando lista en euros'
MENSAJE_MAYOR ='El mayor número ingresado es ---> '
MENSAJE_MENOR ='El menor número ingresado es ---> '
MENSAJE_PROMEDIO ='El promedio es --->'
MENSAJE_DESPEDIDA = 'Que tengas uneliz día'
#----Error----#
MENSAJE_ERROR = 'INGRESO NO VÁLIDO'


listaPesos = [20000,30000,4000,2500,1000,7600]

#Conversión punto 1
listaEuros = []
for elemento in listaPesos:
    conversor = round(elemento*0.00023,2)
    listaEuros.append(conversor)
listaDolares = []
for elemento in listaDolares:
    conversor = round(elemento*0.00028,2)
    listaDolares.append(conversor)


opcion_escogida= int(input(PREGUNTA_NUMERO))
while (opcion_escogida != 5) :
    #----------------Opción1----------------#
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
        print ('Respuesta no válida')
    opcion_escogida =int(input(PREGUNTA_NUMERO))

print (MENSAJE_DESPEDIDA)