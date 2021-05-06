PREGUNTA_NOMBRE = '¿Cuál es tu nombre? : '
nombre = input (PREGUNTA_NOMBRE)

MENSAJE_SALUDO = f'''Hola, {nombre}. En el día de hoy te mostraré en un gráfico de barras los ingresos que recibiste en el 2020.
                Por favor. Ingresarás tus ganancias mes a mes.
                '''

PREGUNTA_GANANCIAS_ENERO ='¿ Cuánto dinero recibiste en el mes de enero ? : '
PREGUNTA_GANANCIAS_FEBRERO ='¿ Cuánto dinero recibiste en el mes de febrero ? : '
PREGUNTA_GANANCIAS_MARZO ='¿ Cuánto dinero recibiste en el mes de marzo ? : '
PREGUNTA_GANANCIAS_ABRIL ='¿ Cuánto dinero recibiste en el mes de abril ? : '
PREGUNTA_GANANCIAS_MAYO = '¿ Cuánto dinero recibiste en el mes de mayo ? : '
PREGUNTA_GANANCIAS_JUNIO = '¿ Cuánto dinero recibiste en el mes de junio ? : '
PREGUNTA_GANANCIAS_JULIO = '¿ Cuánto dinero recibiste en el mes de julio ? : '
PREGUNTA_GANANCIAS_AGOSTO = '¿ Cuánto dinero recibiste en el mes de agosto  ? : '
PREGUNTA_GANANCIAS_SEPTIEMBRE = '¿ Cuánto dinero recibiste en el mes de septiembre ? : '
PREGUNTA_GANANCIAS_OCTUBRE ='¿ Cuánto dinero recibiste en el mes de octubre ? : '
PREGUNTA_GANANCIAS_NOVIEMBRE ='¿ Cuánto dinero recibiste en el mes de noviembre ? : '
PREGUNTA_GANANCIAS_DICIEMBRE = '¿ Cuánto dinero recibiste en el mes de diciembre ? : '

enero = int (input (PREGUNTA_GANANCIAS_ENERO))
febrero = int (input (PREGUNTA_GANANCIAS_FEBRERO))
marzo = int (input (PREGUNTA_GANANCIAS_MARZO))
abril = int (input (PREGUNTA_GANANCIAS_ABRIL))
mayo = int (input (PREGUNTA_GANANCIAS_MAYO))
junio = int (input (PREGUNTA_GANANCIAS_JUNIO))
julio = int (input (PREGUNTA_GANANCIAS_JULIO))
agosto = int (input (PREGUNTA_GANANCIAS_AGOSTO))
septiembre = int (input (PREGUNTA_GANANCIAS_SEPTIEMBRE))
octubre= int (input (PREGUNTA_GANANCIAS_OCTUBRE))
noviembre= int (input (PREGUNTA_GANANCIAS_NOVIEMBRE))
diciembre = int (input (PREGUNTA_GANANCIAS_DICIEMBRE))

import matplotlib.pyplot as plt 
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
ingresosMensuales = [enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre]
plt.barh (meses, ingresosMensuales , color ='m')
##################
PREGUNTA_NOMBRE =  '¿Cuál es tu nombre? : '
nombre = input (PREGUNTA_NOMBRE)
#Título
plt.title(f'Ingresos mensuales de {nombre} en el año 2020')
plt.xlabel('Meses del año 2020')
plt.ylabel('Cantidad de ingresos en el año 2020 en millones de pesos (COP)')
plt.savefig('GraficodeBarrasIngresos2020.png')
##################
plt.show ()