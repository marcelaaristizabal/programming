#------------------Sumar 2 números-----------------------#
def sumar (a = 0 ,b = 0):
    '''
        devuelve la suma de dos números A y B
        por defecto a vale 0 al igual que b
    '''
    suma = a + b
    return suma

#------------------Restar 2 números-----------------------#
def restar (a = 0 ,b = 0):
    resta= a - b
    return resta
#------------------Multiplicar 2 números-----------------------#
def multiplicar (a = 0 ,b = 0):
    multiplica = a * b
    return multiplica
#------------------Dividir 2 números-----------------------#
def dividir (a = 0 ,b = 1):
    dividi = a / b
    return dividi
#------------------Elevar a una potencia un número------------------#
PREGUNTA_EXPONENTE= 'Ingresa un número que quieras calcular (exponente) dado una base que elijas : '
PREGUNTA_BASE = 'Ingresa una base que quieras calcular : '
numero_base = int (input(PREGUNTA_BASE))
numero_exponente = int (input(PREGUNTA_EXPONENTE))
def potenciar (base = 0 ,exponente = 1):
    potencia = base ** exponente
    return potencia
print (potenciar (numero_base, numero_exponente))
#-----------------Funciones que dependen de otras----------------------#
def calcular (operacion, numeroA,numeroB):
    print (operacion(numeroA,numeroB))