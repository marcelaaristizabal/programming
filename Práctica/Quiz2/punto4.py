listaPesos = [20000,30000,4000,2500,1000,7600]
PREGUNTA_BORRAR_COORDENADA ='Ingrese la posición que desee borrar : '
posicion = int (input(PREGUNTA_BORRAR_COORDENADA)) - 1
print (listaPesos)
listaPesos.pop (posicion)
print (listaPesos)