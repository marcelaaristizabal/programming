guardar = print ('Hola')
print (guardar)

guardar = round(14.2534897,2)
print(guardar)

def linedesing (cantidad = 10 , simbolo= '#' ):
    print (simbolo * cantidad)
    return None 

linedesing(30, '#')
linedesing(10, '*')
linedesing(100,'')


#----------------Mostrar la lista-----------------#
def mostrarlista (listaEntrada= []):
    for elemento in listaEntrada:
        print (elemento)
    return None
lista = [213,32,23123,321,321,233,1232,23]
lista2= [564654,645,64543,2565,547,57865]
linedesing(30,'☺')
mostrarlista(lista)
linedesing(3,'(⊃｡•́‿•̀｡)⊃' )
mostrarlista(lista)
#------------------Sumar 2 números-----------------------#
def sumar (a = 0 ,b = 0):
    suma = a + b
    return suma
linedesing(30,'⌘')
resultado = sumar ()
print (resultado)
print (sumar(12,14))
round (12.234897,2)
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

print(restar(83,87))
print(multiplicar(83,87))
print(dividir(83,87))
print(dividir())

calcular (multiplicar, 63,67)