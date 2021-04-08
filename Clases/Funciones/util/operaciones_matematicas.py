#------------------Sumar 2 números-----------------------#
def sumar (a = 0 ,b = 0):
    '''
        Devuelve la suma de dos números A y B.
        Por defecto, A vale 0 al igual que B.
    '''
    suma = a + b
    return suma
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
def calcular (operacion, numeroA,numeroB):
    print (operacion(numeroA,numeroB))