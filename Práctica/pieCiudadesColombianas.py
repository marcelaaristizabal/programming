import matplotlib.pyplot as plt
pieCiudades = ['Barranquilla','Sincelejo','Villavicencio','Cartagena','Manizales']

porcentajesHabitantes = [34,8,14,31,13]

def etiquetarElementosPorcentuales (porcentanjesHabitantes,pieCiudades,indicador= '-->'):
    acumulador = 0
    for elemento in porcentajesHabitantes:
        acumulador += elemento

    for i in range (len(pieCiudades)):
        pieCiudades [i] += indicador + str (porcentajesHabitantes [i]/ acumulador * 100) + '%'


pieExplode = [0.1, 0 , 0 , 0 , 0]
acumulador = 0
porcentajesHabitantes= [34,8,14,31,13]
pieCiudades = ['Barranquilla','Sincelejo','Villavicencio','Cartagena','Manizales']

etiquetarElementosPorcentuales(porcentajesHabitantes, pieCiudades,'😎')
plt.pie(porcentajesHabitantes,labels = pieCiudades,
        explode=pieExplode, 
        shadow=True,
        startangle=45)

###########################
plt.title('Porcentajes según la cantidad de habitantes en algunas ciudades de Colombia')
plt.savefig('PieCiudadesColombianas.png')
###########################
plt.show ()