PREGUNTA_NUMERO = ''' Ingrese alguna de estas opciones 
    1. Hacer conversión de pesos a Dólares o Euros
    2. Agregue un valor a la lista de pesos 
    3. Mostrar valor más alto,más bajo y promedio
    4. Eliminar elemento de la lista
    5. Salir
'''


listaPesos = [20000,30000,4000,2500,1000,7600]
opcion_escogida= int(input(PREGUNTA_NUMERO))
while (opcion_escogida != 5) :
    if (opcion_escogida == 1) :
        print('Escogiste la opción 1')
    elif (opcion_escogida == 2 ) :
        print('Escogiste la opción 2')
    elif (opcion_escogida == 3) :
        print (' Escogiste la opción 3')
    elif (opcion_escogida == 4) :
        print ('Escogiste la opción 4')
    else :
        print ('Respuesta no válida')
    opcion_escogida =int(input(PREGUNTA_NUMERO))

print ('Feliz día')