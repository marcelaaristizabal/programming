#Punto1

MENSAJE_SNACKS = '¿ Cuáles son tus snacks favoritos 🧐 ? '
SNACK_1 = ' ¿ Cuál es el número 1 de tus snacks favoritos   ? : '
PRECIO_1 = ' ¿ Cuál es el precio de tu snack favorito 🤑 ? : '
SNACK_2 = ' ¿ Cuál es el número 2 de tus snacks favoritos ? : '
PRECIO_2 = ' ¿ Cuál es el precio de tu segundo snack favorito 🤑  ? : '
SNACK_3 = ' ¿ Cuál es el número 3 de tus snacks favoritos ? : '
PRECIO_3 = ' ¿ Cuál es el precio de tu tercer snack favorito 🤑  ? : '
SNACK_4 = ' ¿ Cuál es el número 4 de tus snacks favoritos ? : '
PRECIO_4 = ' ¿ Cuál es el precio de tu cuarto snack favorito  🤑  ? : '
SNACK_5 = ' ¿ Cuál es el número 5 (pero no menos bueno) de tus snacks favoritos ? : '
PRECIO_5 = ' ¿ Cuál es el precio de tu quinto pero no menos importante snack favorito ... 🤑 ? : '

MENSAJE_ENTRADA = '''Hola. En el día de hoy haré un gráfico con tus 5 snacks favoritos, con los que tienes mayor afinidad (enumerados del 1 al 5) y sus respectivos precios.
                    Seguido de cada snack que pongas,ingresarás sus precios.
                    '''
print (MENSAJE_ENTRADA)
PREGUNTA_NOMBRE =  '¿Cuál es tu nombre? : '
nombre = input (PREGUNTA_NOMBRE)
snack1 = input (SNACK_1)
precio_snack_1 = float (input(PRECIO_1))
snack2 = input (SNACK_2)
precio_snack_2 = float (input(PRECIO_2))
snack3 = input (SNACK_3)
precio_snack_3 = float (input(PRECIO_3))
snack4 = input (SNACK_4)
precio_snack_4 = float (input(PRECIO_4))
snack5 = input (SNACK_5)
precio_snack_5 = float (input(PRECIO_5))

import matplotlib.pyplot as plt 
snacks = [ snack1,snack2, snack3, snack4,snack5 ]
preciosSnacks = [precio_snack_1,precio_snack_2,precio_snack_3,precio_snack_4,precio_snack_5]
plt.barh (snacks, preciosSnacks , color ='g')
##################
PREGUNTA_NOMBRE =  '¿Cuál es tu nombre? : '
nombre = input (PREGUNTA_NOMBRE)
#Título
plt.title(f'Top 5 de SNACKS favoritos  de {nombre} ')
plt.xlabel('Precios respectivos de los snacks favoritos en pesos colombianos (COP)')
plt.ylabel(f'SNACKS favoritos de {nombre}')
plt.savefig('GraficodeBarrasSNACKSFavoritos.png')
##################
plt.show ()