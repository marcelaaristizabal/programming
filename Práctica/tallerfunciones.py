#Dada una lista, mostrarla elemento a elemento (función sin entradas).

def MostrarLista (lista):   
    for elemento in lista:
        print (elemento)
frutas=['manzana','piña','pera','papaya','mango']
peso= [280,308,28,159,86]
MostrarLista (frutas)
MostrarLista (peso)

#Dada una lista de números enteros, mostrar el número mayor, el número menor y el promedio.

def lista_numeros (lista):
    NUMERO_MAYOR = max (lista)
    NUMERO_MENOR = min (lista)
    cantidad = 0
    for elemento in lista:
        cantidad += elemento
    total= len (lista)
    PROMEDIO = cantidad / total
    print(f'El número mayor es {NUMERO_MAYOR},El número menor es {NUMERO_MENOR} y El promedio es {PROMEDIO}')
numeros = [16,68,13,29,4,30,6,15]
lista_numeros(numeros)

#Saludar 'n' veces

PREGUNTA_NOMBRE =' ¿Cómo te llamas? '
NOMBRE = input(PREGUNTA_NOMBRE)
PREGUNTAR_SALUDO = f'''
        ¡Hola,{NOMBRE}!
        En este programa debes insertar un número entero,
        la idea es que sea la cantidad de veces 
        que quieras ser saludado
        ...
        ¿Cuántas veces deseas que te salude? Ingresa la cantidad :
'''
n = int (input(PREGUNTAR_SALUDO))
saludo = f'Hola {NOMBRE}. ¿Cómo estás?'
def saludar (saludo=0,n=0):
    return saludo * n
    for elemento in lista:
        print (elemento)

print(saludar(saludo,n))

#Devolver números pares de una lista de números enteros

PREGUNTA_OPCION = '''
            Hola,nuevamente...Ahora podrás ingresar una lista de números (dentro de un rango que podrás escoger). 
            Pero solamente te mostraré los números que sean pares.
            Ingrese las siguientes opciones :
            1- Para escribir su lista de números.
            2- Salir.
'''
MENSAJE_DESPEDIDA = 'Muchas gracias por su participación. Que tenga un buen día.'
opcion_escogida= int (input(PREGUNTA_OPCION))
MENSAJE_ERROR =' Ingrese una opción válida.'
PREGUNTA_CANTIDAD = ''' 
    ¿Cuántos números deseas ingresar a tu lista ? :
    a- 5
    b- 9
    c- 11
    d- 13
'''
INGRESO_LISTA = 'Ingrese su lista de números : '
#lista = int (input(INGRESO_LISTA)) 
total = 0
def par (lista) :
    pares = []
    for elemento in lista :
        if (elemento % 2 == 0):
            pares.append (elemento)
            print(elemento)

if (opcion_escogida == 1):
    cantidad_lista = input(PREGUNTA_CANTIDAD)
    while (cantidad_lista != 'a' and cantidad_lista != 'b' and cantidad_lista != 'c' and cantidad_lista != 'd') :
        print(MENSAJE_ERROR)
        cantidad_lista = (input(PREGUNTA_CANTIDAD))
    if (cantidad_lista == 'a'):
        total= 5
    elif (cantidad_lista == 'b' ) :
        total = 9
    elif (cantidad_lista == 'c') :
        total = 11
    else:
        total = 13
    lista_ingresados = [0] * total
    for i in range (len(lista_ingresados)):
        lista_ingresados [i] =int (input(INGRESO_LISTA))
    print('Los números pares de tu lista son :' )
    par (lista_ingresados)

#Devolver únicamente elementos mayores a 24. (Tras el punto anterior).
MENSAJE_ADVERTENCIA ='En la siguiente fase vas a crear una lista (la cantidad que quieras), pero solo te mostraré aquellos que sean mayores de 24.'
def mayor (lista):
    mayores =[]
    for elemento in lista:
        if (elemento > 24):
            mayores.append (elemento)
    print(mayores)
    return mayores

PREGUNTA_CANTIDAD_2 = '¿Cuántos números deseas ingresar a tu lista ? : '
cantidad_lista = int(input(PREGUNTA_CANTIDAD_2))
lista_ingresados = [0] * cantidad_lista
for i in range (len(lista_ingresados)):
    lista_ingresados [i] =int (input(INGRESO_LISTA))
print('Los números mayores de 24 de tu lista son :' )
mayor (lista_ingresados)

#Función que calcule el IMC.

MENSAJE_BIENVENIDA = "Hola ¿cómo estás? Voy a calcular tu IMC"
PREGUNTA_PESO = "¿Cuánto pesas en kg? : "
PREGUNTA_ESTATURA = "¿Cuánto mides en metros? : "

print (MENSAJE_BIENVENIDA)
peso = float (input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
def calcularIMC (peso, estatura):
    return peso/(estatura**2)
imc = calcularIMC(peso, estatura)
MENSAJE_DESPEDIDA = f"Tu IMC es ...{imc}"
print (MENSAJE_DESPEDIDA)

#Función de despedida.

NOMBRE = input (PREGUNTA_NOMBRE)
PREGUNTA_NOMBRE =' ¿Cómo te llamas? '
def despedir (NOMBRE):
    despedida = f'Hasta luego,{NOMBRE}. Ten un bonito día.'
    return despedida
print (despedir(NOMBRE))