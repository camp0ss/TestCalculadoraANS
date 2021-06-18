import math
import pandas as pd
from sympy import *

#Funcion para calcula el valor de la funcion dada en un punto especifico
def funcion(a, f, evaluador = "x"):
        av = f.evalf(subs={evaluador:a, "e" : math.e})
        #print("datos a: ",a, "funcion: ",f, "valor: ",av)
        return av


#regla del trapecio
class Trapecio:
    def __init__(self, liminf,limsup, func, evaluador = "x"):
        self.limInf = liminf
        self.limSup = limsup
        self.evl = evaluador
        self.func = func
    
    def resultado(self):
        integral = (self.limSup - self.limInf)*(funcion(self.limInf,self.func,self.evl)+funcion(self.limSup,self.func,self.evl))/2
        salida = {"integral":integral, "funcion":rcode(self.func), "metodo":"Trapecio"} #grafica
        return salida

#trapecio compuesto
class TrapecioIntervalo:
    def __init__(self, liminf,limsup, intervalo, func, evaluador = "x"):
        self.limInf = liminf
        self.limSup = limsup
        self.intervalo = intervalo
        self.func = func
        self.evl = evaluador
    
    def resultado(self):
        h = (self.limSup-self.limInf)/self.intervalo

        i = list()
        Xi = list()
        fXi = list()
        i.append(0)
        xi = self.limInf
        Xi.append(xi)
        fXi.append(funcion(self.limInf,self.func,self.evl))

        for num in range(1, self.intervalo+1):
            i.append(num)
            xi = xi+h
            Xi.append(xi)
            fXi.append(funcion(xi,self.func,self.evl))
        
        sum = 0
        for datos in range(1, len(fXi)-1):
            sum = sum + fXi[datos] #Suma de valores f(xi)
        
        d = {"Iteracion": i,"Xi": Xi,"F(Xi)": fXi}
        resu = pd.DataFrame(d)
        integral = (self.limSup - self.limInf)*(funcion(self.limInf,self.func,self.evl)+2*(sum)+funcion(self.limSup,self.func,self.evl))/(2*self.intervalo)
        html = resu.to_html() #Pasar tabla de DataFrame a etiquetas HTML
        salida = {"tabla":html,"integral":integral, "funcion":rcode(self.func), "metodo":"Trapecio Compuesto"}
        return salida

#Simpson 1/3
class SimpsonTercio:
    def __init__(self, liminf,limsup, func, evaluador = "x"):
        self.limInf = liminf
        self.limSup = limsup
        self.func = func
        self.evl = evaluador
    
    def resultado(self):
        Xm = (self.limInf+self.limSup)/2

        i = list()
        Xi = list()
        fXi = list()
        i.append(0)
        Xi.append(self.limInf)
        fXi.append(funcion(self.limInf,self.func,self.evl))
        i.append(1)
        Xi.append(Xm)
        fXi.append(funcion(Xm,self.func,self.evl))
        i.append(2)
        Xi.append(self.limSup)
        fXi.append(funcion(self.limSup,self.func,self.evl))
        
        d = {"Iteracion": i,"Xi": Xi,"F(Xi)": fXi}
        resu = pd.DataFrame(d)
        integral = (self.limSup - self.limInf)*(funcion(self.limInf,self.func,self.evl)+4*(fXi[1])+funcion(self.limSup,self.func,self.evl))/6
        html = resu.to_html() #Pasar tabla de DataFrame a etiquetas HTML
        salida = {"integral":integral, "tabla":html,"funcion":rcode(self.func), "metodo":"Simpson 1/3"} #grafica
        return salida

# Simpson 1/3 con Intervalos
class SimpTercIntervalo:
    def __init__(self, liminf,limsup,intervalo, func, evaluador = "x"):
        self.limInf = liminf
        self.limSup = limsup
        self.intervalo = intervalo
        self.func = func
        self.evl = evaluador
    
    def resultado(self):
        h = (self.limSup-self.limInf)/self.intervalo

        i = list()
        Xi = list()
        fXi = list()
        i.append(0)
        xi = self.limInf
        Xi.append(xi)
        fXi.append(funcion(self.limInf,self.func,self.evl))

        for num in range(1, self.intervalo+1):
            i.append(num)
            xi = xi+h
            Xi.append(xi)
            fXi.append(funcion(xi,self.func,self.evl))

        sum = 0
        for datos in range(1, len(fXi)-1):
            sum = sum + fXi[datos] #Suma de valores f(xi)
        
        d = {"Iteracion": i,"Xi": Xi,"F(Xi)": fXi}
        resu = pd.DataFrame(d)

        Xmi = list()
        fXmi = list()
        sum2 = 0
        for num in range(0,self.intervalo):
            xmi = (Xi[num]+Xi[num+1])/2
            Xmi.append(xmi)
            fXmi.append(funcion(xmi,self.func,self.evl))
            sum2 = sum2 + funcion(xmi,self.func,self.evl)

        d2 = {"Xmi": Xmi,"F(Xmi)": fXmi}
        resu2 = pd.DataFrame(d2)

        integral = (self.limSup - self.limInf)*(funcion(self.limInf,self.func,self.evl)+4*(sum2)+2*(sum)+funcion(self.limSup,self.func,self.evl))/(6*self.intervalo)
        html = resu.to_html()#Pasar tabla de DataFrame a etiquetas HTML
        salida = {"tabla":html,"integral":integral,"funcion":rcode(self.func), "metodo":"Simpson 1/3 compuesto"}
        return salida

#Simpson 3/8
class SimpOctavo:
    def __init__(self, liminf,limsup, func, evaluador = "x"):
        self.limInf = liminf
        self.limSup = limsup
        self.func = func
        self.evl = evaluador
    
    def resultado(self):
        h = (self.limSup-self.limInf)/3

        i = list()
        Xi = list()
        fXi = list()
        i.append(0)
        xi = self.limInf
        Xi.append(xi)
        fXi.append(funcion(self.limInf,self.func,self.evl))

        for num in range(1, 4):
            i.append(num)
            xi = xi+h
            Xi.append(xi)
            fXi.append(funcion(xi,self.func,self.evl))
        
        d = {"Iteracion": i,"Xi": Xi,"F(Xi)": fXi}
        resu = pd.DataFrame(d)

        integral = (self.limSup - self.limInf)*(fXi[0]+3*fXi[1]+3*fXi[2]+fXi[3])/8
        html = resu.to_html()#Pasar tabla de DataFrame a etiquetas HTML
        salida = {"tabla":html,"integral":integral,"funcion":rcode(self.func), "metodo":"Simpson 3/8"}
        return salida

# Simpson 3/8 con Intervalos
class SimpOctIntervalo:
    def __init__(self, liminf,limsup,intervalo, func, evaluador = "x"):
        self.limInf = liminf
        self.limSup = limsup
        self.intervalo = intervalo
        self.func = func
        self.evl = evaluador
    
    def resultado(self):
        h = (self.limSup-self.limInf)/self.intervalo

        i = list()
        Xi = list()
        fXi = list()
        i.append(0)
        xi = self.limInf
        Xi.append(xi)
        fXi.append(funcion(self.limInf,self.func,self.evl))

        for num in range(1, self.intervalo+1):
            i.append(num)
            xi = xi+h
            Xi.append(xi)
            fXi.append(funcion(xi,self.func,self.evl))

        sum = 0
        for datos in range(1, len(fXi)-1):
            sum = sum + fXi[datos] #Suma de valores f(xi)
        
        d = {"Iteracion": i,"Xi": Xi,"F(Xi)": fXi}
        resu = pd.DataFrame(d)
        print(resu)

        sub = list()
        fsub = list()
        sum2 = 0
        for num in range(0,self.intervalo):
            data = 0
            data = Xi[num]+1/3
            sub.append(data)
            ev = funcion(data, self.func,self.evl)
            sum2 = sum2 +ev
            fsub.append(ev)
            data = data + 1/3
            sub.append(data)
            ev = funcion(data, self.func,self.evl)
            fsub.append(ev)
            sum2 = sum2 +ev
            
        d2 = {"Subintervalos": sub, "F(sub)":fsub}
        resu2 = pd.DataFrame(d2)

        integral = ((self.limSup - self.limInf)/(8*self.intervalo))*(funcion(self.limInf,self.func,self.evl)+3*(sum2)+2*(sum)+funcion(self.limSup,self.func,self.evl))
        html = resu.to_html()#Pasar tabla de DataFrame a etiquetas HTML
        html2 = resu2.to_html()#Pasar tabla de DataFrame a etiquetas HTML
        salida = {"tabla":html,"tabla2":html2,"integral":integral,"funcion":rcode(self.func), "metodo":"Simpson 3/8 compuesto"}
        return salida

#Simpson 1/3 adaptativo
class SimpAdaptativo:
    def __init__(self, liminf,limsup, tolerancia, func, evaluador = "x"):
        self.limInf = liminf
        self.limSup = limsup
        self.func = func
        self.tolerancia = tolerancia
        self.evl = evaluador

    def ajuste(s1,s2,s3):
        return abs(s2+s3-s1)/15
    
    def calculo(limSup, limInf, func):
        print("")
        print("lim Sup", limSup, "lim Inf", limInf)
        h = (limSup-limInf)/2
        h += limInf
        sPrim = list()
        aver = SimpsonTercio(limInf, limSup, func)
        sPrim.append(aver.resultado()["integral"])
        aver = SimpsonTercio(limInf, h, func)
        sPrim.append(aver.resultado()["integral"])
        aver = SimpsonTercio(h, limSup, func)
        sPrim.append(aver.resultado()["integral"])
        intervalos = [limInf, h, limSup]
        ajus = SimpAdaptativo.ajuste(sPrim[0],sPrim[1],sPrim[2])
        print("ajuste: ",ajus,"intervalos: ",intervalos)
        intervalos.append(ajus)
        intervalos.append(sPrim)
        return intervalos


    def resultado(self):

        box = list()
        h = (self.limSup-self.limInf)/2
        h += self.limInf
        sPrim = list()
        aver = SimpsonTercio(self.limInf, self.limSup, self.func)
        sPrim.append(aver.resultado()["integral"])
        aver = SimpsonTercio(self.limInf, h, self.func)
        sPrim.append(aver.resultado()["integral"])
        aver = SimpsonTercio(h, self.limSup, self.func)
        sPrim.append(aver.resultado()["integral"])
        intervalos = [self.limInf, h, self.limSup]
        box.append(intervalos)
        if SimpAdaptativo.ajuste(sPrim[0],sPrim[1],sPrim[2])>self.tolerancia:

            index = 0
            total = 0
            nivel = 0
            data = list()
            for num in range(4):
                #print("Iteacion: ",num, "nivel: ",nivel)
                intervalos = SimpAdaptativo.calculo(intervalos[1+index], intervalos[0+index], self.func)
                box.append(intervalos)

                if intervalos[3]<self.tolerancia:
                    total +=1
                    print("nivel: ",nivel)
                    intervalos = box[nivel]
                    nivel-=2
                    print("estas aqui")
                    print("caja: ",box)
                    index =1
                    #data.append()
                nivel+=1
            
            sum = 0
            for num in range(1, total+1):
                sum = sum + (16*(box[-num][-1][1]+box[-num][-1][2])-box[-num][-1][0])/15
                print("")
                print(box[-num][-1])
            print(sum)
            return sum
        else:
            print(sPrim)
            sum = (16*(sPrim[1]+sPrim[2])-sPrim[0])/15
            print(sum)
            return sum



