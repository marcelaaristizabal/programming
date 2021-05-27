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