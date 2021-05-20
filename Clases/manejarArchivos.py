import sys
nombre = input ('Ingrese su nombre : ')
edad = int (input ('Ingrese su edad : '))
estatura = float (input ('Ingrese su estatura : '))

nombreArchivo = 'estudiantes.txt'
#Para validar si el archivo existe o no.
try :
    archivo = open (nombreArchivo)
    print ('1')
except FileNotFoundError:
    archivo = open (nombreArchivo, 'w',encoding='UTF-8') #'w' reescribe los datos existentes. Por eso se usa solo al crear el archivo.
    #Encoding UTF-8 por las letras en latino.
    descripcion = 'Archivo de datos de estudiantes'
    print ('2')
    archivo.writelines(descripcion)
    sys.exit(1) #Para salirse de la ejecución. El 1 significa que el archivo no existía, definido anteriormente.

archivo = open (nombreArchivo, 'a') #Cuando se agrega 'a' se crea automáticamente el archivo.
linea = '\n nombre : ' + nombre + ' edad : ' + str(edad) + ' estatura : ' + str(estatura) #\n significa enter.
archivo.writelines(linea)
archivo.close() #Ocupa menos espacio en la memoria RAM.

#Leer ---> No se necesita archivo.close(). Es más sencilla, con esta opción se pueden mostrar el contenido del archivo.
with open (nombreArchivo, 'r') as reader: 
    for line in reader:
        print (line)

import pandas as pd
diccionario = {}
diccionario ['nombre'] = 'Marcela'
diccionario ['edad'] = 18
diccionario ['estatura'] = 1.78
serie =pd.Series (diccionario)
print(serie)
serie.to_csv ('datos.csv', sep = ';')