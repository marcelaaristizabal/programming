#Integrantes:

#Marcela Aristizábal
#Isabella Parra
#Paulina Orozco 

#Elementos Digitales
class Digitales ():
    def __init__ (self, nombreIn, creadorIn, fechaPublicacionIn):
        print ('Estas son algunas características de esta app de música')
        self.nombre = nombreIn
        self.creador = creadorIn
        self.fechaPublicacion = fechaPublicacionIn
    def todosAtributos (self):
        print (f''' Hola, el nombre de esta plataforma es {self.nombre} es una plataforma digital nueva
                creada por {self.creador} en la fecha {self.fechaPublicacion}
    ''')

digitales1 = Digitales('SpotMusic','Laura', '23 de julio del 2018')
digitales1.todosAtributos()

#Usuario
class Usuario ():
    def __init__ (self, nombreIn, edadIn, sexoIn, nacionalidadIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.sexo = sexoIn
        self.nacionalidad = nacionalidadIn
    def hablar (self):
        print (f'''Hola soy {self.nombre}, pertenezco al sexo {self.sexo}
        tengo {self.edad} años y soy de nacionalidad {self.nacionalidad}''')
    def mostrarAtributos (self, cancionIn):
        self.cancion = cancionIn
        print (f'''Hola soy {self.nombre} y estoy escuchando la cancion {self.cancion}
    ''')
usuario1 = Usuario('Mateo', 28, 'Masculino', 'Colombiana')
usuario1.hablar()
usuario1.mostrarAtributos('El color de tus ojos')

#Página
class Pagina ():
    def __init__(self,tipodeContenido,formatoEntrada,fechaPublicacion):
        self.contenido= tipodeContenido
        self.formato= formatoEntrada
        self.publicacion = fechaPublicacion
    
    def mostrarAtributos(self):
        print(f''' Hola,te enseñaré {self.contenido} en esta plataforma digital,
            el formato en el que está es {self.formato} publicado el {self.publicacion}...
            Realmente espero que sea de tu agrado.
        ''')
pagina1= Pagina ('videoclips musicales', 'MP4', '25 de noviembre del 2019')
pagina1.mostrarAtributos()

class Cancion (Digitales):
    def __init__ (self, nombreIn, creadorIn, fechaPublicacionIn, generoIn, duraciónIn):
        Digitales.__init__(self,nombreIn, creadorIn, fechaPublicacionIn)
        self.genero = generoIn
        self.duracion = duraciónIn
        print (f'la nueva canción se llama {self.nombre} y salió el {self.fechaPublicacion}')
    def reproducir (self, cantidadVeces):
        for i in range (cantidadVeces):
            print (f'La canción {self.nombre} está reproduciéndose {i+1} veces')


class Artista (Usuario):
    def __init__(self, nombreIn, edadIn, sexoIn, nacionalidadIn, GenmusicalIn, NumdecancionespubIn, NumdealbumnsIn):
        Usuario.__init__(self, nombreIn, edadIn, sexoIn, nacionalidadIn)
        self.generomusical = GenmusicalIn
        self.numerodecacionespublicadas = NumdecancionespubIn
        self.numerodealbumns = NumdealbumnsIn
    def cantar (self,ciudad):
        print (f'''Hola, {ciudad}. Mi nombre es {self.nombre} y nos vemos este
        28 de Noviembre. ¡Compra tu boleta ya!
        ''')

#posicion = int (input(PREGUNTA_BORRAR_COORDENADA)) - 1
PREGUNTA_BORRAR_COORDENADA ='Ingrese la posición que desee borrar : '
listasFavoritos= []

class Favoritos (Pagina):
    def __init__(self,tipodeContenido,formatoEntrada,fechaPublicacion,favoritosComunidad,fechaActualizacion):
        Pagina.__init__ (self,tipodeContenido,formatoEntrada,fechaPublicacion)
        self.favoritos=favoritosComunidad
        self.actualizacion= fechaActualizacion
    
    def agregarCancionNueva (self,cancionNueva,fechaActualizada):
        self.nueva = cancionNueva
        self.actualizacion=fechaActualizada
        listasFavoritos.append (cancionNueva)
        print (f'Playlist favoritos {listasFavoritos},Fecha última actualización {fechaActualizada}')
    def eliminarCancion (self,posicion = int (input(PREGUNTA_BORRAR_COORDENADA))):
        print (listasFavoritos)
        listasFavoritos.pop (posicion-1)
        print (listasFavoritos)

trap = Favoritos('Trap', 'MP4', '21 de julio del 2020', '-', '29 Marzo del 2021')
trap.agregarCancionNueva('Cuando la mujer traiciona', '2 de abril del 2021')
trap.agregarCancionNueva('Cuando te veo', '14 de abril del 2021')
trap.agregarCancionNueva('Hecha pa mi', '19 de abril del 2021')
trap.eliminarCancion(2)

cancion1 = Cancion('I miss you', 'Blink 182', '9 de febrero del 2004', 'Rock alternativo', '3:50 minutos')
cancion1.reproducir(9)

artista1 = Artista('Malbin', 21, 'Masculino', 'Colombiana', 'Reggaeton', 5, 1)
artista1.cantar('Medellín')