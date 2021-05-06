import pandas as pd
import matplotlib.pyplot as plt
ppgData= pd.read_csv ('ppg.csv',encoding='UTF-8',header=0,delimiter= ';').to_dict ()
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