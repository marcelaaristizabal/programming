# Estos son booleans que son variables que solo valen
# Verdadero o Falso
pruebaV = True
pruebaF = False
print (pruebaF)
print (pruebaV)
pruebaV = pruebaF
print (pruebaV)
edad = 18 
estatura = 1.78 
peso = 75 
NOMBRE = "Marcela Aristizabal Julio"
print ("#"*15,"Mayor Edad", "#"*15)
isMayorEdad = edad >= 18
print (isMayorEdad)
print ("#"*15, "Bajo la Estatura promedio", "#"*15)
isMayorEstatura = estatura < 1.70
print(isMayorEstatura)
# Calculando si el peso es diferente a 75
print("#"*15, "Peso diferente 75", "#"*15)
isPesoDiferente = peso != 75
print (isPesoDiferente)
# vamos a ver si un apellido esta en el nombre completo
apellido = "Aristizabal"
isApellido = apellido in NOMBRE
print ("#"*15,"Esta el apellido en el nombre?", "#"*15)
print(isApellido)