def calculadora (accion,valor1,valor2,valor3):
    print(accion(valor1,valor2,valor3))
#------------------Sumar 3 números-----------------------#
def sumar (valor1 = 0 ,valor2 = 0,valor3 = 0): 
    '''
        Devuelve la suma de tres números A, B y C.
        Por defecto, A vale 0 al igual que B y C.
    '''
    suma = valor1 + valor2 + valor3
    return suma
#------------------Restar 3 números-----------------------#
def restar (valor1= 0 ,valor2 = 0,valor3 = 0):
    '''
        Devuelve la resta de tres números A, B y C.
        Por defecto, A vale 0 al igual que B y C.
    '''
    resta= valor1 - valor2 - valor3
    return resta
#------------------Multiplicar 3 números-----------------------#
def multiplicar (valor1 = 0,valor2 = 0,valor3 = 0):
    '''
        Devuelve la multiplicación de tres números A, B y C.
        Por defecto, A vale 0 al igual que B y C.
    '''
    multiplica = valor1 * valor2 * valor3
    return multiplica
#------------------Dividir 3 números-----------------------#
def dividir (valor1= 0 ,valor2 = 1, valor3 = 1):
    '''
        Devuelve la división entre dos números A, B y C.
        Por defecto, A vale 0, B y C valen 1 (B != 0 y C != 0).
    '''
    dividi = valor1 / valor2 / valor3
    return dividi

PREGUNTA_EXPONENTE= 'Ingresa un número que quieras calcular (exponente) dado una base que elijas : '
PREGUNTA_EXPONENTE_2= 'Ingresa otro número que quieras calcular (exponente) dado una base que elijas : '
PREGUNTA_BASE = 'Ingresa una base que quieras calcular : '
numero_base = int (input(PREGUNTA_BASE))
numero_exponente = int (input(PREGUNTA_EXPONENTE))
def potenciar (valor1= 0 ,valor2= 1,valor3 = 1) :
    '''
        Devuelve la potenciación de una base A y unos exponentes B y C.
        Se puede ingresar la base y los exponentes (diferentes o iguales). 
        Pero por defecto, A vale 0,B y C valen 1.
    '''
    potencia = (valor1 ** valor2)**valor3
    return potencia
calculadora(sumar, 3, 6, 7)
calculadora(restar, 4, 8, 9)
calculadora(multiplicar, 4, 12, 15)
calculadora(dividir, 5, 7, 9)
calculadora(potenciar, 3, 7,9 )

nombres =['Mariana','Juanita','Carolina','Santiago','Gerónimo']
apellidos =['Restrespo','Castrillón','Contreras','Castaño','Aristizábal']
edades = [18,20,16,37,16]
print('Mostrando listas')
print( 'Nombre' , '\t' , 'Apellido' , '\t' , 'Edad' )
def mostrar3Lista (lista1, lista2,lista3):
    for i in range (len(lista1)):
        print(lista1 [i], '\t' , lista2 [i] , '\t' , lista3 [i])
mostrar3Lista(nombres,apellidos,edades)

PREGUNTA_BASET= 'Ingresa un número entero (en metros) que será la base para el área de un triángulo : '
PREGUNTA_ALTURA= 'Ingresa otro número entero (en metros ) que será la altura de un triángulo : '    
MENSAJE_AREA='''
        Devuelve el área de un triángulo de base A y altura B.
        Se puede ingresar la base y la altura (diferentes o iguales). 
        Pero por defecto, la base vale 0 y la altura vale 1.
    '''

area = (base*altura)/2
def calcularArea (base = 1,altura =1 ) :
    base = int (input(PREGUNTA_BASET))
    altura = int (input(PREGUNTA_ALTURA))
    MENSAJE_AREA='''
        Devuelve el área de un triángulo de base A y altura B.
        Se puede ingresar la base y la altura (diferentes o iguales). 
        Pero por defecto, la base vale 0 y la altura vale 1.
    '''
    area = (base*altura)/2
    print(area)
calcularArea(base,altura)
calcularArea(2,3)

lista = [12,54,89,14,37,36,27,43]
mayor = max (lista)
sumatoria = 0
menor = min (lista)
promedioLista = sum(lista) / len(lista)
MENSAJE_MAXIMO =f'El dato mayor de la lista es {mayor}'
MENSAJE_MINIMO=f'El dato menor de la lista es {menor}'
MENSAJE_PROMEDIO =f'El promedio de todos los datos de la lista es {promedioLista}'

def mostrarTopes (lista):
    sumatoria = 0
    mayor =max (lista)
    print(MENSAJE_MAXIMO)
    menor = min (lista)
    print(MENSAJE_MINIMO)
    acumulado = 0
    for elemento in lista:
        acumulado += elemento
    promedioLista = sum(lista) / len(lista)
    print(MENSAJE_PROMEDIO)
mostrarTopes(lista)


PREGUNTA_n = 'Ingresa la posición (entero) que quieras saber de la Sucensión de Fibonacci : '
n_fib= int(input(PREGUNTA_n))
fn = fibonacci(n-1) + fibonacci(n-2)
def fibonacci (n):
    if (n < 2):
        return n
    else:
        #Fórmula de Fibonacci:
        # fn = fn-1 + fn-2
        fn = fibonacci(n-1) + fibonacci(n-2)
        print(fn)
fibonacci(10)