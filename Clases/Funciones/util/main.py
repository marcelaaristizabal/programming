import operaciones_matematicas as opm 
import operaciones_strings as ops
#--------Mensajes--------#
MENSAJE_OPERACION='{} las dos entradas'
ops.linedesing(12)
numeroA = int (input('Ingrese un número A'))
numeroB = int (input('Ingrese un número B'))
ops.linedesing(12)
print(MENSAJE_OPERACION.format('Sumando'))
opm.calcular (opm.sumar,numeroA,numeroB)
ops.linedesing(12)
ops.linedesing(12)
print(MENSAJE_OPERACION.format('Restando'))
opm.calcular (opm.restar,numeroA,numeroB)
ops.linedesing(12)
ops.linedesing(12)
print(MENSAJE_OPERACION.format('Multiplicando'))
opm.calcular (opm.multiplicar,numeroA,numeroB)
ops.linedesing(12)
ops.linedesing(12)
print(MENSAJE_OPERACION.format('Dividiendo'))
opm.calcular (opm.dividir,numeroA,numeroB)
ops.linedesing(12)