#Aquí explicaremos cómo hacer un gráfico de barras
import matplotlib.pyplot as plt 
lenguajes = ['py','Java','Dart','Ts','elixir']
encuesta= [50,10,20,10,10]
plt.bar(lenguajes,encuesta,width = 0.6, color ='c')
##################
#Título
plt.title('Lenguajes más usados')
plt.xlabel('Lenguajes de Programación')
plt.ylabel('% de uso de Lenguajes')
plt.savefig('GráficodeLenguajes.png')
##################
plt.show ()