import matplotlib.pyplot as plt
pieCiudades = ['Barranquilla','Sincelejo','Villavicencio','Cartagena','Manizales']

cantidadHabitantes = [1.2,0.27,0.53,0.91,0.43]

def etiquetarElementosPorcentuales (cantidadHabitantes ,pieCiudades,indicador= '-->'):
    acumulador = 0
    for elemento in porcentajesHabitantes:
        acumulador += elemento

    for i in range (len(pieCiudades)):
        pieCiudades [i] += indicador + str (cantidadHabitantes [i]/ acumulador * 100) + ' Millones '


pieExplode = [0.1, 0 , 0 , 0 , 0]
acumulador = 0
porcentajesHabitantes= [34,8,14,31,13]
pieCiudades = ['Barranquilla','Sincelejo','Villavicencio','Cartagena','Manizales']

etiquetarElementosPorcentuales(cantidadHabitantes, pieCiudades,'--->')
plt.pie(cantidadHabitantes,labels = pieCiudades,
        explode=pieExplode, 
        shadow=True,
        startangle=45)

###########################
plt.title(' Cantidad de habitantes en algunas ciudades de Colombia')
plt.savefig('PieCiudadesColombianas.png')
###########################
plt.show ()