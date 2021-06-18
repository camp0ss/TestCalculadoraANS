
import math
import pandas as pd
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class Secante:

    """ docstring for Secante."""

    def __init__(self, funcion, inte_inferior, inte_superior, cifras):

        ''' Inicializo las variables que voy a utilizar,
			siendo las ingresadas por el usuario.'''

        self.cifras = cifras
        self.funcion = funcion
        self.inte_inferior = inte_inferior
        self.inte_superior = inte_superior

    ''' Esta función la utilizamos para hacer las evaluaciones
        con los distintos valores de "x" y implementamos la
        estructura de contro "try-except".'''

    def evaluar(funcion, valor):
        try:
            retornar = funcion.evalf(subs={"x":valor})
            return retornar
        except ZeroDivisionError:
            pass

    def resultado(self):

        iteracion = 1
        tol = (0.5*(10**(2-self.cifras)))
        lstieracion = list()
        lstxi = list()
        lstx2 = list()
        lstgx = list()
        lstea = list()
        print("X1 = ", self.inte_inferior)
        print("X2 = ", self.inte_superior)
        print("Decimales = 3\n" )
        error = 1
        n = 0
        x3 = 0
        while error > tol:
            lstieracion.append(iteracion)
            iteracion=iteracion+1
            lstxi.append("{0:.15f}".format(self.inte_inferior))
            lstx2.append("{0:.15f}".format(self.inte_superior))
            x3 = self.inte_inferior-((((self.inte_superior-self.inte_inferior))/(((Secante.evaluar(self.funcion, self.inte_superior))-(Secante.evaluar(self.funcion, self.inte_inferior)))))*(Secante.evaluar(self.funcion, self.inte_inferior)))
            self.inte_inferior = self.inte_superior
            self.inte_superior = x3
            error = abs(Secante.evaluar(self.funcion, x3))
            n += 1
            lstea.append("{0:.15f}".format(error))
            lstgx.append("{0:.15f}".format(x3))

        d = {"Iteracion":lstieracion,"X1":lstxi,"X2":lstx2,"Xn+1":lstgx,"Ea":lstea,"funcion":sp.rcode(self.funcion), "metodo":"Secante"}
        resu = pd.DataFrame(d)
        print(resu)
        html = resu.to_html() #pasar a tabla HTML
        print("\nRaíz es: ", x3)
        salida = {"tabla":html, "raiz":x3, "error":error,"graficar":"si"} #grafica
        return salida

#ecuacion = parse_expr("tan(x)+1")
#prueba = Secante(ecuacion,7.6,7.8,3)
#prueba.resultado()
