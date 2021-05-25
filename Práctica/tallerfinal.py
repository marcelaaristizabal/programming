#Punto1.
MENSAJE_IMC = 'Hola, soy una calculadora del ÍNDICE DE MASA CORPORAL.Ahora calcularé el tuyo.'
print (MENSAJE_IMC)
PREGUNTA_ESTATURA = 'Ingresa tu estatura en metros (m) : '
PREGUNTA_PESO = ' Ingresa tu peso en kilogramos (kg) : '

isCorrectInfo = False
while (isCorrectInfo == False):
    try: 
        estatura = float (input(PREGUNTA_ESTATURA))
        isCorrectInfo = True
    except ValueError : 
        print ('Ingresaste un dato no válido. La estatura para calcular tu IMC debe ser un decimal (en metros)')
    try:
        peso = float (input(PREGUNTA_PESO))
        isCorrectInfo = True
    except ValueError:
        print ('Ingresaste un dato no válido. El peso para calcular tu IMC debe ser un número entero o decimal (en kilogramos).')
try:
    imc = peso/(estatura**2)
    isCorrectInfo = True
except ZeroDivisionError:
    print ('El divisor (estatura) ingresado es igual a 0. Por lo tanto,es imposible ejecutar el cálculo de tu IMC.')

isCorrectInfo = False
while (isCorrectInfo == False):
    try : 
        PREGUNTA_NOMBRE ='Por favor,ingrese su nombre : '
        nombre= (input(PREGUNTA_NOMBRE))
        assert (nombre.isalpha())
        isCorrectInfo = True
    except AssertionError: 
            print ('Ingresaste un dato no válido')
MENSAJE_DESPEDIDA = "Tu IMC es ..."
MENSAJE_BAJO_PESO = f'CUIDADO: Estás en infrapeso,{nombre}. Alimentante bien y haz mucho ejercicio.'
MENSAJE_NORMAL = f'¡Muy bien,{nombre}!. Estás en forma,sigue así.'
MENSAJE_SOBRE_PESO = f'PRECAUCIÓN:Ten cuidado {nombre}.Estás en sobre peso. ' 
MENSAJE_OBESO = f'ALTO RIESGO: Cuidate mucho, {nombre} ya estás obeso. Tu salud corre peligro.'
isBajoPeso = imc < 18.5
isNormal = imc >= 18.5 and imc < 25
isSobrePeso = imc >= 25 and imc < 30
resultado = ''
if (isBajoPeso) :
    resultado = MENSAJE_BAJO_PESO
elif (isNormal) :
    resultado = MENSAJE_NORMAL
elif (isSobrePeso) :
    resultado = MENSAJE_SOBRE_PESO
else :
    resultado = MENSAJE_OBESO
print (MENSAJE_DESPEDIDA, imc)
print (resultado)

#Punto2.
import sys
MENSAJE_PARRAFO = '''Ingresa un párrafo del tema que desees. Pero la condición es que al finalizar debes agregarle un punto (.)
            Agrega tu párrafo : 
            '''
usuarioParrafo = input(MENSAJE_PARRAFO)
nombreArchivo1 ='párrafoUsuario.txt'
try:
    archivo1 = open (nombreArchivo1)
    print ('1')
except FileNotFoundError:
    archivo1 = open (nombreArchivo1,'w',encoding= 'UTF-8' )
    descripcion = 'Párrafo generado por un usuario que está ejecutando este código.'
    print ('2')
    archivo1.writelines(descripcion)
    sys.exit (1)

archivo1 = open (nombreArchivo1,'a')
parrafo = '\n'+ usuarioParrafo
archivo1.writelines(parrafo)
archivo1.close()

isCorrectInfo = False
while (isCorrectInfo == False):
    try : 
        usuarioParrafo = parrafo
        isCorrectInfo = True
    except AssertionError: 
        print (parrafo.endwith (' . '))
usuarioParrafo = input(MENSAJE_PARRAFO)
#----->Palabra más grande y palabra más pequeña.
print (max(usuarioParrafo, key = len))
#Leer o ver en pantalla. 
with open (nombreArchivo1,'r') as reader:
    for line in reader:
        print(line)


#Punto3.
import sys
nombreArchivo2 ='mantenimientos.txt'
try:
    archivo2 = open (nombreArchivo2)
    print ('1')
except FileNotFoundError:
    archivo1 = open (nombreArchivo2,'w',encoding= 'UTF-8' )
    descripcion = 'Párrafo generado por un usuario que está ejecutando este código.'
    print ('2')
    archivo2.writelines(descripcion)
    sys.exit (1)

archivo1 = open (nombreArchivo1,'a')
parrafo = '\n'+ usuarioParrafo
archivo1.writelines(parrafo)
archivo1.close()
