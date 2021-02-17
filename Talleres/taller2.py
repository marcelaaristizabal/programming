#----Constantes----#
ENTRADA_1 = "Ingrese número A, por favor : "
ENTRADA_2 = "Ingrese número B, por favor : "

MENSAJE_BIENVENIDA = "Hola, es un placer interactuar contigo"
MENSAJE_AVISO = "Voy a hacer varias comparaciones y operaciones matemáticas con los números que ingresaste"

#----Entrada al código----#
print (MENSAJE_BIENVENIDA)
numeroA = int (input (ENTRADA_1))
numeroB = int (input (ENTRADA_2))
print (MENSAJE_AVISO)
print ("#"*20, "CARGANDO...", "#"*20)

#----Comparaciones y preguntas con los datos ingresados por el usuario----#
# Preguntar si el número A es mayor al número B 
print ("#"*17, "¿ Es el número A mayor al número B ?", "#"*17)
isMayor = numeroA > numeroB
print (f"El resultado de si A es mayor que B es ...", isMayor)
# Preguntar el número A es menor al número B
print ("#"*17, "¿ Es el número A menor al número B ?", "#"*17)
isMenor = numeroA < numeroB
print (f"El resultado de si A es menor que B es ... ", isMenor)
# Preguntar si los números A y B son diferentes
print ("#"*17, "¿ Son los números A y B diferentes ?", "#"*17)
isNumerosDiferentes = numeroA != numeroB
print (f"El resultado de si A y B son diferentes es ...", isNumerosDiferentes)
# Preguntar si los números A y B son iguales
print ("#"*17, "¿ Son los números A Y B iguales ?", "#"*17)
isNumerosIguales = numeroA == numeroB
print (f"El resultado de si A y B son iguales es ...", isNumerosIguales)

#----Operaciones matemáticas con los datos ingresados por el usuario----#
# Sumando los dos valores ingresados
sumar = numeroA + numeroB
print(f"La suma de los datos ingresados dio {sumar} exitosamente")
# Restando los dos valores ingresados
restar = numeroA - numeroB
print(f"La resta de los datos ingresados dio {restar} exitosamente")
# Multiplicando los dos valores ingresados
multiplicar = numeroA * numeroB
print (f"La multiplicación de los datos ingresados dio {multiplicar} exitosamente")
# Dividiendo los dos valores ingresados
dividir = numeroA / numeroB
print (f"La división de los datos ingresados dio {dividir} exitosamente")
# Potenciación con los dos valores ingresados
potenciacion = numeroA**numeroB
print (f"La potenciación con los datos ingresados dio {potenciacion} exitosamente")