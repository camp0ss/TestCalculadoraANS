import numpy as np
import math
from sympy.parsing.sympy_parser import parse_expr

#Funcion para evaluar un punto en la funcion recibida
def funcion(a, f, evaluador = "x"):
        av = f.evalf(subs={evaluador:a, "e" : math.e})
        #print("datos a: ",a, "funcion: ",f, "valor: ",av)
        return av

#Funcion para calcular la cuadratura
def integraCuadGauss2p(funcionx,a,b):
    x0 = -1/np.sqrt(3)
    x1 = -x0
    xa = (b+a)/2 + (b-a)/2*(x0)
    xb = (b+a)/2 + (b-a)/2*(x1)
    area = ((b-a)/2)*(funcion(xa,funcionx) + funcion(xb,funcionx))
    return(area)
    
class cuadratura:
    def __init__(self, funcion, a, b, puntos):
         self.funcion = funcion
         self.a = a
         self.b = b
         self.tramos = puntos

    def resultado(self):
        muestras = self.tramos+1
        xi = np.linspace(self.a,self.b,muestras)
        area = 0
        for i in range(0,muestras-1,1):
            deltaA = integraCuadGauss2p(self.funcion,xi[i],xi[i+1])
            area = area + deltaA
        print('Cuadratura de Gauss: ', area)

#func = parse_expr("(e**x*sin(x))/(1+x**2)")
#aver = cuadratura(func, 0, 3, 2)
#print(aver.resultado())