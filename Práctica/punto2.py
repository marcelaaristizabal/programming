import sys
MENSAJE_PARRAFO = '''Ingresa un párrafo del tema que desees. Pero la condición es que al finalizar debes agregarle un punto (.)
            Agrega tu párrafo : 
            '''
isCorrectInfo = False
usuarioParrafo = ' '

while (isCorrectInfo == False):
    usuarioParrafo = input(MENSAJE_PARRAFO)
    isCorrectInfo = usuarioParrafo.endswith(' . ')

    if (isCorrectInfo == False):
        print ('Recuerda que debe terminar con un punto "." . Intentalo nuevamente.')
        print (usuarioParrafo.endswith ("."))