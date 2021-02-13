# Estos son booleans que son variables que solo valen
# Verdadero o Falso
pruebaV = True
pruebaF = False
print (pruebaF)
print (pruebaV)
pruebaV = pruebaF
print (pruebaV)
# Definir dos numeros cualquiera para aplicar
# diferentes booleans,preguntas y operaciones 
numeroA = 45
numeroB = 67
# preguntar si el numero A es mayor al numero B 
print ("#"*14, "¿ Es el numero A mayor al numero B ?", "#"*14)
isMayor = numeroA > numeroB
print (isMayor)
# preguntar si los numeros A y B son diferentes
print ("#"*14, "¿ Son los numeros A y B diferentes ?", "#"*14)
isNumerosDiferentes = numeroA != numeroB
print (isNumerosDiferentes)
# preguntar si los numeros A y B son iguales
print ("#"*14, "¿ Son los numeros A Y B iguales ?", "#"*14)
isNumerosIguales = numeroA == numeroB
print (isNumerosIguales)
# Aplicando las diferentes operaciones a los dos valores definidos
# Sumando los dos valores definidos 
sumar = numeroA + numeroB
print (f"la suma dio {sumar} exitosamente")
# Restando los dos valores definidos
restar = numeroA - numeroB
print (f"la resta dio {restar} exitosamente")
# Multiplicando los dos valores definidos 
multiplicar = numeroA * numeroB
print (f"la multiplicar dio {multiplicar} exitosamente")
# Dividiendo los dos valores definidos
dividir = numeroA / numeroB
print (f"la dividir dio {dividir} exitosamente")
# Potenciacion con los dos valores definidos
potenciacion = numeroA ** numeroB
print (f"la potenciacion dio {potenciacion} exitosamente")