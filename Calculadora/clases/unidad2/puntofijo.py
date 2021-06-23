

#Revisar

import math
import pandas as pd
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class PuntoFijo:

    """ docstring for Secante."""

    def __init__(self, funcion, intervalo, cifras):

        ''' Inicializo las variables que voy a utilizar,
			siendo las ingresadas por el usuario.'''

        self.cifras = cifras
        self.funcion = funcion
        self.intervalo = intervalo

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

    ''' En esta función hacemos el desarrollo matematico y
        retornamos los valores en tablas.'''

    def resultado(self):

        try:
            ''' Creación de variables.'''

            ea = 0
            es = -1
            ejecucion = 1

            ''' Creación de listas.'''

            lstea= list()
            lstxi = list()
            lstx2 = list()
            lstgx = list()
            lstfx1 = list()
            lstfxr = list()
            lstfx1Xfxr = list()
            lstieracion = list()

            gx = PuntoFijo.evaluar(self.funcion, self.intervalo)
            ea = abs((gx-self.intervalo)/gx)*100

            ''' Guardado de la primera iteración.'''

            lstieracion.append(ejecucion)
            lstgx.append("{0:.15f}".format(gx))
            lstea.append("{0:.15f}".format(ea))
            lstxi.append("{0:.15f}".format(self.intervalo))

            while ea >= es :

                es = (0.5*(10**(2-self.cifras)))
                self.intervalo = gx
                gx = PuntoFijo.evaluar(self.funcion, self.intervalo)
                ea = abs((gx-self.intervalo)/gx)*100
                print(gx)
                ''' Guardado de las iteraciones.'''

                lstieracion.append(ejecucion)
                lstxi.append("{0:.15f}".format(self.intervalo))
                lstgx.append("{0:.15f}".format(gx))
                lstea.append("{0:.15f}".format(ea))
                ejecucion = ejecucion + 1

            d = {"Iteracion":lstieracion,"Xi":lstxi,"g(x)":lstgx,"ea":lstea}
            resu = pd.DataFrame(d)
            print(resu)
            html = resu.to_html() #pasar a tabla HTML
            print("\nRaíz es: ", "{0:.15f}".format(gx))
            salida = {"tabla":html, "raiz":"{0:.15f}".format(gx), "error":"{0:.15f}".format(ea),
            "funcion":sp.rcode(self.funcion), "metodo":"Punto fijo",
            "graficar":"si"} #grafica
            return salida
        except TypeError:
            salida = {"Error":"No se puede operar", "metodo":"Punto fijo"}
            return salida



#ecuacion = parse_expr("tan(x)+1")
#prueba = PuntoFijo(ecuacion,7.04,3)
#prueba.resultado()
