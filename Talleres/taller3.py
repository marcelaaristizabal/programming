# Dado dos números deteminar si estos son iguales o cual es mayor
#----Preguntas----#
PREGUNTA_NUMERO_A= "Ingrese un número A : " 
PREGUNTA_NUMERO_B= "Ingrese un número B : "

#----Mensajes----#
MENSAJE_BIENVENIDA = "Hola,es un placer interactuar contigo.Espero que estés bien"
MENSAJE_MAYOR_A = "El número A es mayor que el número B"
MENSAJE_MAYOR_B = "El número B es mayor que el número A"
MENSAJE_IGUAL = "Los números A y B son iguales"

#----Entradas al código----#
print (MENSAJE_BIENVENIDA)
numeroA = int (input(PREGUNTA_NUMERO_A))
numeroB = int (input(PREGUNTA_NUMERO_B))
isMayor_A = numeroA > numeroB
isMayor_B = numeroB > numeroA
isNumerosIguales = numeroA == numeroB
resultado = ""
if (isMayor_A) :
    resultado = MENSAJE_MAYOR_A
elif (isMayor_B) :
    resultado = MENSAJE_MAYOR_B
else :
    resultado = MENSAJE_IGUAL

print (resultado)

# Pedir la edad del usuario y determinar ciertos parámetros
#----Preguntas----#
PREGUNTA_EDAD = "¿ Cuántos años tienes ? :"

#----Mensajes----#
MENSAJE_MENOR_EDAD = "Aún eres un adolescente. Te falta mucho por vivir,muchacho."
MENSAJE_JOVEN = "Aún eres joven. Te falta mucho por vivir,no te quejes de la vida.Vívela."
MENSAJE_ADULTO = "Mi señ@r. La vida no es fácil"
MENSAJE_ADULTO_MAYOR = "Madurar y envejecer es parte de la vida.Gracias por su colaboración."
MENSAJE_BIENVENIDA = "Hola,de nuevo. Espero que te encuentres bien."

#----Entradas al código----#
print (MENSAJE_BIENVENIDA)
edad = int (input (PREGUNTA_EDAD))
IsMenor_Edad = edad < 18 
IsJoven = edad >= 18 and edad < 26
IsAdulto = edad >= 26 and edad < 60
isAdulto_Mayor = edad >= 60
resultado = ""

#----Condicionales----#
if (IsMenor_Edad) :
    resultado = MENSAJE_MENOR_EDAD
elif (IsJoven) :
    resultado = MENSAJE_JOVEN
elif (IsAdulto) :
    resultado = MENSAJE_ADULTO
else :
    resultado = MENSAJE_ADULTO_MAYOR

print (resultado)

# Programa que pida año actual y año cualquiera.Descripción de años concurridos o faltantes para llegar a él.
#----Preguntas----#
PREGUNTA_AÑO_ACTUAL = "Ingrese año en el que nos encontramos actualmente : "
PREGUNTA_AÑO_CUALQUIERA = "Ingrese año que desee : "

#----Mensajes----#
MENSAJE_BIENVENIDA = "Hola. Bienvenido a la calculadora del tiempo"

#----Entradas al código----#
print (MENSAJE_BIENVENIDA)
año_actual = int (input(PREGUNTA_AÑO_ACTUAL))
año_cualquiera = int (input (PREGUNTA_AÑO_CUALQUIERA))

#----Condicionales----#
if ( año_actual > año_cualquiera) : 
    restar_mayor= año_actual - año_cualquiera
    print( f"Han pasado {restar_mayor} años desde el año {año_cualquiera}" )

elif (año_cualquiera> año_actual) :
    restar_menor = año_cualquiera - año_actual
    print ( f"Faltan {restar_menor} años para llegar al año {año_cualquiera}" )

# Programa que pida una distancia en centímetros que escriba esa distancia en kilómetros, metros y centímetros.
#----Preguntas----#
PREGUNTA_MEDIDA = "Ingrese una medida en centímetros : "
PREGUNTA_UNIDAD = ''' Ingrese unidad a la que desee transformar : 
km - kilometros 
m - metros 
cm - centimetros 
''' 

#----Entradas al código----#
medida = float (input(PREGUNTA_MEDIDA))
unidad = input (PREGUNTA_UNIDAD)

#----Mensajes----#
MENSAJE_ERROR = "Entrada no válida"

#----Conversiones----#
metros = medida * 10**-2
kilometros = medida * 10**-5
centimetros = medida

#---Condicionales----#
if (unidad == 'km') :
    print (kilometros)
elif (unidad == 'm') :
    print (metros)
elif (unidad == 'cm'):
    print (centimetros)
else :
    print (MENSAJE_ERROR)