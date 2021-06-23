
import math
import pandas as pd
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class Falsa_posicion:

    """ docstring for Falsa_posicion."""

    def __init__(self, funcion, inte_inferior, inte_superior, cifras):

        ''' Inicializo las variables que voy a utilizar,
			siendo las ingresadas por el usuario.'''

        self.ejecucion = 1
        self.cifras = cifras
        self.funcion = funcion
        self.inte_inferior = inte_inferior
        self.inte_superior = inte_superior

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

    def aproximacion(funcion, intervalo_infe, intervalo_supe):
        retornar = intervalo_infe-(((Falsa_posicion.evaluar(funcion, intervalo_infe))*(intervalo_infe-intervalo_supe))/((Falsa_posicion.evaluar(funcion, intervalo_infe))-(Falsa_posicion.evaluar(funcion, intervalo_supe))))
        return retornar

    ''' En esta función hacemos el desarrollo matematico y
        retornamos los valores en tablas.'''

    def resultado(self):

        try:
            ''' Creación de variables.'''

            exit = False
            intervalo_xr = 0
            eval_funcion1 = 0
            eval_funcion2 = 0
            pro_funciones = 0
            error_aproximado = 0
            nivel_tolerancia = -1

            ''' Creación de listas.'''

            lstea= list()
            lstx1 = list()
            lstx2 = list()
            lstxr = list()
            lstfx1 = list()
            lstfxr = list()
            lstfx1Xfxr = list()
            lstieracion = list()

            if ((Falsa_posicion.evaluar(self.funcion, self.inte_inferior))*(Falsa_posicion.evaluar(self.funcion, self.inte_superior))) < 0:

                ''' Cálculo de la primera iteración.'''

                intervalo_xr = Falsa_posicion.aproximacion(self.funcion, self.inte_inferior, self.inte_superior)
                eval_funcion1 = Falsa_posicion.evaluar(self.funcion, self.inte_inferior)
                eval_funcion2 = Falsa_posicion.evaluar(self.funcion, intervalo_xr)
                pro_funciones = eval_funcion1*eval_funcion2

                ''' Guardado de la primera iteración.'''

                lstieracion.append(self.ejecucion)
                lstxr.append("{0:.9f}".format(intervalo_xr))
                lstfx1.append("{0:.9f}".format(eval_funcion1))
                lstfxr.append("{0:.9f}".format(eval_funcion2))
                lstea.append("{0:.9f}".format(error_aproximado))
                lstx1.append("{0:.9f}".format(self.inte_inferior))
                lstx2.append("{0:.9f}".format(self.inte_superior))
                lstfx1Xfxr.append("{0:.9f}".format(pro_funciones))

                while error_aproximado > nivel_tolerancia or exit == True:

                    nivel_tolerancia = (0.5*(10**(2 - self.cifras)))
                    xrprevio = intervalo_xr

                    if pro_funciones == 0:
                        exit = True
                        print("Encontrado es xr", intervalo_xr)
                    elif pro_funciones < 0:
                        self.inte_inferior = self.inte_inferior
                        self.inte_superior = intervalo_xr
                    else:
                        self.inte_superior = self.inte_superior
                        self.inte_inferior = intervalo_xr


                    ''' Cálculo de las iteraciones'''

                    intervalo_xr = Falsa_posicion.aproximacion(self.funcion, self.inte_inferior, self.inte_superior)
                    eval_funcion1 = Falsa_posicion.evaluar(self.funcion, self.inte_inferior)
                    eval_funcion2 = Falsa_posicion.evaluar(self.funcion, intervalo_xr)
                    pro_funciones = eval_funcion1*eval_funcion2
                    error_aproximado = abs((intervalo_xr - xrprevio)/intervalo_xr)*100

                    ''' Guardado de las iteraciones.'''

                    self.ejecucion = self.ejecucion + 1
                    lstieracion.append(self.ejecucion)
                    lstxr.append("{0:.9f}".format(intervalo_xr))
                    lstfx1.append("{0:.9f}".format(eval_funcion1))
                    lstfxr.append("{0:.9f}".format(eval_funcion2))
                    lstea.append("{0:.9f}".format(error_aproximado))
                    lstx1.append("{0:.9f}".format(self.inte_inferior))
                    lstx2.append("{0:.9f}".format(self.inte_superior))
                    lstfx1Xfxr.append("{0:.9f}".format(pro_funciones))

                d = {"Iteracion":lstieracion,"X1":lstx1,"X2":lstx2,"Xr":lstxr,"f(X1)":lstfx1,"f(Xr)":lstfxr,"f(X1)*f(Xr)":lstfx1Xfxr,"Ea":lstea}
                resu = pd.DataFrame(d)
                print(resu)
                html = resu.to_html() #pasar a tabla HTML
                print("\nRaíz es: ", lstxr[-1])
                salida = {"tabla":html, "raiz":lstxr[-1], "error":error_aproximado,
                "funcion":sp.rcode(self.funcion), "metodo":"Falsa posicion",
                "graficar":"si"} #grafica
                return salida
            else:
                salida = {"Error":"No se puede operar", "metodo":"Falsa posicion"}
                return salida
        except TypeError:
            salida = {"Error":"No se puede operar", "metodo":"Falsa posicion"}
            return salida

#ecuacion = parse_expr("tan(x)-x+1")
#prueba = Falsa_posicion(ecuacion,4.4,4.6,3)
#prueba.resultado()
