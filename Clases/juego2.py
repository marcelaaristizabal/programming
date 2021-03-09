
import random
#----Entradas----#
MENSAJE_SALUDAR = '''
    Bienvenido a 
        este programa. 
    ¡¡¡Juguemos!!!'''
MENSAJE_SEGUNDO_NIVEL = ' Feliciddes,pasate el primer nivel.¡Ahora ve por el último!'
MENSAJE_CALIENTE = '¡¡Estás caliente!!'
MENSAJE_FRIO = 'Estás frío...'
PREGUNTAR_NUMERO = '''
        En este juego debes insertar un número entero
        que va desde el 1-10, la idea es que
        lo puedes intentar antes de que se te
        acaben las vidas. No existe vida 0.
        Muchos éxitos.Ingresa tu número :
'''
PREGUNTA_DIFICULTAD = '''
    1- Fácil
    2- Moderadp
    3- Difícil
'''
PREGUNTA_FALLIDA = 'Ahhhhh fallaste...Ingresa otro número : '
MENSAJE_GANASTE = '¡¡¡Felicidades,ganaste!!!'
MENSAJE_PERDISTE = 'Perdiste D: . Vuelve a intentarlo ...'
#----Entrada al código----#
numeroOculto = random.randint (1,10)
numeroOcultoDos = random.randint (1,10)
vidas = None


dificultad = int(input(PREGUNTA_DIFICULTAD))
while (dificultad != 1 and dificultad != 2 and dificultad != 3) :
    print ('Ingresa una opción válida')
    dificultad =int (input (PREGUNTA_DIFICULTAD))


if (dificultad == 1):
    print (' Modo fácil activado')
    vidas = 10
elif (dificultad == 2 ) :
    vidas = 5
    print ('Modo moderado activado')
else :
    print ('Modo difícil activado...¡Mucho cuidado!')
    vidas = 2

numeroIngresado = int (input (PREGUNTAR_NUMERO))
while (numeroIngresado != numeroOculto and vidas > 1 ) :
    if (numeroIngresado > numeroOculto) :
        print(MENSAJE_CALIENTE)
    else:
        print(MENSAJE_FRIO)
    vidas -= 1
    print (f'Te quedan {vidas} vidas')
    numeroIngresado = int(input(PREGUNTA_FALLIDA))
if (vidas >= 0 and numeroIngresado == numeroOculto) :
    print (MENSAJE_SEGUNDO_NIVEL)
    numeroIngresado = int(input(PREGUNTAR_NUMERO))
    while (numeroIngresado != numeroOcultoDos and vidas > 1):
        if (numeroIngresado > numeroOcultoDos) :
            print(MENSAJE_CALIENTE)
        else :
            print(MENSAJE_FRIO)
        vidas -=1
        print(f'Te quedan {vidas} vidas')
        numeroIngresado = int(input(PREGUNTA_FALLIDA))


if (vidas >= 0 and numeroIngresado == numeroOcultoDos ) :
    print (MENSAJE_GANASTE)

else: 
    print (MENSAJE_PERDISTE ,
                            'El numero uno era el ',
                            numeroOculto,
                            'El número dos era el ',
                            numeroOcultoDos)