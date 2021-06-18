
from math import sin
from math import exp
import pandas as pd

import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr


class Muller:

    """ docstring for Muller."""

    def __init__(self, funcion, cifras, lista):

        ''' Inicializo las variables que voy a utilizar,
			siendo las ingresadas por el usuario.'''

        self.funcion = funcion
        self.cifras = cifras
        self.valores = lista

    ''' Esta función la utilizamos para hacer las evaluaciones
        con los distintos valores de "x" y implementamos la
        estructura de control "try-except".'''

    def evaluar(funcion, valor):
        try:
            retornar = funcion.evalf(subs={"x":valor})
            return retornar
        except ZeroDivisionError:
            retornar = 1
            return retornar

    def resultado(self):
        iteracion = 1
        repetir = True
        lstxr = list()
        lsterror = list()
        lstiteracion = list()
        es = 0.5*10**(2-self.cifras)

        while repetir:
            func = []
            for x in self.valores:
                        func.append(Muller.evaluar(self.funcion, x))
            h0=self.valores[1]-self.valores[0]
            h1=self.valores[2]-self.valores[1]
            amp0 = (func[1]-func[0])/h0
            amp1 = (func[2]-func[1])/h1
            a = (amp1 - amp0)/(h1+h0)
            b = a*h1+amp1
            c = func[2]
            d = (((b)**2)-4*a*c)**(1/2)
            if abs(b+d)>abs(b-d):
                xr = self.valores[2] + (-2*c)/(b+d)
            else:
                xr = self.valores[2] + (-2*c)/(b-d)
            ea = abs((xr-self.valores[2])/xr)*100
            if ea < es:
                repetir = False
            self.valores = [self.valores[1], self.valores[2], xr]
            lstiteracion.append(iteracion)
            lstxr.append("{0:.15f}".format(xr))
            lsterror.append("{0:.15f}".format(ea))
            iteracion+=1

        d = {"Iteracion":lstiteracion,"Xr":lstxr,"Error":lsterror}
        resu = pd.DataFrame(d)
        print(resu)
        html = resu.to_html() #pasar a tabla HTML
        print("\nRaíz es: ", xr)
        salida = {"tabla":html, "raiz":xr, "error":ea,"funcion":sp.rcode(self.funcion),
         "metodo":"Muller", "graficar":"si"} #grafica
        return salida

#ecuacion = parse_expr("exp(sin(x)**3) + x**6 - 2*x**4 - x**3 - 1")
#prueba= Muller(ecuacion,3,[1.2,1.6,2])
#prueba.resultado()
