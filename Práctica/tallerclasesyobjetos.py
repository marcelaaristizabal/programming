class Torta ():
    def __init__(self,formaTorta,saborTorta,alturaTorta):
        print('La torta de mi abuela')
        self.forma = formaTorta
        self.sabor = saborTorta
        self.altura = alturaTorta
    
    def mostrarAtributos (self):
        print (f'''La forma de la torta es {self.forma}. Genial.
                    Mi abuela las hace muy grandes. Su altura es de {self.altura} metros.
                    Tiene un delicioso sabor de {self.sabor}. A todos nos encanta.
        ''')
tortaUva = Torta('Redonda', 'Uva', 0.50)
tortaUva.mostrarAtributos()

class Estudiante ():
    def __init__ (self,nombreEntrada,idEntrada,edadEntrada,carreraEntrada,semestreEntrada) :
        self.nombre = nombreEntrada
        self.id= idEntrada
        self.edad= edadEntrada
        self.carrera = carreraEntrada
        self.semestre = semestreEntrada
    
    def estudiar (self,materia,horasEstudio):
                    print (f'''Tengo que estudiar {materia} a lo largo de mi carrera.
                    Me gusta mucho asistir a las clases. Consume mucho de mi tiempo,
                    cerca de {horasEstudio} horas diarias.
        ''')

estudiante1= Estudiante ('Jerónimo',123456789,19, 'Ingeniería Biomédica','Tercer semestre')
estudiante1.estudiar ('Morfofisiología', 9)

class Nutricionista ():
    def __init__(self,nombreEntrada,edadEntrada,universidadEngresado):
        self.nombre = nombreEntrada
        self.edad= edadEntrada
        self.universidad = universidadEngresado
        print (f'''Hola, soy {self.nombre}.
        Tengo {self.edad} años y 
        soy egresado de Nutrición y Dietética de la Universidad {self.universidad}
    ''')
    def calcularIMC ():
        PREGUNTA_PESO = ' ¿ Cuánto es tu peso en kilogramos ? : '
        pesoEntrada =int (input(PREGUNTA_PESO))
        PREGUNTA_ALTURA = '¿Cuánto es tu altura en metros ? : '
        alturaEntrada = float (input(PREGUNTA_ALTURA))
        return pesoEntrada/(alturaEntrada**2)

nutricionista1 = Nutricionista ('Nicolás',37,'CES')
imc= Nutricionista.calcularIMC ()
MENSAJE_DESPEDIDA = f"Tu IMC es ...{imc}"
print (MENSAJE_DESPEDIDA)

class Canguro ():
    def __init__ (self,nombreEntrada,idEntrada,edadEntrada):
        self.nombre = nombreEntrada
        self.id= idEntrada
        self.edad= edadEntrada
    def recorrerDistancia (self,cantidadSaltos):
        print (f'''Hola, soy {self.nombre} 
        Mi identificación es {self.id}
        ''')
        for i in range (cantidadSaltos):
            print(f'y he realizado {i+1} saltos')

canguro1 = Canguro ('Stive',7462204,24)
canguro1.recorrerDistancia (9)

class Tropeta ():
    def __init__ (self,nombreTrompeta,cancionTrompeta):
        self.nombre = nombreTrompeta
        self.cancion = cancionTrompeta
    def sonar (self,n):
        print(f'''Mi nombre es {self.nombre}
            Y sonaré la canción que dice...{self.cancion} veces
        ''')
        for i in range (n):
            print (self.cancion)
trompeta1 = Tropeta ('Úrsula', 'Tararí...tarará...tararí...tarará')
trompeta1.sonar(5)