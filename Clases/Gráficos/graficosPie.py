#Importamos la librería.
import matplotlib.pyplot as plt
#Creamos los labels ( componentes que etiqutan los gráficos de torta),sizes y explode.

#Labels: Python, Java, Dart, Js---> Nombres porciones de torta.
pieLabels= ['Pyhton','Java','Dart','Js']

#Sizes: Los tamaños de cada porción de la torta. En total debe dar 100%.
sizes= [50,25,15,10]

def etiquetarElementosPorcentuales (sizes,labels,indicador= '-->'):
    acumulador = 0
    for elemento in sizes:
        acumulador += elemento

    for i in range (len(pieLabels)):
        pieLabels [i] += indicador + str (sizes [i]/ acumulador * 100) + '%'

#Explode: Que tan alejado del origen está la torta.
pieExplode = [0,0,0.1,0]
acumulador = 0
sizes= [50,25,15,10]
pieLabels= ['Python','Java','Dart','Js']
etiquetarElementosPorcentuales(sizes, pieLabels,'😄')
plt.pie(sizes,labels = pieLabels,
        explode=pieExplode, 
        shadow=True,
        startangle=45)

###########################
plt.title('Uso de lenguajes de Programación en el 2021')
plt.savefig('tortasLenguajes.png')
###########################
plt.show ()