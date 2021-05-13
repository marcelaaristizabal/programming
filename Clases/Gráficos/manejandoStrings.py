#Strings ----> Similares a una lista ya que convierten una línea de palabras en una lista (cada strings ). Se copian o agregan elementos a una lista.Se le pueden realizar muchas operaciones.
texto = ' Hola espero que todo ande bien'
lista = [1,434,53,2,2]
lista.sort ()
print (lista)
lista.pop (2)
for elemento in lista:
    print (elemento)
for i in range (len(lista)):
    print (lista[i])

for letra in texto : 
    print (letra)

print (texto[1]) # Como el texto son una lista de strings si se pide mostrar las posiciones se puede hacer. Los Strings son como listas.
#Se le pueden quitar espacios entre palabras.
palabras = texto.split (' ') # Split---> Dividirlo cada vez que va un espacio. 
print (palabras)
print (type(palabras)) #Conversión a una lista de strings donde cada strings es una palabra.
eliminarE = texto.split ('e') #Elimina o da un salto cada vez que se encuentra la letra 'E'.
datos = 'nombre;apellido;edad'
print (datos.split(';'))
print (eliminarE)

uniendo = 'i'.join (eliminarE) #Para convertirlos nuevamente en Strings. Unir los elementos de la lista unidos por 'nada' o por una letra. Reemplazar una letra por otra tras eliminarla.
print (uniendo)
info = ' '.join (datos.split (';')) # Separar las palabras por espacios tras eliinar los ';'
print (info)

listaNombres = ['Laura',' Juan','Mario','Elsa','Katherine','daniel','Raúl','©']
print (max(listaNombres)) #Usando el código ASCII la 'd' minúscula vale más. En strings se compara diferente.
print (max(listaNombres, key = len)) #Calcula el nombre más grande, mayor cantidad de letras normales.


respuesta = input('Ingrese Si o No : ' )
print(respuesta.upper()) #Upper ---> Convierte las letras en mayúscula para no presentar problemas en la validación por la escritura. Los () indican que Upper es una función y pide ejecución.
if respuesta.upper == 'Si':
    print('Hola. Bienvenido al programa')
else:
    print('Hasta luego...😲')

nombre =  input('Ingrese su nombre : ')
print(nombre.capitalize()) #Capitalize----> Convierte la primera letra de una palabra en Mayúscula...Es una función y para ejecutarla se necesitan (). Generalmente es la primera letra.
print (type(nombre))  #Clase 'Str' con funciones en su interior como Capitalize o Upper.

correo = 'ESPERO QUE ESTES BIEN'
print (correo.casefold().capitalize()) #Casefold----> Convierte en minúscula las letras que están en mayúscula y al agregar Capitalize solo queda en mayúscula la primera letra. ¡WOW!
saludo = 'Hola como estas?'
nombre= 'Maria Alejandra'
nombre = 'maria alejandra' #Para hacer las mayúsculas debe verse bien que las separa (Split)
nombres = nombre.split(' ') #Genera una lista de nombres.
nombre = ''
for elemento in nombres :
    nombre += elemento.capitalize() +' '
print (nombre)
print (saludo.center (50)) #Center---> Toma en cuenta las palabras y los espacios entre letras y el resto lo divida en un espacio entre antes de las palabras y después de las palabras.
print (nombre.center (50))

enunciado = 'hola hola ya me cansé de decir tantos hola pero como vamos hola'
print (enunciado.upper().count('HOLA')) #Contar las palabras repetidas en una línea de Strings sin importar su escritura porque lo convierte todo en mayúsculas y son iguales.

print (enunciado.find ('decir')) #indica la posición en la lista de Srings...
print (enunciado [25:30]) #---> Posición de acuerdo al lugar u número de caracteres que determinan esta posición.

txt = 'Me gusta programar en Java'
print (txt.replace('Java', 'Python'))

numeroID= '123124'
print (numeroID.isnumeric()) #Permite detectar errores en la entrada por un usuario.

parrafo = ''

print (parrafo.endwith(' . ')) #Pregunta o valida si el párrafo termina en puntos o no devolviendo un booleano ('True' o 'False'). Puede volverse a preguntar en caso de no terminar el punto, lo vuelva a hacer.