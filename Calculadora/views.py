from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from .models import biseccionModel, falsaModel, hermiteModel, mullerModel, newtonModel, puntoModel, secanteModel, taylorModel
from .models import lagran, divididasModel, polNewtonModel,hermiteModel
from .models import diferenciacionModel, trapecioModel, trapecioCompuestoModel, simpsonTercioModel, simpsonTercioCompuestoModel, simpsonOctavoModel, simpsonOctavoCompuestoModel, simpsonTercioAdaptativoModel, richardsonModel, rosembergModel
from .models import eulerModel, taylorModel, rungeModel, seriesTaylorModel, multipasosModel
import pandas as pd
from math import pi
from sympy import simplify, separatevars
from sympy.parsing.sympy_parser import parse_expr

#Vistas:
'''
#404: página no encontrada
def pag_404_not_found(request, exception=None):
    return HttpResponse('Error handler content', status=403)
 
#500: error en el servidor
def pag_500_error_server(request, exception=None):
    return HttpResponse('Error handler content', status=403)
'''
def pagina1(request):
    return render(request, "unidad1/taylor.html")

#unidad 2:
def biseccion(request):
    return render(request, "unidad2/biseccion.html")

def falsa(request):
    return render(request, "unidad2/falsa.html")

def punto(request):
    return render(request, "unidad2/punto.html")

def secante(request):
    return render(request, "unidad2/secante.html")

def newton(request):
    return render(request, "unidad2/newton.html")

def muller(request):
    return render(request, "unidad2/muller.html")
#unidad 3:
def diffDivididas(request):
    return render(request, "unidad3/diffDivididas.html")

def hermite(request):
    return render(request, "unidad3/hermite.html")

def lagrange(request):
    return render(request, "unidad3/lagrangev2.html")

def polNewton(request):
    return render(request, "unidad3/polNewton.html")

#unidad 4:
def derivacion(request):
    return render(request, "unidad4/diferenciacion.html")

def integracion(request):
    return render(request, "unidad4/integracion.html")

def richardson(request):
    return render(request, "unidad4/richardson.html")

def rosemberg(request):
    return render(request, "unidad4/rosemberg.html")

#unidad 5:
def multipasos(request):
    return render(request, "unidad5/multipasos.html")

def euler(request):
    return render(request, "unidad5/euler.html")

def runge(request):
    return render(request, "unidad5/runge.html")

def taylor(request):
    return render(request, "unidad5/taylor.html")

#Vista donde se extraen y se envian datos
def solve(request):
    
    #Unidad 1:
    if request.GET["tipo"] == "seriesTaylorModel":
        valorX = float(parse_expr(request.GET["valorX"]))
        cifras = float(parse_expr(request.GET["cifras"]))
        opcion = int(request.GET["opcion"])
        
        av = seriesTaylorModel(valorX,cifras, opcion) 

    #Unidad 2:
    elif request.GET["tipo"] == "biseccion":
        func = parse_expr(request.GET["funcion"])
        valorI = float(parse_expr(request.GET["valorI"]))
        valorF = float(parse_expr(request.GET["valorF"]))
        
        av = biseccionModel(valorI,valorF, func, float(request.GET["cifras"])) 

    elif request.GET["tipo"] == "falsa":
        func = parse_expr(request.GET["funcion"])
        valorI = float(parse_expr(request.GET["valorI"]))
        valorF = float(parse_expr(request.GET["valorF"]))

        av = falsaModel(func,valorI,valorF,float(request.GET["cifras"]))

    elif request.GET["tipo"] == "newton":
        func = parse_expr(request.GET["funcion"])
        intervalo = float(parse_expr(request.GET["intervalo"]))

        av = newtonModel(func,intervalo,float(request.GET["cifras"]))

    #revisar
    elif request.GET["tipo"] == "punto":
        func = parse_expr(request.GET["funcion"])
        intervalo = float(parse_expr(request.GET["intervalo"]))

        av = puntoModel(func,intervalo,float(request.GET["cifras"])) 

    elif request.GET["tipo"] == "secante":
        func = parse_expr(request.GET["funcion"])
        valorI = float(parse_expr(request.GET["valorI"]))
        valorF = float(parse_expr(request.GET["valorF"]))

        av = secanteModel(func,valorI,valorF,float(request.GET["cifras"]))

    elif request.GET["tipo"] == "muller":
        func = parse_expr(request.GET["funcion"])
        lista = list()
        lista.append(float(parse_expr(request.GET["valor1"])))
        lista.append(float(parse_expr(request.GET["valor2"])))
        lista.append(float(parse_expr(request.GET["valor3"])))

        av = mullerModel(func,float(request.GET["cifras"]),lista)
         
    #Unidad 3:
    elif request.GET["tipo"] == "lagrange":
        if int(request.GET["opcion"]) == 1:
            func = parse_expr(request.GET["funcion"])
            lista1 = list()
            cols= int(request.GET["cols1"])
            for col in range(0,cols):
                lista1.append(float(request.GET["0_"+str(col)]))

            av = lagran(lista1,float(request.GET["puntoEvaluar"]),1,1,func) 
            data = {
                        "funcion":request.GET["funcion"],
                        "tipo":request.GET["tipo"],
                        "av": av,}
            return render(request, "resolverU3.html", data)

        elif int(request.GET["opcion"]) == 2:
            lista1 = list()
            lista2 = list()

            cols= int(request.GET["cols"])
            for col in range(0,cols):
                lista1.append(float(parse_expr(request.GET["0_"+str(col)])))

            for col in range(0,cols):
                lista2.append(float(parse_expr(request.GET["1_"+str(col)])))
            av = lagran(lista1, float(request.GET["puntoEvaluar"]),2, lista2) 
            data = {
                        "funcion":request.GET["funcion"],
                        "tipo":request.GET["tipo"],
                        "av": av,}
            return render(request, "resolverU3.html", data)

    elif request.GET["tipo"] == "diffDivididas":
        if int(request.GET["opcion"]) == 1:
            func = parse_expr(request.GET["funcion"])
            lista1 = list()
            lista2=list()
            cols= int(request.GET["cols1"])
            for col in range(0,cols):
                lista1.append(float(request.GET["0_"+str(col)]))

            av = divididasModel(lista1, float(request.GET["puntoEvaluar"]),lista2,func) 
            data = {
                        "funcion":request.GET["funcion"],
                        "tipo":request.GET["tipo"],
                        "av": av,}
            return render(request, "resolverU3.html", data)

        elif int(request.GET["opcion"]) == 2:
            lista1 = list()
            lista2 = list()

            cols= int(request.GET["cols"])
            for col in range(0,cols):
                lista1.append(float(parse_expr(request.GET["0_"+str(col)])))

            for col in range(0,cols):
                lista2.append(float(parse_expr(request.GET["1_"+str(col)])))
            av = divididasModel(lista1, float(request.GET["puntoEvaluar"]),lista2) 
            data = {
                        "funcion":request.GET["funcion"],
                        "tipo":request.GET["tipo"],
                        "av": av,}
            return render(request, "resolverU3.html", data)

    elif request.GET["tipo"] == "polNewton":
        if int(request.GET["opcion"]) == 1:
            func = parse_expr(request.GET["funcion"])
            lista1 = list()
            lista2=list()
            cols= int(request.GET["cols1"])
            for col in range(0,cols):
                lista1.append(float(request.GET["0_"+str(col)]))

            av = polNewtonModel(lista1, float(request.GET["puntoEvaluar"]),lista2,func) 
            data = {
                        "funcion":request.GET["funcion"],
                        "tipo":request.GET["tipo"],
                        "av": av,}
            return render(request, "resolverU3.html", data)

        elif int(request.GET["opcion"]) == 2:
            lista1 = list()
            lista2 = list()

            cols= int(request.GET["cols"])
            for col in range(0,cols):
                lista1.append(float(parse_expr(request.GET["0_"+str(col)])))

            for col in range(0,cols):
                lista2.append(float(parse_expr(request.GET["1_"+str(col)])))
            av = polNewtonModel(lista1, float(request.GET["puntoEvaluar"]),lista2) 
            data = {
                        "funcion":request.GET["funcion"],
                        "tipo":request.GET["tipo"],
                        "av": av,}
            return render(request, "resolverU3.html", data)

    elif request.GET["tipo"] == "hermite":
        cols= int(request.GET["cols"])
        rows= int(request.GET["rows"])
        matriz = list()
        for col in range(0,cols):
            matriz.append([float(parse_expr(request.GET["0_"+str(col)]))])
        for col in range(0,cols):
            for row in range(1,rows):
                aver = matriz[col]
                aver.append(float(parse_expr(request.GET[str(row)+"_"+str(col)])))
        av = hermiteModel(float(parse_expr(request.GET["punto"])), matriz)

    #Unidad 4:
    elif request.GET["tipo"] == "diferenciacion":
        valorH = float(parse_expr(request.GET["valorH"]))
        valorX = float(parse_expr(request.GET["valorX"]))
        func = parse_expr(request.GET["funcion"])
        opcion = int(request.GET["opcion"])
        av = diferenciacionModel(func, valorH, valorX, opcion)

    elif request.GET["tipo"] == "integracion":
        limInf = float(parse_expr(request.GET["limInf"]))
        limSup = float(parse_expr(request.GET["limSup"]))
        func = parse_expr(request.GET["funcion"])
        opcion = int(request.GET["opcion"])
        if opcion == 1:
            av = trapecioModel(limInf, limSup, func)
        elif opcion == 2:
            intervalos = int(request.GET["intervalos"])
            av = trapecioCompuestoModel(limInf, limSup, intervalos, func)
        elif opcion == 3:
            av = simpsonTercioModel(limInf, limSup, func)
        elif opcion == 4:
            intervalos = int(request.GET["intervalos"])
            av = simpsonTercioCompuestoModel(limInf, limSup, intervalos, func)
        elif opcion == 5:
            av = simpsonOctavoModel(limInf, limSup, func)
        elif opcion == 6:
            intervalos = int(request.GET["intervalos"])
            av = simpsonOctavoCompuestoModel(limInf, limSup, intervalos, func)
        elif opcion == 7:
            intervalos = int(request.GET["intervalos"])
            av = simpsonTercioAdaptativoModel(limInf, limSup, intervalos, func)

    elif request.GET["tipo"] == "richardson":
        func = parse_expr(request.GET["funcion"])
        valorH = float(parse_expr(request.GET["valorH"]))
        valorX = float(parse_expr(request.GET["valorX"]))
        metodo = int(request.GET["opcion"])
        nivel = int(request.GET["nivel"])
        av = richardsonModel(func, valorH, valorX, metodo, nivel)
    
    elif request.GET["tipo"] == "rosemberg":
        func = parse_expr(request.GET["funcion"])
        limInf = float(parse_expr(request.GET["limInf"]))
        limSup = float(parse_expr(request.GET["limSup"]))
        nivel = int(request.GET["nivel"])
        av = rosembergModel(limInf, limSup, nivel, func)


    #Unidad 5:
    elif request.GET["tipo"] == "euler":
        func = str(request.GET["funcion"])
        xInicial = float(parse_expr(request.GET["xInicial"]))
        yInicial = float(parse_expr(request.GET["yInicial"]))
        valorH = int(parse_expr(request.GET["valorH"]))
        punto = float(parse_expr(request.GET["punto"]))
        opcion = int((request.GET["opcion"]))

        av = eulerModel(func, xInicial, yInicial, punto, valorH, opcion)

    elif request.GET["tipo"] == "taylor":
        func = str(request.GET["funcion"])
        xInicial = float(parse_expr(request.GET["xInicial"]))
        yInicial = float(parse_expr(request.GET["yInicial"]))
        valorH = int(parse_expr(request.GET["valorH"]))
        punto = float(parse_expr(request.GET["punto"]))
        orden = int((request.GET["orden"]))

        av = taylorModel(func, xInicial, yInicial, punto, valorH, orden)

    elif request.GET["tipo"] == "runge":
        func = str(request.GET["funcion"])
        xInicial = float(parse_expr(request.GET["xInicial"]))
        yInicial = float(parse_expr(request.GET["yInicial"]))
        intervalo = int(parse_expr(request.GET["valorH"]))
        punto = float(parse_expr(request.GET["punto"]))
        opcion = int((request.GET["opcion"]))

        av = rungeModel(func, xInicial, yInicial, punto, intervalo, opcion)

    elif request.GET["tipo"] == "multipasos":
        func = str(request.GET["funcion"])
        xInicial = float(parse_expr(request.GET["xInicial"]))
        yInicial = float(parse_expr(request.GET["yInicial"]))
        intervalo = float(parse_expr(request.GET["valorh"]))
        punto = float(parse_expr(request.GET["punto"]))
        nivel = int(parse_expr(request.GET["nivel"]))
        inicializador = int((request.GET["inicializador"]))
        predictor = int((request.GET["predictor"]))
        corrector = int((request.GET["corrector"]))

        av = multipasosModel(inicializador,predictor,corrector,func, xInicial, yInicial, punto, intervalo,nivel)

    data = {"av": av,}
    return render(request, "resolver.html", data)

    