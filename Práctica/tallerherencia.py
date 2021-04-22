class Persona ():
    def __init__(self,nombreEntrada,edadEntrada, idEntrada):
        self.nombre= nombreEntrada
        self.edad = edadEntrada
        self.id =idEntrada 
    
    def hablar (self,mensaje):
        'Expresa cualquuier mensajes que pueda ser ingresado.'
        print(f'Hola,soy {self.nombre} y tengo un mensaje que emitir... : ',mensaje)
    
    def recorrerDistancia (self,pasosDados):
        for i in range (pasosDados):
                print(f'Hola, soy {self.nombre} y he andado {i+1} pasos')

persona1= Persona('Marcela',18, 1193206840)
persona1.hablar('Amo a Camila Cabello')
persona1.recorrerDistancia(10)

class Doctor (Persona):
    def __init__ (self,nombreEntrada,edadEntrada,idEntrada,especialidadEntrada):
        Persona.__init__(self, nombreEntrada, edadEntrada, idEntrada)
        self.especialidad = especialidadEntrada

    def sanar (self,enfermedad):
        print(f'''Hola, soy {self.nombre}. Soy médico especialista en {self.especialidad} 
            y voy a aplicar una {enfermedad}
        ''')

anestesiologo = Doctor('Miguel', 37, 1001398789, 'Anestesiología')
anestesiologo.sanar ('epidural')

class Nutricionista (Persona):
    def __init__ (self, nombreEntrada, edadEntrada,universidadEngresado,idEntrada):
        Persona.__init__(self, nombreEntrada, edadEntrada, idEntrada)
        self.universidad= universidadEngresado
        print (f'''Hola, soy {self.nombre}.
        Tengo {self.edad} años
        Soy egresado de Nutrición y Dietética de la Universidad {self.universidad} y
        Mi número de ID es {self.id}.
    ''')
    def calcularIMC ():
        PREGUNTA_PESO = ' ¿ Cuánto es tu peso en kilogramos ? : '
        pesoEntrada =int (input(PREGUNTA_PESO))
        PREGUNTA_ALTURA = '¿Cuánto es tu altura en metros ? : '
        alturaEntrada = float (input(PREGUNTA_ALTURA))
        return pesoEntrada/(alturaEntrada**2)

nutricionista1 = Nutricionista ('Susana',22,'CES',1197867800)
imc= Nutricionista.calcularIMC ()
MENSAJE_DESPEDIDA = f"Tu IMC es ...{imc}"
print (MENSAJE_DESPEDIDA)

class Abogado (Persona):
    def __init__(self,nombreEntrada,edadEntrada,universidadEngresado,idEntrada,especialidadEntrada):
        Persona.__init__(self, nombreEntrada, edadEntrada, idEntrada)
        self.universidad = universidadEngresado
        self.especialidad = especialidadEntrada
        print(f''' Hola, soy {self.nombre}.
        Tengo {self.edad} años
        Soy egresad@ de la Facultad de Derecho de la Universidad {self.universidad}
        Me especialicé en Derecho {self.especialidad}
        Mi número de ID es {self.id}.
        ''')
    def defender (self,cliente,caso):
        print(f'''Procedo a representar a {cliente} en el caso por {caso}
        ''')

abogado1 = Abogado('Mariana', 22, 'de Cartagena', '3609654', 'Penal')
abogado1.defender('Carolina Sandoval', 'Corrupción de Menores')