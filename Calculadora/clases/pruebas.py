from unidad4.integracion import TrapecioIntervalo, Trapecio, SimpsonTercio, SimpTercIntervalo, SimpOctavo, SimpOctIntervalo,SimpAdaptativo
from unidad4.integracionListas import IntegracionNum
from unidad4.rosemberg import Rosemberg

from biseccion import Biseccion

from math import sin
from sympy.parsing.sympy_parser import parse_expr




funcion = parse_expr("(e**-x**2)")
aver = SimpAdaptativo(0, 4, 0.001, funcion)
print(aver.resultado())

#funcion = parse_expr("(e**x**2)")
#aver = Rosemberg(0, 1, 3, funcion)
#print(aver.resultado())



'''
#ejemplo integral triple:
funcion = parse_expr("x**3-2*y*z")
aver = TrapecioIntervalo(-1, 3, 8, funcion)
data = aver.resultado()
funcion = parse_expr(str(data["tabla"]))
aver = TrapecioIntervalo(0, 6, 8, funcion, "y")
data = aver.resultado()
funcion = parse_expr(str(data["tabla"]))
aver = TrapecioIntervalo(-4, 4, 8, funcion, "z")
print(aver.resultado())
'''

'''#ejemplo integral doble:
funcion = parse_expr("x**2-3*y**2+x*y**3")
aver = TrapecioIntervalo(0, 4, 4, funcion)
data = aver.resultado()
funcion = parse_expr(str(data["tabla"]))
aver = TrapecioIntervalo(-2, 2, 4, funcion, "y")
print(aver.resultado())
'''


#lstX = [0,0.1,0.2,0.3,0.4,0.5]
#lstFx = [1,7,4,3,5,2]
#aver = IntegracionNum(lstX,lstFx,6)
#print(aver.resultado())

#funcion = parse_expr("(e**x)*ln(x)*y")
#aver = SimpOctIntervalo(1, 4,3, funcion)
#print(aver.resultado())

#funcion = parse_expr("e**x/x")
#aver = Trapecio(2, 4, funcion)
#print(aver.resultado())

#funcion = parse_expr("sin(x)+1")
#aver = Diferencias_finitas(funcion, 2, 4, 1)
#aver = Biseccion(-2,-1, funcion,3)
#print(aver.resultado())

#aver = Muller(3,1.2,1.6,2)
#print(aver.resultado())
