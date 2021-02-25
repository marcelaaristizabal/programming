#----Mensajes----#
MENSAJE_SALUDAR ='¡Bienvenido! Te apoyaré ahorrando'
MENSAJE_AHORRO = 'LLEVAS AHORRADO...'
PREGUNTAR_VALOR_CPU = '¿ Cuánto vale el PC que deseas ? : '
PREGUNTAR_CUANTO_TIENE = '¿ Cuánto tienes ahorrado? : '

#----Entradas----#
print (MENSAJE_SALUDAR)
valor = float (input(PREGUNTAR_VALOR_CPU))
ahorrado = float (input (PREGUNTAR_CUANTO_TIENE))

while (valor > ahorrado) :
    print (MENSAJE_AHORRO, ahorrado ,"Te faltan...",valor - ahorrado)
    ahorrado = ahorrado + 1000
print (valor == ahorrado)