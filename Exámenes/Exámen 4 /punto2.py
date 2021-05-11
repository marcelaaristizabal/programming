#Punto2

CIUDAD_1 = '¿ Cuál es tu ciudad favorita en el mundo entero ? : '
CIUDAD_2 = '¿ Cuál es tu segunda ciudad favorita en el mundo entero ? : '
CIUDAD_3 = '¿ Cuál es tu tercera ciudad favorita en el mundo entero ? : '
CIUDAD_4 = '¿ Cuál es tu cuarta ciudad favorita en el mundo entero ? : '
CIUDAD_5 = '¿ Cuál es tu quinta (pero no menos importante) ciudad favorita en el mundo entero ? : '

PREGUNTA_NOMBRE = '¿Cuál es tu nombre? : '
nombre = input (PREGUNTA_NOMBRE)

MENSAJE_SALUDO = f'''Hola, {nombre}. En el día de hoy te mostraré en un gráfico de torta de tus CIUDADES FAVORITAS en el mundo.
                Seguidamente ingresarás su cantidad (en millones) de habitantes.
                '''

print (MENSAJE_SALUDO)
ciudad1 = input(CIUDAD_1)
HABITANTES_CUIDAD_1 = ' ¿ Cuántas personas habitan en tu ciudad favorita ? : '
habitantes_1 = float (input (HABITANTES_CUIDAD_1))
ciudad2 = input(CIUDAD_2)
HABITANTES_CUIDAD_2 = f' ¿ Cuántas personas habitan en {ciudad2} ? : '
habitantes_2= float (input (HABITANTES_CUIDAD_2))
ciudad3 = input(CIUDAD_3)
HABITANTES_CUIDAD_3 = f' ¿ Cuántas personas habitan en {ciudad3} ? : '
habitantes_3 = float (input (HABITANTES_CUIDAD_3))
ciudad4 = input(CIUDAD_4)
HABITANTES_CUIDAD_4 = f' ¿ Cuántas personas habitan en {ciudad4}? ; '
habitantes_4 = float (input (HABITANTES_CUIDAD_4))
ciudad5 = input(CIUDAD_5)
HABITANTES_CUIDAD_5 = f' ¿ Cuántas personas habitan en {ciudad5} ? : '
habitantes_5 = float (input (HABITANTES_CUIDAD_5))

import matplotlib.pyplot as plt
pieCiudadesFavoritas = [ ciudad1,ciudad2,ciudad3,ciudad4,ciudad5]

cantidadHabitantes = [habitantes_1,habitantes_2,habitantes_3,habitantes_4,habitantes_5]
def etiquetarCantidadHabitantes (cantidadHabitantes ,pieCiudades,indicador= '-->'):
    acumulador = 0
    for elemento in cantidadHabitantes:
        acumulador += elemento

    for i in range (len(pieCiudadesFavoritas)):
        pieCiudadesFavoritas [i] += indicador +  str (cantidadHabitantes[i])+ ' Millones '

cantidadHabitantes = [habitantes_1,habitantes_2,habitantes_3,habitantes_4,habitantes_5]
maximoHabitantes = max (cantidadHabitantes)
ubicacion = cantidadHabitantes.index (maximoHabitantes)
print (ubicacion)

pieExplode = [0, 0 , 0 , 0 , 0]
pieExplode [ubicacion] = 0.1 

etiquetarCantidadHabitantes (cantidadHabitantes, pieCiudadesFavoritas,'---> ')
plt.pie(cantidadHabitantes,labels = pieCiudadesFavoritas,
        explode=pieExplode, 
        shadow=True,
        startangle=45)

###########################
plt.title(f' Top 5 de ciudades FAVORITAS en el mundo entero de {nombre}')
plt.savefig('PieCiudadesFavoritas.png')
###########################
plt.show ()