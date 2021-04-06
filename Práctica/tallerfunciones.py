#Dada una lista, mostrarla elemento a elemento (función sin entradas).
def MostrarLista (lista):   
    for elemento in lista:
        print (elemento)
frutas=['manzana','piña','pera','papaya','mango']
peso= [280,308,28,159,86]
MostrarLista (frutas)
MostrarLista (peso)
#Dada una lista de números enteros, mostrar el número mayor, el número menor y el promedio.
def lista_numeros (lista):
    NUMERO_MAYOR = max (lista)
    NUMERO_MENOR = min (lista)
    cantidad = 0
    for elemento in lista:
        cantidad += elemento
    total= len (lista)
    PROMEDIO = cantidad / total
    print(f'El número mayor es {NUMERO_MAYOR},El número menor es {NUMERO_MENOR} y El promedio es {PROMEDIO}')
numeros = [16,68,13,29,4,30,6,15]
lista_numeros(numeros)

#Saludar 'n' veces
PREGUNTA_NOMBRE =' ¿Cómo te llamas? '
NOMBRE = input(PREGUNTA_NOMBRE)
PREGUNTAR_SALUDO = f'''
        ¡Hola {NOMBRE}!
        En este programa debes insertar un número entero,
        la idea es que sea la cantidad de veces 
        que quieras ser saludado
        ...
        ¿Cuántas veces deseas que te salude? Ingresa la cantidad :
'''
n = int (input(PREGUNTAR_SALUDO))
saludo = f'Hola {NOMBRE}. ¿Cómo estás?'
def saludar (saludo=0,n=0):
    return saludo * n
    for elemento in lista:
        print(elemento)
print(saludar(saludo,n))
#Devolver números pares de una lista de números enteros
