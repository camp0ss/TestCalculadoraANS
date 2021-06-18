from .clases.unidad2 import  biseccion, falsaPosicion, muller, newton, puntofijo, secante
from .clases.unidad3 import lagrange, newton_divididas, newton_recursivo, hermite
from .clases.unidad4 import integracion, rosemberg, finitas, richardson
from .clases.unidad5 import euler, runge, taylor, multipasos

import pandas as pd

#Uso de clases de archivos python 

#Unidad 2:
def biseccionModel(a,b,funcion,cifras):
    clase = biseccion.Biseccion
    resu = clase(a,b,funcion,cifras)
    return resu.resultado()

def falsaModel(funcion,a,b,cifras):
    clase = falsaPosicion.Falsa_posicion
    resu = clase(funcion,a,b,cifras)
    return resu.resultado()

def mullerModel(funcion,cifras,lista):
    clase = muller.Muller
    resu = clase(funcion,cifras,lista)
    return resu.resultado()

def newtonModel(funcion,intervalo,cifras):
    clase = newton.Newton
    resu = clase(funcion,intervalo,cifras)
    return resu.resultado()

def puntoModel(funcion,intervalo,cifras):
    clase = puntofijo.PuntoFijo
    resu = clase(funcion,intervalo,cifras)
    return resu.resultado()

def secanteModel(funcion,a,b,cifras):
    clase = secante.Secante
    resu = clase(funcion,a,b,cifras)
    return resu.resultado()

#Unidad 3:
def lagran(listaX, punto, opcion, listaY="x",funcion=""):
    if opcion ==1:
        aver = lagrange.Lagrange
        aver = aver(funcion, listaX, punto)
        resu = aver.resultado()
        return resu
    else:
        print("aqui")
        aver = lagrange.Lagrange_tabla
        aver = aver(listaX, listaY, punto)
        resu = aver.resultado()
        return resu

def divididasModel(listaX, punto, listaY="",funcion=""):
    aver = newton_divididas.Newton_divididas
    aver = aver(listaX, listaY, punto, funcion)
    resu = aver.resultado()
    return resu

def polNewtonModel(listaX, punto, listaY="",funcion=""):
    aver = newton_recursivo.Newton_recursivo
    aver = aver(listaX, listaY, punto, funcion)
    resu = aver.resultado()
    return resu

def hermiteModel(punto, matriz):
    aver = hermite.Hermite
    aver = aver(punto, matriz)
    resu = aver.resultado()
    return resu
#Unidad 4:
#Metodos de diferenciacion numerica
def diferenciacionModel(funcion, h, valorX, opcion):
    clase = finitas.Finitas(funcion, h, valorX)
    if opcion ==1:
        return clase.first_forward_diff
    if opcion ==2:
        return clase.first_backward_diff
    if opcion ==3:
        return clase.second_forward_diff
    if opcion ==4:
        return clase.second_backward_diff
    if opcion ==5:
        return clase.central_second_order
    if opcion ==6:
        return clase.central_fourth_order
    if opcion ==7:
        return clase.three_points_0
    if opcion ==8:
        return clase.three_points_1
    if opcion ==9:
        return clase.fourth_derivate_forward


#Metodos de integracion numerica
def trapecioModel(a,b,funcion):
    clase = integracion.Trapecio
    resu = clase(a,b,funcion)
    return resu.resultado()

def trapecioCompuestoModel(a,b,intervalo,funcion):
    clase = integracion.TrapecioIntervalo
    resu = clase(a,b,intervalo,funcion)
    return resu.resultado()

def simpsonTercioModel(a,b,funcion):
    clase = integracion.SimpsonTercio
    resu = clase(a,b,funcion)
    return resu.resultado()

def simpsonTercioCompuestoModel(a,b,intervalo,funcion):
    clase = integracion.SimpTercIntervalo
    resu = clase(a,b,intervalo,funcion)
    return resu.resultado()

def simpsonOctavoModel(a,b,funcion):
    clase = integracion.SimpOctavo
    resu = clase(a,b,funcion)
    return resu.resultado()

def simpsonOctavoCompuestoModel(a,b,intervalo,funcion):
    clase = integracion.SimpOctIntervalo
    resu = clase(a,b,intervalo,funcion)
    return resu.resultado()

def simpsonTercioAdaptativoModel(a,b,tolerancia,funcion):
    clase = integracion.SimpAdaptativo
    resu = clase(a,b,tolerancia,funcion)
    return resu.resultado()

#No
def listasModel(lstX,lstFx,metodo):
    clase = rosemberg.Rosemberg
    resu = clase(lstX,lstFx,metodo)
    return resu.resultado()

#Metodo de richardson
def richardsonModel(funcion, valorH, valorX,  metodo, nivel):
    clase = richardson.Richardson(funcion, valorH, valorX, metodo, nivel)
    return clase.resultado()

#Metodo de Rosemberg
def rosembergModel(limInf,limSup, nivel, func):
    clase = rosemberg.Rosemberg
    resu = clase(limInf,limSup, nivel, func)
    return resu.resultado()

#Unidad 5:

def eulerModel(funcion,xo,yo,xlim,intervalo,opcion):
    clase = euler.Euler(funcion,xo,yo,xlim,intervalo)
    if opcion ==1:
        return clase.eulerAdelante
    if opcion ==2:
        return clase.eulerAtras
    if opcion ==3:
        return clase.eulerCentrada
    if opcion ==4:
        return clase.eulerModificado

def taylorModel(funcion,xo,yo,xlim,intervalo,orden):
    clase = taylor.Taylor(funcion,xo,yo,xlim,intervalo,orden)
    return clase.taylor

def rungeModel(funcion,xo,yo,xlim,intervalo,opcion):
    clase = runge.Runge(funcion,xo,yo,xlim,intervalo)
    if opcion ==1:
        return clase.rungeDos
    if opcion ==2:
        return clase.rungeTres
    if opcion ==3:
        return clase.rungeCuatro