#Punto3 

Electrocardiograma = '''Un electrocardiograma (ECG) registra las señales eléctricas del corazón.
        Es una prueba común e indolora que se utiliza para detectar
        rápidamente los problemas cardíacos y controlar la salud del corazón.
        Permite diagnosticar muchos problemas cardíacos frecuentes en personas de todas las edades.

        Se puede utilizar un electrocardiograma para determinar o detectar:
            -Un ritmo cardíaco anormal (arritmias)
            -Si las arterias obstruidas o estrechadas del corazón (enfermedad de las arterias coronarias) están ocasionando dolor de pecho o un ataque cardíaco
            -Si has tenido un ataque cardíaco previo
            -Cómo están funcionando determinados tratamientos para una enfermedad cardíaca, como un marcapasos
'''
print (Electrocardiograma)

import pandas as pd
import matplotlib.pyplot as plt
ecgData= pd.read_csv ('ecg (1).csv',encoding='UTF-8',header=0,delimiter= ';').to_dict ()
print (ecgData.keys ())
muestras = list(ecgData ['muestra'].values())
print (muestras)
voltaje = list (ecgData ['valor'].values())
print (voltaje)
plt.plot(muestras,voltaje)
###############################
plt.title('Electrocardiograma (ECG)')

plt.xlabel('Tiempo (ms)')
plt.ylabel('Amplitud o Voltaje(mV)')
plt.savefig('Electrocardiograma.png')
#################################
plt.show ()

Fotopletismografía = '''La fotopletismografía o fotopletismograma es una técnica de pletismografía en la cual se utiliza un haz de luz 
                        para determinar el volumen de un órgano.
                        Una fuente de luz infrarroja (LED) emite un haz sobre la piel para iluminar los vasos subcutáneos,
                        estos reflejan parte de dicho haz dependiendo la cantidad de hematíes que contienen.
                        La luz reflejada incide en un fotosensor (usualmente de cadmio-selenio) que la convierte en un voltaje equivalente.
                        Debido a que la piel absorbe más del 90 % de la luz, el par diodo-fotosensor se acompaña de amplificadores y
                        filtros que garantizan un voltaje adecuado.
                        ​ El ciclo cardíaco puede obtenerse midiendo el intervalo que existe entre cada pico de voltaje.
'''
print (Fotopletismografía)

import pandas as pd
import matplotlib.pyplot as plt
ppgData= pd.read_csv ('ppg (1).csv',encoding='UTF-8',header=0,delimiter= ';').to_dict ()
print (ppgData.keys ())
muestras = list(ppgData ['muestra'].values())
print (muestras)
voltaje = list (ppgData ['valor'].values())
print (voltaje)
plt.plot(muestras,voltaje)
###############################
plt.title('Fotopletismografía(PPG)')

plt.xlabel('Tiempo (ms)')
plt.ylabel('Amplitud o Voltaje(mV)')
plt.savefig('Fotopletismografía.png')
#################################
plt.show ()