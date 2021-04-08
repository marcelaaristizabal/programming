# Estos son booleans que son variables que solo valen
# Verdadero o Falso
pruebaV = True
pruebaF = False
print (pruebaF)
print (pruebaV)
pruebaV = pruebaF
print (pruebaV)
# Estas fueron las variables definidas en la clase 
# anterior
edad = 18 
estatura = 1.78 
peso = 75 
# Definiendo una variable que nunca cambia
NOMBRE = "Marcela Aristizabal Julio"
# Preguntando si se es Mayor de Edad
print ("#"*15,"Mayor Edad", "#"*15)
isMayorEdad = edad >= 18
print (isMayorEdad)
# Preguntando si la estatura se encuentra Bajo la
# Estatura promedio
print ("#"*15, "Bajo la Estatura promedio", "#"*15)
isMayorEstatura = estatura < 1.70
print(isMayorEstatura)
# Calculando si el peso es diferente de 75
print("#"*15, "Peso diferente 75", "#"*15)
isPesoDiferente = peso != 75
print (isPesoDiferente)
# vamos a ver si un apellido esta en el nombre completo
apellido = "Aristizabal"
isApellido = apellido in NOMBRE
print ("#"*15,"Esta el apellido en el nombre?", "#"*15)
print(isApellido) 