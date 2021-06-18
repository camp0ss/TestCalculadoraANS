import numpy as np
import math
import pandas as pd

np.set_printoptions(precision=3)

def Funcion(a, f, evaluador = "x"):
        av = f.evalf(subs={evaluador:a, "e" : math.e})
        #print("datos a: ",a, "funcion: ",f, "valor: ",av)
        return av

def Trapecio(limSup, limInf, func, evl):
        integral = (limSup - limInf)*(Funcion(limInf,func,evl)+Funcion(limSup,func,evl))/2
        #print(integral)
        return integral

def TrapecioCompuesto(limSup, limInf, intervalo, func, evl):
        h = (limSup-limInf)/2**intervalo

        i = list()
        Xi = list()
        fXi = list()
        i.append(0)
        xi = limInf
        Xi.append(xi)
        fXi.append(Funcion(limInf,func,evl))
        print("funcion 1: ",xi, "funcion 2: ",limSup)
        while Funcion(xi,func,evl) < Funcion(limSup,func,evl):
            num = 1
            i.append(num)
            xi = xi+h
            Xi.append(xi)
            fXi.append(Funcion(xi,func,evl))
            num+=1
            print("aver",xi)
        
        sum = 0
        for datos in range(1, len(fXi)-1):
            sum = sum + fXi[datos] 
            print("dato de suma: ", sum)
        
        d = {"Iteracion": i,"Xi": Xi,"F(Xi)": fXi}
        resu = pd.DataFrame(d)
        #print(resu)
        integral = (limSup - limInf)*(Funcion(limInf,func,evl)+2*(sum)+Funcion(limSup,func,evl))/(2**(intervalo+1))
        #print(integral)
        return integral

class Rosemberg:
    def __init__(self, liminf,limsup, nivel, func, evaluador = "x"):
        self.limInf = liminf
        self.limSup = limsup
        self.nivel = nivel
        self.func = func
        self.evl = evaluador

    def resultado(self):
        lista_de_listas = []
        lista_de_listas.append([Trapecio(self.limInf,self.limSup, self.func, self.evl)])
        level = 0
        for num in range(1, self.nivel):
            #print("n: ",num)
            lista_de_listas.append([TrapecioCompuesto(self.limInf,self.limSup, num, self.func, self.evl)])
            level+=1
        print("Datos iniciales: ",lista_de_listas)

        a = np.array(lista_de_listas)
        #print("Valores en la entrada:\n" ,a)
        contador = 0

        iteraciones = self.nivel 
        for uwu in range (self.nivel):
            iteraciones = iteraciones - 1
            listak = list ()        
            listak = a[:,uwu]
            newlevel = levelgenerator(listak,(uwu+2),iteraciones)
            a = np.append(a, newlevel, axis=1)
        data_df = pd.DataFrame(a)
        print("\n\nRespuesta:\n",data_df)
        html = data_df.to_html()
        solu = {"tabla": html, "respuesta": data_df[len(data_df)-1][0], "metodo":"Integracion por Rosemberg"}
        return solu


def calcular_h (nivelprevio, k, i):


    k = k -1
    i = i -1
    
    valorparak = (((4**k)*(nivelprevio[(i+1)]))/((4**k)-1))-(1*(nivelprevio[i])/((4**k)-1))


    return valorparak


def levelgenerator(nivelprevio,numeronivelacrear,iteraciones):
    listita = list()
    cantidad = len(nivelprevio)
    for xd in range(1, iteraciones+1):
        listita.append(calcular_h(nivelprevio,numeronivelacrear,xd))
    for xd in range(cantidad-iteraciones):
        listita.append(0)

    listafinal = []
    for i in range(cantidad):
        listafinal.append([])
        listafinal[i].append(listita[i])
    return listafinal
