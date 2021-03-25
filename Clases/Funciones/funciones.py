#------------------Sumar 2 números-----------------------#
def sumar (a = 0 ,b = 0):
    '''
        Devuelve la suma de dos números A y B.
        Por defecto, A vale 0 al igual que B.
    '''
    suma = a + b
    return suma
def linedesing (cantidad = 10 , simbolo= '#' ):
    print (simbolo * cantidad)
    return None 
#------------------Restar 2 números-----------------------#
def restar (a = 0 ,b = 0):
    '''
        Devuelve la resta de dos números A y B.
        Por defecto, A vale 0 al igual que B
    '''
    resta= a - b
    return resta
#------------------Multiplicar 2 números-----------------------#
def multiplicar (a = 0 ,b = 0):
    '''
        Devuelve la multiplicación de dos números A y B.
        Por defecto, A vale 0 al igual que B.
    '''
    multiplica = a * b
    return multiplica
#------------------Dividir 2 números-----------------------#
def dividir (a = 0 ,b = 1):
    '''
        Devuelve la división entre dos números A y B.
        Por defecto, A vale y B vale 1 (B != 0).
    '''
    dividi = a / b
    return dividi
#------------------Elevar a una potencia un número------------------#
PREGUNTA_EXPONENTE= 'Ingresa un número que quieras calcular (exponente) dado una base que elijas : '
PREGUNTA_BASE = 'Ingresa una base que quieras calcular : '
numero_base = int (input(PREGUNTA_BASE))
numero_exponente = int (input(PREGUNTA_EXPONENTE))
def potenciar (base = 0 ,exponente = 1):
    '''
        Devuelve la potenciación de una base A y un exponente B.
        Se puede ingresar la base y el exponente. 
        Pero por defecto, A vale 0 y B vale 1
    '''
    potencia = base ** exponente
    return potencia
print (potenciar (numero_base, numero_exponente))
#-----------------Funciones que dependen de otras----------------------#
def calcular (operacion, numeroA,numeroB):
    print (operacion(numeroA,numeroB))

def mostrarLista (lista)