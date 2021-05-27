import sys
nombreArchivo ='pacientes.txt'
try:
    archivo= open (nombreArchivo)
    print ('1')
except FileNotFoundError:
    archivo = open (nombreArchivo,'w',encoding= 'UTF-8' )
    descripcion = 'Base de datos de manejo de pacientes en el consultorio de Neurología.'
    print ('2')
    archivo.writelines(descripcion)
    sys.exit (1)

archivo = open (nombreArchivo, 'a') 
nombrePaciente= input (' Ingrese el nombre completo del paciente : ')
descripcionEnfermedad= input('Ingrese descripción de la enfermedad o patalogía del paciente : ')
precioConsulta = float (input('Ingrese la cantidad estimada del precio de la consulta en pesos colombianos (COP): '))
linea = '\nNombre del paciente: ' + nombrePaciente + ' Descripción de la enfermedad o patología del paciente : ' + descripcionEnfermedad  +  'Precio de la consulta en pesos colombianos (COP) : '+ str(precioConsulta) 
archivo.writelines(linea)
archivo.close() 

#Leer o mostra en pantalla el archivo 'mantenimientos.txt'
with open (nombreArchivo, 'r') as reader: 
    for line in reader:
        print (line)