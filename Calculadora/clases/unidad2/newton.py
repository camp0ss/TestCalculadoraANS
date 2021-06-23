
import math
import pandas as pd
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class Newton:

    """docstring for Newton."""

    def __init__(self, funcion, intervalo, cifras):

        x = sp.Symbol('x')
        self.ejecucion = 1
        self.cifras = cifras
        self.funcion = funcion
        self.intervalo = intervalo
        self.derivada_1 = sp.diff(self.funcion, x)

    ''' Esta función la utilizamos para hacer las evaluaciones
        con los distintos valores de "x" y implementamos la
        estructura de control "try-except".'''

    def evaluar_func(funcion, valor):
        try:
            retornar = funcion.evalf(subs={"x":valor})
            return retornar
        except ZeroDivisionError:
            retornar = 1
            return retornar

    def aproximacion(funcion, funcion_dx, valor):
        retornar = valor - ((Newton.evaluar_func(funcion, valor))/(Newton.evaluar_func(funcion_dx, valor)))
        return retornar

    def resultado(self):

        try:
            ''' Creación de variables.'''

            funcion_x = 0
            funcion_dx = 0
            aproximacion = 0
            nuevo_intervalo = 0
            error_aproximado = 0
            nivel_tolerancia = -1

            ''' Creación de listas.'''

            lst_error = list()
            lst_intervalo = list()
            lst_funcion_x = list()
            lst_iteracion = list()
            lst_funcion_dx = list()
            lst_aproximacion = list()

            ''' Cálculo para el bucle y primera iteracion.'''

            funcion_x = Newton.evaluar_func(self.funcion, self.intervalo)
            funcion_dx = Newton.evaluar_func(self.derivada_1, self.intervalo)
            aproximacion = Newton.aproximacion(self.funcion, self.derivada_1, self.intervalo)
            error_aproximado = abs((aproximacion-self.intervalo)/aproximacion)*100

            ''' Guardado de la primera iteracion en la lista.'''

            lst_iteracion.append(self.ejecucion)
            lst_funcion_x.append("{0:.15f}".format(funcion_x))
            lst_funcion_dx.append("{0:.15f}".format(funcion_dx))
            lst_error.append("{0:.15f}".format(error_aproximado))
            lst_intervalo.append("{0:.15f}".format(self.intervalo))
            lst_aproximacion.append("{0:.15f}".format(aproximacion))

            while error_aproximado >= nivel_tolerancia :

                ''' Cálculo de las iteraciones y nuevo intervalo.'''

                nuevo_intervalo = aproximacion
                nivel_tolerancia = 0.5*pow(10,(2-self.cifras))
                funcion_x = Newton.evaluar_func(self.funcion, nuevo_intervalo)
                funcion_dx = Newton.evaluar_func(self.derivada_1, nuevo_intervalo)
                aproximacion = Newton.aproximacion(self.funcion, self.derivada_1, nuevo_intervalo)
                error_aproximado = abs((aproximacion-nuevo_intervalo)/aproximacion)*100

                ''' Guardado de las iteraciones en las listas.'''

                self.ejecucion = self.ejecucion + 1
                lst_iteracion.append(self.ejecucion)
                lst_funcion_x.append("{0:.15f}".format(funcion_x))
                lst_funcion_dx.append("{0:.15f}".format(funcion_dx))
                lst_error.append("{0:.15f}".format(error_aproximado))
                lst_intervalo.append("{0:.15f}".format(nuevo_intervalo))
                lst_aproximacion.append("{0:.15f}".format(aproximacion))

            d = {"Iteracion":lst_iteracion,"Xn":lst_intervalo,"F(Xn)":lst_funcion_x,"F'(Xn)":lst_funcion_dx,"Xn+1":lst_aproximacion,"ea":lst_error}
            resu = pd.DataFrame(d)
            print(resu)
            html = resu.to_html() #pasar a tabla HTML
            print("\nRaíz es: ", nuevo_intervalo)
            salida = {"tabla":html, "raiz":nuevo_intervalo, "error":error_aproximado,
            "funcion":sp.rcode(self.funcion), "metodo":"Newton",
            "graficar":"si"} #grafica
            return salida
        except TypeError:
            salida = {"Error":"No se puede operar", "metodo":"Newton"}
            return salida

#ecuacion = parse_expr("tan(x)-x+1")
#prueba = Newton(ecuacion,7.6,3)
#prueba.resultado()
