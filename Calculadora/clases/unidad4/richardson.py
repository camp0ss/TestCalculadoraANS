from .finitas import Finitas
from sympy.parsing.sympy_parser import parse_expr
import numpy as np
import pandas as pd


def finite_generator(f2,arg_h2,p2, me2, nvl2):
    lst_temp = list()
    #primer derivada hacia adelante
    if me2 == 1:
        for SDX in range(nvl2):
            cas = Finitas(f2, arg_h2, p2)
            uwu = cas.first_forward_diff()
            uwu =  uwu.get("estimateValue")
            lst_temp.append(uwu)
            arg_h2= (arg_h2/2)
        return matrix_generator(lst_temp)
    #primer derivada hacia atras
    elif me2 == 2:
        for SDX in range(nvl2):
            cas = Finitas(f2, arg_h2, p2)
            uwu = cas.first_backward_diff()
            uwu =  uwu.get("estimateValue")
            lst_temp.append(uwu)
            arg_h2= (arg_h2/2)
        return matrix_generator(lst_temp)
    #segunda derivada hacia adelante
    elif me2 == 3:
        for SDX in range(nvl2):
            cas = Finitas(f2, arg_h2, p2)
            uwu = cas.second_forward_diff()
            uwu =  uwu.get("estimateValue")
            lst_temp.append(uwu)
            arg_h2= (arg_h2/2)
        return matrix_generator(lst_temp)
    #segunda derivada hacia atras
    elif me2 == 4:
        for SDX in range(nvl2):
            cas = Finitas(f2, arg_h2, p2)
            uwu = cas.second_backward_diff()
            uwu =  uwu.get("estimateValue")
            lst_temp.append(uwu)
            arg_h2= (arg_h2/2)
        return matrix_generator(lst_temp)
    #Centrada de segundo order
    elif me2 == 5:
        for SDX in range(nvl2):
            cas = Finitas(f2, arg_h2, p2)
            uwu = cas.central_second_order()
            uwu =  uwu.get("estimateValue")
            lst_temp.append(uwu)
            arg_h2= (arg_h2/2)
        return matrix_generator(lst_temp)
    #Centrada de cuarto order
    elif me2 == 6:
        for SDX in range(nvl2):
            cas = Finitas(f2, arg_h2, p2)
            uwu = cas.central_fourth_order()
            uwu =  uwu.get("estimateValue")
            lst_temp.append(uwu)
            arg_h2= (arg_h2/2)
        return matrix_generator(lst_temp)
    #Primera derivada con primera formula 3 puntos
    elif me2 == 7:
        for SDX in range(nvl2):
            cas = Finitas(f2, arg_h2, p2)
            uwu = cas.three_points_0()
            uwu =  uwu.get("estimateValue")
            lst_temp.append(uwu)
            arg_h2= (arg_h2/2)
        return matrix_generator(lst_temp)
    #Primera derivada con segunda formula 3 puntos
    elif me2 == 8:
        for SDX in range(nvl2):
            cas = Finitas(f2, arg_h2, p2)
            uwu = cas.three_points_1()      
            uwu =  uwu.get("estimateValue")     
            lst_temp.append(uwu)
            arg_h2= (arg_h2/2)
        return matrix_generator(lst_temp)
    #Cuarta derivada hacia adelante
    elif me2 == 9:
        for SDX in range(nvl2):
            cas = Finitas(f2, arg_h2, p2)
            uwu = cas.fourth_derivate_forward()    
            uwu =  uwu.get("estimateValue")
            lst_temp.append(uwu)
            arg_h2= (arg_h2/2)
        return matrix_generator(lst_temp)
    
def funcionimportante (nivelprevio, k, i):
    ##print("IMPRIMIENDO ENTRADA DE LA FUNCION IMPORTANTE:\n",nivelprevio)
    k = k -1
    i = i -1

    valorparak = (((4**k)*(nivelprevio[(i+1)]))/((4**k)-1))-(1*(nivelprevio[i])/((4**k)-1))
    print("Debug: ",type(k), type(nivelprevio[i]), type(i))

    return valorparak

#funcion que genera las nuevas clumnas
def generadordecolumnas(nivelprevio,numeronivelacrear,iteraciones):
    listita = list()
    cantidad = len(nivelprevio)
    for xd in range(1, iteraciones+1):
        listita.append(funcionimportante(nivelprevio,numeronivelacrear,xd))
    for xd in range(cantidad-iteraciones):
        listita.append(0)
    ##print("imprimiendo listita", listita)
    listafinal = []
    for i in range(cantidad):
        listafinal.append([])
        listafinal[i].append(listita[i])
    ##print("columna generada = \n", listafinal)
    return listafinal

def matrix_generator(lst_finitegenerator):
    listafinal = []
    cantidad = len(lst_finitegenerator)
    for i in range(cantidad):
        listafinal.append([])
        listafinal[i].append(lst_finitegenerator[i])
        ##print("columna generada = \n", listafinal)
    return listafinal


class Richardson:

    def __init__(self, f,arg_h,p, me, nvl):
        #f = funcion
        #arg_h = h o espaciado
        #p = punto a evaluar en la derivada uwu
        #me = metodo de diferencias finitas que servira de entrada a Richardson
        self.funcion = f
        self.hx1 = arg_h
        self.punto= p
        self.method = me
        self.level = nvl

    def resultado(self):
        iteraciones = self.level
        nivel = self.level
        matriz = np.array(finite_generator(self.funcion,self.hx1,self.punto,self.method,self.level))
        #print("imprimiendo matriz\n", matriz)
        for MX4 in range (nivel):
            #print("MX4 = ", MX4)
            iteraciones = iteraciones - 1
            listak = list ()        
            listak = matriz[:,MX4]
            newlevel = generadordecolumnas(listak,(MX4+2),iteraciones)
            matriz = np.append(matriz, newlevel, axis=1)
        matriz = pd.DataFrame(matriz)
        html = matriz.to_html()
        #print(matriz)
        #extraemos la penultima columna, pues contiene la respuesta
        valor =matriz.loc[:,[(nivel-1)]]
        #ahora teniendo solo la penultima columna, extraemos el valor de la primera fila.
        respuesta =  valor.iat[0,0]
        solu = {"tabla": html, "respuesta": respuesta, "metodo":"Extrapolación de Richardson"}
        return solu
