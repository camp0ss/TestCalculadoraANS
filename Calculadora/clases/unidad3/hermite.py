import decimal
import math
import numpy as np
import pandas as pd
import sympy as sym
from scipy.interpolate import lagrange
from sympy import *
from math import *
from sympy.parsing import sympy_parser

def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1) 

class Hermite:

    def __init__(self, p_eva,matrizz):
        #x = lista con valores de x
        #p_eva = punto de evaluacion
        #y = lista con valores de y
        #fp1x = lista con valores de x prima 1
        #fp2x = lista con valores de x prima 2
        #fp3x = lista con valores de x prima 3
        #... #fp5x = lista con valores de x prima 5
        self.puntoeva = p_eva
        self.matriz = matrizz
        
    def resultado(self):

        evaluador = self.puntoeva

        #                   x f(x) f'(x) f''(x) ... f^n(x)

        matrix = np.array(self.matriz)
        print(matrix)


        lstf1 = np.arange(len(matrix[0]))

        for indice in range(2,len(matrix)):
            index = 0
            for matx in matrix[indice]:
                if matx != "-":
                    lstf1[index] = indice
                index += 1

        lstX = []
        lstY = []
        lstA = []

        for indice in matrix[0]:
            lstA.append(float(indice))
        ite = 0
        ite2 = 0

        for index in range(2):
            for indice in matrix[index]:
                while ite2<lstf1[ite]:
                    if index == 1:
                        lstX.append(float(indice))
                    else:
                        lstY.append(float(indice))
                    ite2 +=1  
                ite2 = 0  
                ite+=1
            ite = 0

        xi = np.array(lstY)
        fi = np.array(lstX)

        posicion_insertar=2
        df = pd.DataFrame(list(zip(lstY,lstX)), 
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

        #print("Inicio: \n",tabla)
        ite = 2 #iterador
        while (j < m):
            lstdivisor = list()
            nombre_columna = 'b('+str(j-2)+')'
            i = 0
            paso = j-2
            
            while (i < diagonal):
                denominador = (xi[i+paso] - xi[i])
                numerador = tabla[i+1,j-1] - tabla[i,j-1]
                if denominador == 0 and numerador == 0:
                    if matrix[ite][lstA.index(xi[i])] != "-" :
                        tabla[i,j] = float(matrix[ite][lstA.index(xi[i])])/factorial(ite-1)
                        lstdivisor.append(float(matrix[ite][lstA.index(xi[i])])/factorial(ite-1))
                else:
                    tabla[i,j] = numerador/denominador
                    lstdivisor.append(numerador/denominador)
                i = i+1
                        
            diagonal = diagonal - 1
            j = j+1
            for x in range (0, len(lstY)):
                if len(lstX) != len(lstdivisor):
                    lstdivisor.append(" ")
            df.insert(posicion_insertar,nombre_columna,lstdivisor,True)
            posicion_insertar = posicion_insertar +1
            #print("----------------------------")
            #print(tabla)
            ite +=1    

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

        px = sym.lambdify(x,polisimple)

        muestras = 101
        a = np.min(xi)
        b = np.max(xi)
        pxi = np.linspace(a,b,muestras)
        pfi = px(pxi)

        html = df.to_html
        evaluacion2 = polisimple.subs(x,evaluador)
        #Tabla
        '''
        print("\nResultado: \n",df)
        print('\nPolinomio sin simplificar: ', polinomio)
        print('\nPolinomio simplificado: ',polisimple)
        print("\nResultado de evaluar en el punto: " ,evaluador, " = ", evaluacion2)
        '''

        salida = {"sin_simplificar":polinomio,
                    "simple":rcode(polisimple),
                    "evalucion":evaluacion2,
                    "tabla" : html,
                    "metodo": "Hermite"
                    }
        return salida
