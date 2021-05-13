from cProfile import label
import matplotlib.pyplot as plt 
def agregarElementos (pregunta1, pregunta2):
    lista1 = []
    lista2 = []
    for i in range (5):
        print (f'Ingresando dato {i+1} de 5')
        lista1.append (input (pregunta1))
        lista2.append (float(input(pregunta2)))
    return lista1, lista2

#-------------------Punto1-------------------#
preguntaSnack= 'Ingrese su snack favorito : '
preguntaPrecio = 'Ingrese el precio del snack : '
# listaSnacks, listaPrecios = agregarElementos (preguntaSnack,preguntaPrecio)
# print(listaSnacks,listaPrecios)
# plt.bar (listaSnacks,listaPrecios)
# plt.show()
#--------------Punto2--------------# 
preguntaCiudad= 'Ingrese su ciudad favorita : '
preguntaPoblacion= 'Ingrese la población : '

listaCiudades,listaPoblacion = agregarElementos (preguntaCiudad,preguntaPoblacion)
mayor = max (listaPoblacion)
ubicacion = listaPoblacion.index (mayor)
_explode = [0,0,0,0,0]
_explode[ubicacion] = 0.1

plt.pie(listaPoblacion,label=listaCiudades,explode = _explode)
plt.show ()

