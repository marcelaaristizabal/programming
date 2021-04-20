MENSAJE_CONTEXTO ='Hola,en el día de hoy te mostraré en pantalla algunos datos curiosos de los delfines (De acuerdo a cada especie)'
PREGUNTAGENERO = ''' ¿De qué género de la especie Delphinus Delphis quisieras conocer ? :
                    1 - Hembra
                    2 - Macho
'''
genero = input (PREGUNTAGENERO)
class Animal ():
    '''
        Esta es la clase Animal que muestra de manera ilutrativa atributos,
        datos curiosos y algunas características del Delfín.
        En este caso, la especie Delphinus Delphis.

        Tiene las siguientes acciones:

        -saludar (saludo):
            Muestra de forma onomatopoyética el sonido que hace un delfín al saludar.


        -mostrarAtributos():
            Muestra los atributos del delfín 
            De la especie Delphinus Delphis.
    '''
    def __init__(self,genero) :
        print("Chasquidos y silbidos")
        if ( genero == 'Hembra'):
            nombreEntrada = 'Josephine'
            pesoDelfin= 'El promedio normal del peso de una hembra de la especie Delphinus Delphis es de 200 kilogramos'
            tamañoDelfin ='''En el PACÍFICO ORIENTAL las hembras pueden medir entre  1,6-2,2 m...
                        Mientras que en ATLÁNTICO ORIENTAL tienen un tamaño promedio de 2,70m. 
            '''
            edadEntrada= 'Las hembras de esta especie sobreviven en cautiverio entre 25 y 35 años.'
        elif (genero == 'Macho'):
            nombreEntrada = 'Tómas'
            pesoDelfin = 'El promedio normal del peso de un macho de la especie Delphinus Delphis es de 200 kilogramos.'
            tamañoDelfin = '''En el PACÍFICO ORIENTAL los machos pueden medir entre 1,7-2,3 m
                        Mientras que en ATLÁNTICO ORIENTAL tienen un tamaño promedio de 2,70m. 
            '''
            edadEntrada = 'Los machos de esta especie pueden sobrevivir en cautiverio cerca de 40 años.'
        else:
            print('INGRESA UNA OPCIÓN VÁLIDA.')
    
        self.edad = edadEntrada
        self.peso = pesoDelfin
        self.nombre= nombreEntrada
        self.tamaño= tamañoDelfin
        self.especie = "Delphinus delphis"
        self.ubicacion = '''El Delfín común oceánico o de aletas cortas,es una especie oceánica con
                        una amplia distribución en los mares tropicales de los océanos:
                        1- Océano Atlántico 
                        2- Océano Pacífico 
                        3- Océano Índico (algunos sitios)

                        También se encuentra en algunos mares relativamente aislados, como los mares: 

                        a- Mar del Japón
                        b- Mar Okhotsk
                        c- Mar MEDITERRÁNEO
                        d- Mar Negro
        '''
    def saludar (self,saludo):
        #Los delfines suelen utilizar silbidos únicos propios de cada uno 
        #cuando se reunen con otro grupo a modo de saludo y presentación.
        print(f'Hola, soy {self.nombre}. Así es como te saludo', saludo)
    

    def mostrarAtributos (self):
        print(f''' Mi nombre {self.nombre}. Soy un@ delfín muy feliz.
                    {self.tamaño}
                    {self.edad}  
                    {self.peso}
        ''')
    def datosCuriosos (self):
        print ('''Al nacer, el delfín común oceánico mide alrededor de 80-100 cm.
            DENTICIÓN : 41 y 54 pares de dientes en ambas hemimandíbulas, pudiendo presentar, uno o dos pares más, en la superior. 

            PIGMENTACIÓN: El color gris oscuro predomina en la superficie dorsal, desde la frente hasta la aleta dorsal,
            donde forma un pico invertido,trazándose un dibujo en el lateral que recuerda a un “reloj de arena”, cuyo fragmento anterior es de color amarillo,
            contrastando con el color oscuro de la parte posterior del mismo, que se extiende hasta el pedúnculo caudal. Ventralmente es blanco.

            Las aletas dorsales y pectorales son oscuras, aunque en adultos la dorsal presenta un tono gris en la parte central. 
            Destaca una línea que parte de la zona genital hacia delante atravesando el parche torácico amarillo.
            Así como una banda negra que une aletas pectorales con el maxilar inferior. Los juveniles tienen una coloración más clara.
            Los machos adultos tienen una quilla en el área genital, marcada con la edad.
        ''')

    def alimentar (self):
        print('La alimentación del delfín común macho o hembra se basa en calamares y peces pequeños que forman bancos, alimentándose de noche y descansando por el día.')

saludo = '''‘Güi, güi...
            Tototo...’
'''


delfin = Animal(genero)
delfin.saludar(saludo)
print(delfin.especie)
delfin.alimentar()
print(delfin.ubicacion)
delfin.mostrarAtributos()
delfin.datosCuriosos()