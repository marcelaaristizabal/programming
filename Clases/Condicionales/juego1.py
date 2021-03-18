#----Entradas----#
MENSAJE_SALUDAR = '''
    Bienvenido a 
        este programa. 
    ¡¡¡Juguemos!!!'''
PREGUNTAR_NUMERO = '''
        En este juego debes insertar un número entero
        que va desde el 1-10, la idea es que
        lo puedes intentar las veces que
        quieras ...
        Muchos éxitos.Ingresa tu número :
'''
PREGUNTA_FALLIDA = 'Ahhhhh fallaste...Ingresa otro número : '
MENSAJE_GANASTE = '¡¡¡Felicidades,ganaste!!!'
MENSAJE_PERDISTE = 'Perdiste D: . Vuelve a intentarlo ...'
#----Entrada al código----#
numeroOculto = 7
vidas = 5
print (MENSAJE_SALUDAR)
numeroIngresado = int (input (PREGUNTAR_NUMERO))
if (numeroIngresado != numeroOculto) :
    vidas -=1
while (numeroOculto != numeroIngresado and vidas > 0) :
    numeroIngresado = int (input (PREGUNTA_FALLIDA))
    vidas -=1

if (vidas >= 0 and numeroOculto == numeroIngresado) : 
    print (MENSAJE_GANASTE)
    print (vidas)
else :
    print (MENSAJE_PERDISTE, 'El número era el',numeroOculto)