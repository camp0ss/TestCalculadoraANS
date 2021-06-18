import decimal
import math
import numpy as np
import pandas as pd
import sympy as sym
from sympy import *


class Newton_divididas:
    def __init__(self,tx,ty,p, f = sympify("x")):
        #f = funcion
        #t = lista con valores de x
        #e = valor de x que se busca en la funcion
        self.tablax = tx
        self.tablay = ty
        self.punto = p
        self.funcion = f

    def factorial(n):
        if n<=1:
            return 1 
        return n*factorial(n-1) 

    def resultado(self):
        
        x, y, z = symbols('x y z')
        init_printing(use_unicode=True)
        init_printing()

        convertido2 = self.funcion
        valor_real = convertido2.subs(x, self.punto)
        evaluador = self.punto
        yi = self.tablay 
        lstxi = list()
        lstxi = self.tablax
        lstfi = list()
        
        if len(yi) == 0:
            #generando valores de fx
            for uwu in lstxi:
                temp = convertido2.subs(x, uwu)
                lstfi.append(temp)
        else:
            lstfi = yi #se nos dio una tabla con valores de y, pasamos la entrada a fi

    
        #codigo para derivar

        deri = diff(convertido2,x,len(lstxi))
        deri.expand()
        derivada = deri.subs(x, evaluador)

        #pasamos los arrays de python, a arrays de numpy
        xi = np.array(lstxi)
        fi = np.array(lstfi)

        #guardamos los arrays de numpy a pandas.
        posicion_insertar=2
        df = pd.DataFrame(list(zip(lstxi,lstfi)), 
                    columns =[" ","b(0)"]) 

        n = len(xi)
        ki = np.arange(0,n,1)
        tabla = np.concatenate(([ki],[xi],[fi]),axis=0)
        tabla = np.transpose(tabla)
        dfinita = np.zeros(shape=(n,n),dtype=float)
        tabla = np.concatenate((tabla,dfinita), axis=1)
        [n,m] = np.shape(tabla)
        diagonal = n-1
        j = 3

        while (j < m):
            lstdivisor = list()
            nombre_columna = 'b('+str(j-2)+')' #guardamos el nombre de la columna
            i = 0
            paso = j-2 
            while (i < diagonal):
                denominador = (xi[i+paso]-xi[i]) #nos movemos entre la tabla para calcular las diferencias.
                numerador = tabla[i+1,j-1]-tabla[i,j-1] #nos movemos entre la tabla para calcular las diferencias.
                tabla[i,j] = numerador/denominador #se agrega el resultado a numpy
                lstdivisor.append(numerador/denominador)  #se agrega el resultado a pandas
                i = i+1
                
            diagonal = diagonal - 1
            j = j+1

            #este codigo agrega las diferencias calculadas en una nueva columna de pandas
            for x in range (0, len(lstxi)):
                if len(lstfi) != len(lstdivisor):
                    lstdivisor.append(" ")
            df.insert(posicion_insertar,nombre_columna,lstdivisor,True)
            posicion_insertar = posicion_insertar +1
            
        #esta parte calcula el polinomio de interpolacion
        dDividida = tabla[0,3:]
        n = len(dfinita)
        x = sym.Symbol('x')
        polinomio = fi[0]
        for j in range(1,n,1):
            factor = dDividida[j-1]
            termino = 1
            for k in range(0,j,1):
                termino = termino*(x-xi[k])
            polinomio = polinomio + termino*factor


        polisimple = polinomio.expand()
        #hace el polinimio una funcion evaluable
        px = sym.lambdify(x,polisimple)

        muestras = 101
        a = np.min(xi)
        b = np.max(xi)
        pxi = np.linspace(a,b,muestras)
        pfi = px(pxi)

        #esta parte calcula el error teorico
        multi = 1
        for lista in lstxi: 
            multi = multi * evaluador-lista 

        errorTeorico = (derivada/factorial(len(lstxi)))*multi 
        evaluacion = polisimple.subs(x,evaluador) #evaluando x en el polinimio
        er100 = (abs((valor_real-polisimple.subs(x,evaluador))/valor_real))*100 #calculando error porcentual

        #convierte el dataframe de pandas a una tabla HTML
        html = df.to_html()
        '''
        print(df)
        print('\nPolinomio completo = \n ',polinomio)
        print('\nPolinomio simplificado = \n', polisimple)
        print("\nResultado de evaluar en el punto: " ,evaluador, " = ", evaluacion)
        print("\nError porcentual = ", er100 , "%")
        print("\nError teorico= ", errorTeorico) 
        '''

        if len(yi) != 0:
            #no tenemos informacion para encontrar los errores.
            salida = {"sin_simplificar":polinomio,
                    "simple":polisimple,
                    "evalucion":evaluacion,
                    "valor_real": 0,
                        "errorx100": 0,
                    "errorteorico": 0,
                    "tabla" : html,
                    "graficar":"si"
                    } 
        else:
            salida = {"sin_simplificar":polinomio,
                    "simple":rcode(polisimple),
                    "evalucion":evaluacion,
                    "valor_real": valor_real,
                        "errorx100": er100,
                    "errorteorico": errorTeorico,
                    "tabla" : html,
                    "funcion":rcode(self.funcion), "metodo":"Newton Diferencias Divididas",
                    "graficar":"si"
                    } 
        return salida

    