#Punto1--> Calcular el IMC de un usuario, pero valide que los datos de entrada sean los correctos en caso de que alguna entrada sea errónea
#vuelva a solicitar el ingreso del dato hasta que sea correcto (adicionalmente pida el nombre y valide que sea un nombre válido).

def validateFloat (pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try :
            valor = float (input (pregunta))
            isCorrectData = True 
        except ValueError:
            print ('Ingresaste datos incorrectos. Inténtalo nuevamente.')
    return valor 

def validateString (pregunta):
    isCorrectData = False 
    while (isCorrectData == False):
        try: 
            valor= input (pregunta)
            assert (valor.isalpha())
            isCorrectData = True 
        except AssertionError:
            print ('Datos incorrectos. Inténtelo nuevamente.')
    return valor 

validateString ('Nombre : ')
validateFloat ('Ingrese su peso en kilogramos (kg) : ')
#Calcular IMC --> Estatura, peso --> imc= peso /(estatura**2)
def pedirDatosEPN():
    '''
    Se le pide al usuario su peso, estatura
    y su nombre.
    Con el fin de validar si la información brindada (data) está buena
    '''
    PREGUNTA_PESO ='Ingrese su peso en kilogramos (kg) : '
    PREGUNTA_ESTATURA = 'Ingrese su estatura en metros (m) : '
    PREGUNTA_NOMBRE = 'Ingrese su nombre : '
    peso = validateFloat (PREGUNTA_PESO)
    estatura = validateFloat (PREGUNTA_ESTATURA)
    nombre = validateString (PREGUNTA_NOMBRE)
    return peso, estatura,nombre

def calcularIMC ():
    pesoIn,estaturaIn,nombreIn = pedirDatosEPN()
    imc = pesoIn/(estaturaIn**2)
    return imc,nombreIn

calcularIMC ()

imc,nombre = calcularIMC()
print (imc, nombre)
print(f'El IMC de {nombre} es de {imc} %')


#Punto2-->Pida al usuario que ingrese un párrafo y luego muestre en pantalla cual es la palabra más grande,la palabra más pequeña.
#  Valide que el párrafo ingresado termine en punto sino es así se debe pedir al usuario que ingrese nuevamente el párrafo.

def validateEndWith (strValidate, pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try : 
            valor = input (pregunta)
            assert (valor.endswith (strValidate))
            isCorrectData = True 
        except AssertionError:
            print (f'Los datos son incorrectos.Ingrese nuevamente y recuerde que debe terminar con " {strValidate} " ')
    return valor 

parrafo = validateEndWith (' . ','Ingrese un párrafo : ')
parrafo = parrafo [ : - 1 ]
palabras = parrafo.split (' ')
print (palabras)
print (f'La palaba más grande es "{max(palabras, key = len)}" y el menor es "{min(palabras, key = len)}" ')

parrafo = 'Hola , cómo anda todo'
parrafo = parrafo.replace (' , ',' ')
print (parrafo)
palabras = parrafo.split(' ')
print (palabras)

parrafo = 'y e a '
palabras = parrafo.split(' ')
print (min(palabras))

#Punto3--->Un taller de biomédica desea tener un archivo para el manejo de los clientes, se pide que desarrolle un programa que en su primera ejecución cree el archivo llamado mantenimientos.txt. 
# Luego en cada ejecución se preguntará por el nombre del equipo médico, una descripción y el precio acordado para el mantenimiento (se deben almacenar estos datos nuevos en el archivo mantenimientos.txt).
def validarArchivo (nombreArchivo, descripcion):
    try: 
        archivo = open (nombreArchivo)
        return True
    except FileNotFoundError: 
        archivo = open(nombreArchivo, 'w', encoding = 'UTF-8')
        print ('2')
        archivo.writelines (descripcion)
        return False

def guardarLinea  (nombreArchivo, lineaIn):
    archivo = open (nombreArchivo,'a')
    archivo.writelines(lineaIn)

nameFile = 'mantenimientos.txt'
isValidate = validarArchivo (nameFile,'Seguimiento de mantenimiento de equipos médicos.')
if (isValidate):
    descEquipo = input ('Ingrese la descripción del equipo : ')
    nombre = validateString ('Ingrese su nombre : ')
    precio = validateFloat ('Ingrese el precio : ')
    linea = '\n Descripción' + descEquipo + 'Nombre de técnico encargado : ' + nombre + 'Precio acordado : ' + str (precio)
    guardarLinea (nameFile, linea)
else: 
    print(' Se creó el archivo')