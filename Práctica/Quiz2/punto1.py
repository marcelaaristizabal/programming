


listaDolares = [20000,30000,4000,2500,1000,7600]

#Conversión punto 1
listaEuros = []
for elemento in listaDolares:
    conversor = round(elemento*0.84)
    listaEuros.append(conversor)
listaPesos = []
for elemento in listaPesos:
    conversor = round(elemento*3700)
    listaPesos.append(conversor)

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