#------------------------------------Punto1---------------------------------#
MENSAJE_SNACKS = '¿ Cuáles son tus snacks favoritos 🧐 ? '

SNACK_1 = ' ¿ Cuál es el número 1️⃣  de tus snacks favoritos   ? : '
PRECIO_1 = ' ¿ Cuál es el precio de tu snack favorito 🤑 ? : '
SNACK_2 = ' ¿ Cuál es el número 2️⃣  de tus snacks favoritos ? : '
PRECIO_2 = ' ¿ Cuál es el precio de tu segundo snack favorito 🤑  ? : '
SNACK_3 = ' ¿ Cuál es el número 3️⃣  de tus snacks favoritos ? : '
PRECIO_3 = ' ¿ Cuál es el precio de tu tercer snack favorito 🤑  ? : '
SNACK_4 = ' ¿ Cuál es el número 4️⃣  de tus snacks favoritos ? : '
PRECIO_4 = ' ¿ Cuál es el precio de tu cuarto snack favorito  🤑  ? : '
SNACK_5 = ' ¿ Cuál es el número 5️⃣  de tus snacks favoritos ? : '
PRECIO_5 = ' ¿ Cuál es el precio de tu quinto snack favorito ... 🤑 ? : '
SNACK_6 = ' ¿ Cuál es el número 6️⃣  de tus snacks favoritos ? : '
PRECIO_6 = ' ¿ Cuál es el precio de tu sexto pero no menos importante snack favorito ... 🤑 ? : '
SNACK_7 = ' ¿ Cuál es el número 7️⃣  de tus snacks favoritos ? : '
PRECIO_7 = ' ¿ Cuál es el precio de tu séptimo pero no menos importante snack favorito ... 🤑 ? : '
SNACK_8 = ' ¿ Cuál es el número 8️⃣  (pero no menos bueno) de tus snacks favoritos ? : '
PRECIO_8 = ' ¿ Cuál es el precio de tu octavo pero no menos importante snack favorito ... 🤑 ? : '

MENSAJE_ENTRADA = '''Hola. En el día de hoy haré un gráfico con tus 8 snacks favoritos, con los que tienes mayor afinidad (enumerados del 1 al 8) y sus respectivos precios.
                    Seguido de cada snack que pongas,ingresarás sus precios.
                    '''
print (MENSAJE_ENTRADA)

PREGUNTA_NOMBRE =  '¿Cuál es tu nombre? : '
nombre = input (PREGUNTA_NOMBRE)

snack1 = input (SNACK_1)
precio_snack_1 = float (input(PRECIO_1))
snack2 = input (SNACK_2)
precio_snack_2 = float (input(PRECIO_2))
snack3 = input (SNACK_3)
precio_snack_3 = float (input(PRECIO_3))
snack4 = input (SNACK_4)
precio_snack_4 = float (input(PRECIO_4))
snack5 = input (SNACK_5)
precio_snack_5 = float (input(PRECIO_5))
snack6 = input (SNACK_6)
precio_snack_6 = float (input(PRECIO_6))
snack7 = input (SNACK_7)
precio_snack_7 = float (input(PRECIO_7))
snack8 = input (SNACK_8)
precio_snack_8 = float (input(PRECIO_8))

import matplotlib.pyplot as plt 
snacks = [ snack1,snack2, snack3, snack4,snack5,snack6,snack7,snack8 ]
preciosSnacks = [precio_snack_1,precio_snack_2,precio_snack_3,precio_snack_4,precio_snack_5,precio_snack_6,precio_snack_7,precio_snack_8]
plt.barh (snacks, preciosSnacks , color ='m')
##################
PREGUNTA_NOMBRE =  '¿Cuál es tu nombre? : '
nombre = input (PREGUNTA_NOMBRE)
#Título
plt.title(f'Top 8 de SNACKS favoritos  de {nombre} ')
plt.xlabel('Precios respectivos de los snacks favoritos en pesos colombianos (COP)')
plt.ylabel(f'SNACKS favoritos de {nombre}')
plt.savefig('GraficodeBarrasSNACKSFavoritos.png')
##################
plt.show ()
#---------------------------------------Punto2---------------------------------#
class Humano ():
    '''
        Esta es la clase Humano exige atributos
        nombreIn: Hace referencia al nombre del usuario
        sexoIn: Hace referencia al sexo del usuario
        edadIn: Hace refencia a la estatura del usuario


    Tiene la siguiente acción:
        -Hablar(mensaje):
            Dado un mensaje lo muestra en pantalla
    '''

    def __init__(self,nombreIn,sexoIn,edadIn):
        self.nombre = nombreIn
        self.sexo = sexoIn
        self.edad = edadIn
        print(f'''Hola,soy {self.nombre},
            tengo {self.edad} años 
            y pertenezco al género {self.sexo}
            ''')
    def hablar (self,mensaje):
        'Expresa un mensaje ingresado'
        print(f'Hola,soy {self.nombre} tengo un mensaje que decir...',mensaje)

humano1 = Humano ('Marcela Aristizábal','Femenino',18)
humano1.hablar ('Eres una gran persona. Nunca cambies.')

class Doctor (Humano):
    def __init__ (self, nombreIn, edadIn,sexoIn):
        Humano.__init__(self, nombreIn, edadIn, sexoIn)
        print (f'''Hola, soy {self.nombre}.
        Tengo {self.edad} años,
        pertenezco al género {self.sexo}.
        Soy médico especialista en Endocrinología y calcularé tu IMC.
    ''')
    def calcularIMC ():
        PREGUNTA_PESO = ' ¿ Cuánto es tu peso en kilogramos ? : '
        pesoEntrada =int (input(PREGUNTA_PESO))
        PREGUNTA_ALTURA = '¿Cuánto es tu altura en metros ? : '
        alturaEntrada = float (input(PREGUNTA_ALTURA))
        return pesoEntrada/(alturaEntrada**2)

doctor1 = Doctor ('Gerónimo Restrepo','Masculino',32)
imc= Doctor.calcularIMC ()
MENSAJE_DESPEDIDA = f"Tu IMC es ...{imc}"
print (MENSAJE_DESPEDIDA)

#------------------------------------Punto3----------------------------------–#
MENSAJE_SALUDO = 'Hola,soy tu convertidora de monedas ONLINE. En el día de hoy podrás ingresar cuánto dinero tienes en dólares y te lo convertiré en euros.'
PREGUNTA_DOLARES = 'Ingresa la cantidad de dinero en dólares (US) : '
MENSAJE_EUROS = 'Mostrando cantidad ingresada en euros...'

isCorrectInfo = False
while (isCorrectInfo == False):
    try: 
        cantidadDolares= float (input(PREGUNTA_DOLARES))
        isCorrectInfo = True
    except ValueError : 
        print ('Ingresaste un dato no válido.')

euros = cantidadDolares * 0.82
cantidadEuros = euros
print(MENSAJE_EUROS)
print (cantidadEuros)

isCorrectInfo = False
while (isCorrectInfo == False):
    try : 
        PREGUNTA_NOMBRE ='Por favor,ingrese su nombre : '
        nombre= (input(PREGUNTA_NOMBRE))
        assert (nombre.isalpha())
        isCorrectInfo = True
    except AssertionError: 
            print ('Ingresaste un dato no válido')
isCorrectInfo = False
#-----------------------------------Punto4--------------------------------------#
import sys
nombreArchivo ='pacientes.txt'
try:
    archivo = open (nombreArchivo)
    print ('1')
except FileNotFoundError:
    archivo = open (nombreArchivo,'w',encoding= 'UTF-8' )
    descripcion = 'Base de datos de manejo de pacientes en el consultorio de Neurología.'
    print ('2')
    archivo.writelines(descripcion)
    sys.exit (1)

archivo = open (nombreArchivo, 'a') 
nombrePacientes= input (' Ingrese el nombre completo del paciente : ')
descripcionEnfermedad= input('Ingrese descripción de la enfermedad o patalogía del paciente : ')
precioConsulta = float (input('Ingrese la cantidad estimada del precio de la consulta en pesos colombianos (COP): '))
linea = '\nNombre del paciente: ' + nombrePacientes + ' Descripción de la enfermedad o patología del paciente : ' + str(precioConsulta) 
archivo.writelines(linea)
archivo.close() 

#Leer o mostra en pantalla el archivo 'mantenimientos.txt'
with open (nombreArchivo, 'r') as reader: 
    for line in reader:
        print (line)
