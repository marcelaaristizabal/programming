def validateEndWith (strValidate, pregunta) :
    isCorrectData = False
    while (isCorrectData == False):
        try : 
            valor = input(pregunta)
        assert (valor.endswith(strValidate))
        isCorrectData = True
        except AssertionError: 
            print (f'datos incorrectos ingrese nuevamente y recuerde que debe terminar con "{strValidate}" ')
    return valor 

parrafo =validateEndWith('.','ingrese un parrafo.')
parrafo = parrafo[:-1]
palabras = parrafo.split(' ')
print(palabras)
print(f'la palabra más grande es "{max(palabras, key=len)}" y el menor es "{min(palabras, key=len)}"')