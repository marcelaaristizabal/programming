MENSAJE_SNACKS = '¿ Cuáles son tus snacks favoritos 🧐 ? '

SNACK_1 = ' ¿ Cuál es el número 1️⃣  de tus snacks favoritos   ? : '
PRECIO_1 = ' ¿ Cuál es el precio de tu snack favorito 🤑 ? : '
SNACK_2 = ' ¿ Cuál es el número 2️⃣  de tus snacks favoritos ? : '
PRECIO_2 = ' ¿ Cuál es el precio de tu segundo snack favorito 🤑  ? : '
SNACK_3 = ' ¿ Cuál es el número 3️⃣  de tus snacks favoritos ? : '
PRECIO_3 = ' ¿ Cuál es el precio de tu tercer snack favorito 🤑  ? : '
SNACK_4 = ' ¿ Cuál es el número 4️⃣  de tus snacks favoritos ? : '
PRECIO_4 = ' ¿ Cuál es el precio de tu cuarto snack favorito  🤑  ? : '
SNACK_5 = ' ¿ Cuál es el número 5️⃣  de tus snacks favoritos ? : '
PRECIO_5 = ' ¿ Cuál es el precio de tu quinto snack favorito ... 🤑 ? : '
SNACK_6 = ' ¿ Cuál es el número 6️⃣  de tus snacks favoritos ? : '
PRECIO_6 = ' ¿ Cuál es el precio de tu sexto pero no menos importante snack favorito ... 🤑 ? : '
SNACK_7 = ' ¿ Cuál es el número 7️⃣  de tus snacks favoritos ? : '
PRECIO_7 = ' ¿ Cuál es el precio de tu séptimo pero no menos importante snack favorito ... 🤑 ? : '
SNACK_8 = ' ¿ Cuál es el número 8️⃣  (pero no menos bueno) de tus snacks favoritos ? : '
PRECIO_8 = ' ¿ Cuál es el precio de tu octavo pero no menos importante snack favorito ... 🤑 ? : '

MENSAJE_ENTRADA = '''Hola. En el día de hoy haré un gráfico con tus 8 snacks favoritos, con los que tienes mayor afinidad (enumerados del 1 al 8) y sus respectivos precios.
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
snack6 = input (SNACK_6)
precio_snack_6 = float (input(PRECIO_6))
snack7 = input (SNACK_7)
precio_snack_7 = float (input(PRECIO_7))
snack8 = input (SNACK_8)
precio_snack_8 = float (input(PRECIO_8))

import matplotlib.pyplot as plt 
snacks = [ snack1,snack2, snack3, snack4,snack5,snack6,snack7,snack8 ]
preciosSnacks = [precio_snack_1,precio_snack_2,precio_snack_3,precio_snack_4,precio_snack_5,precio_snack_6,precio_snack_7,precio_snack_8]
plt.barh (snacks, preciosSnacks , color ='m')
##################
PREGUNTA_NOMBRE =  '¿Cuál es tu nombre? : '
nombre = input (PREGUNTA_NOMBRE)
#Título
plt.title(f'Top 8 de SNACKS favoritos  de {nombre} ')
plt.xlabel('Precios respectivos de los snacks favoritos en pesos colombianos (COP)')
plt.ylabel(f'SNACKS favoritos de {nombre}')
plt.savefig('GraficodeBarrasSNACKSFavoritos.png')
##################
plt.show ()