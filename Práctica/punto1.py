
PREGUNTA_MONEDA ='''
    C- Mostrar original en pesos colombianos 
    D- Mostrar en Dólares
    E- Mostrar en Euros
'''
MENSAJE_PESOS = 'Mostrando lista original'
MENSAJE_DOLARES = 'Mostrando lista en dólares'
MENSAJE_EURO ='Mostrando lista en euros'
MENSAJE_ERROR = 'INGRESO NO VÁLIDO'

listaPesos = [20000,30000,4000,2500,1000,7600]

listaEuros = []
for elemento in listaPesos:
    conversor = round(elemento*0.00023,2)
    listaEuros.append(conversor)
listaDolares = []
for elemento in listaDolares:
    conversor = round(elemento*0.00028,2)
    listaDolares.append(conversor)

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

print('Feliz día')