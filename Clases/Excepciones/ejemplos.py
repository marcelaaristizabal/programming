
isCorrectInfo = False
while (isCorrectInfo == False):
    try : 
        nombre = (input('Ingrese su nombre : '))
        isCorrectInfo = True
    except ValueError: #Capturan los tipos de error.Se captura si hay un error a la hora de ingresar ese valor (sin descontrolarse)
        print ('Ingresaste un dato no válido')
nombreArchivo =input ('Ingrese el nombre del archivo que desea encontrar : ')
try:
    archivo = open(nombreArchivo)
except FileNotFoundError: #El programa puede cerrarse sin ningun error.
    print (f'El archivo {nombreArchivo} no se ha encontrado')

base = 4 
divisor = 0
try: #Try y Except para cada input en el Parcial.
    dividir = base/ divisor 
except ZeroDivisionError:
    print ('El divisor ingresado es igual a 0. Por lo tanto,es imposible ejecutar la división.')

nombre = 'Marcela'
print (nombre.isalpha())
assert (nombre.isalpha()) #cuando se necesita en el código que las cosas sean iguales para poder seguir.

isCorrectInfo = False
while (isCorrectInfo == False):
    try : 
        nombre= (input('Ingrese su nombre : '))
        assert (nombre.isalpha())
        isCorrectInfo = True
    except AssertionError: #Capturan los tipos de error.Se captura si hay un error a la hora de ingresar ese valor (sin descontrolarse)
        print ('Ingresaste un dato no válido')

isCorrectInfo = False
while (isCorrectInfo == False):
    try : 
        edad = int (input('Ingrese su edad : '))
        assert (edad >= 18)
        isCorrectInfo = True
    except AssertionError: #Capturan los tipos de error.Se captura si hay un error a la hora de ingresar ese valor (sin descontrolarse)
        print ('Los menores de edad no pueden acceder.')
    except ValueError:
        print ('Las edades son números enteros.')

listas = [2,43,42,4]
try: 
    listas [5]
except IndexError:
    print ('Este índice no existe.Es mayor al tamaño de la lista.')
