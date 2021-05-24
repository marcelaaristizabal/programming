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
    except ZeroDivisionError:
        print ('El divisor (estatura) ingresado es igual a 0. Por lo tanto,es imposible ejecutar el cálculo de tu IMC.')
PREGUNTA_NOMBRE ='Por favor,ingrese su nombre : '
nombre= (input(PREGUNTA_NOMBRE))
MENSAJE_BAJO_PESO = f'CUIDADO: Estás en infrapeso,{nombre}. Alimentante bien y haz mucho ejercicio.'
MENSAJE_NORMAL = f'¡Muy bien {nombre}!. Estás en forma,sigue así.'
MENSAJE_SOBRE_PESO = f'PRECAUCIÓN:Ten cuidado {nombre}.Estás en sobre peso. ' 
MENSAJE_OBESO = f'ALTO RIESGO: Cuidate mucho, {nombre} ya estás obeso. Tu salud corre peligro.'
imc = peso/(estatura**2)
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

isCorrectInfo = False
while (isCorrectInfo == False):
    try : 
        PREGUNTA_NOMBRE ='Por favor,ingrese su nombre : '
        nombre= (input(PREGUNTA_NOMBRE))
        assert (nombre.isalpha())
        isCorrectInfo = True
    except AssertionError: 
            print ('Ingresaste un dato no válido')
