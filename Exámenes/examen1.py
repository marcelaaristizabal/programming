# Desarrollar progrma que permita que el personal de la salud ingrese el nivel de triglicéridos y homocisteína
#----Mensajes TRIGLICÉRIDOS----#
MENSAJE_SALUDO = "Hola,espero que te encuentres bien. Calcularé tus niveles de TRIGLICÉRIDOS y HOMOCISTEÍNA en sangre."
MENSAJE_HOMOCISTEÍNA = "Tus niveles de HOMOCISTEÍNA se encuentran en estado ..."
MENSAJE_TRIGLICÉRIDOS = "Tus niveles de TRIGLICÉRIDOS se encuentran en estado ..."
MENSAJE_OPTIMO_TG = "Muy bien. Tus niveles de TRIGLICÉRIDOS están dentro del rango adecuado."
MENSAJE_OPTIMO_HMC = "Muy bien. Tus niveles de HOMOCISTEÍNA están dentro del rango adecuado."
MENSAJE_SOBRE_EL_LIMITE_OPTIMO_TG = "Bien. Tus niveles de TRIGLICÉRIDOS no han sobrepasado el límite."
MENSAJE_SOBRE_EL_LIMITE_OPTIMO_HMC= "Bien. Tus niveles de HOMOCISTEÍNA no han sobrepasado el límite."
MENSAJE_ALTO_TG= "Ten cuidado. Tus niveles de TRIGLICÉRIDOS están altos.Tu salud está en riesgo."
MENSAJE_ALTO_HMC = "Ten cuidado. Tus niveles de HOMOCISTEÍNA están altos.Tu salud está en riesgo."
MENSAJE_MUY_ALTO_TG = "Advertencia: Niveles de TRIGLICÉRIDOS están muy altos.Existe posibilidad de hiperlipidemia."
MENSAJE_MUY_ALTO_HMC = "Advertencia: Niveles de HOMOCISTEÍNA están muy altos.Existe posibilidad de hiperhomocisteinemia."

#----Preguntas----#
PREGUNTA_TRIGLICERIDOS= "Ingresa tus niveles de TRIRGLICÉRIDOS : "
PREGUNTA_HOMOCISTEINA= "Ingresa tus niveles de HOMOCISTEÍNA : "

#----Entradas al código TRIGLICÉRIDOS----#
print (MENSAJE_SALUDO)
trigliceridos = float (input(PREGUNTA_TRIGLICERIDOS))
IsOptimoTrigliceridos = trigliceridos < 150  
isSobreLimiteOptimo_TG = trigliceridos >= 150 and trigliceridos < 199
IsAlto_TG = trigliceridos >= 200 and trigliceridos < 500
IsMuyAlto_TG = trigliceridos > 500
resultado = ""
#----Condicionales TRIGLICÉRIDOS----#
if (IsOptimoTrigliceridos) :
    resultado = MENSAJE_OPTIMO_TG
elif (isSobreLimiteOptimo_TG) :
    resultado = MENSAJE_SOBRE_EL_LIMITE_OPTIMO_TG
elif (IsAlto_TG) : 
    resultado = MENSAJE_ALTO_TG
else :
    resultado = MENSAJE_MUY_ALTO_TG

print (resultado)

#----Entradas al código HOMOCISTEÍNA----#
homocisteina = float (input (PREGUNTA_HOMOCISTEINA))
IsOptimoHomocisteina = homocisteina >= 2 and homocisteina < 15
IsSobreLimiteOptimo_HMC = homocisteina >= 15 and homocisteina < 30
IsAlto_HMC = homocisteina >= 30 and homocisteina < 100
IsMuyAlto_HMC = homocisteina >= 100
resultado = ""

#----Condicionales HOMOCISTEÍNA----#
if (IsOptimoHomocisteina) :
    resultado = MENSAJE_OPTIMO_HMC
elif (IsSobreLimiteOptimo_HMC) :
    resultado = MENSAJE_SOBRE_EL_LIMITE_OPTIMO_HMC
elif (IsAlto_HMC) :
    resultado = MENSAJE_ALTO_HMC
else :
    resultado = MENSAJE_MUY_ALTO_HMC

print(resultado)