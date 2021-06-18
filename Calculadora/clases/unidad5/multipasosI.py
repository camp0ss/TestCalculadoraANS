from pandas.io import html
import sympy as sym
import pandas as pd

class MultiPasos:
    #inicializa datos necesarios, metodo inicializador, metodo predictor, metodo corrector, funcion, valores de x,y iniciales, valor de x a llegar, valor del espaciado, niveles
    def __init__(self,mInicializador,mPredictor,mCorrector,f,xo,yo,xlim,espaciado,n):
        self.inicializador = mInicializador
        self.predictor = mPredictor
        self.corrector = mCorrector
        self.funcion = f
        self.xo = xo
        self.yo = yo
        self.x = xlim
        self.h = espaciado
        print("debig", self.h, type(self.h))
        self.n = n
        print("debig", self.n, type(self.n))
    #evalua la funcion en x,y
    def evalF(tn,yn,f):
        x = sym.Symbol("x")
        y = sym.Symbol("y")
        p = sym.lambdify(x,f)
        ev = p(tn)
        p = sym.lambdify(y,ev)
        value = p(yn)
        return value
    #aquí estan todos los metodos inicializadores, predictores y correctores
    def multipasos(self):
        f = self.funcion
        funcion = sym.parse_expr(f)
        xo = self.xo
        yo = self.yo
        xfinal = self.x
        h = self.h
        n = self.n
        indiceI = self.inicializador
        indiceP = self.predictor
        indiceC = self.corrector
        #se evalua en algun metodo inicial
        #metodo de euler modificado
        if indiceI==1:
            tn = [xo]
            yn = [yo]
            yi = ["---"]
            #aplicacion del metodo,  tn es para x, yn es para y, yi son los valores para el refinamiento del metodo
            for i in range(0,n):
                temp = yn[i]+(h*MultiPasos.evalF(tn[i],yn[i],funcion))
                yi.append(temp)
                aux = tn[i]+h
                tn.append(aux)
                temp = yn[i]+h*((MultiPasos.evalF(tn[i],yn[i],funcion)+MultiPasos.evalF(tn[i+1],yi[i+1],funcion))/2)
                yn.append(temp)
        #metodo de runge-kutta de cuarto orden
        elif indiceI==2:
            tn = [xo]
            yn = [yo]
            #aplicacion del metodo,  tn es para x, yn es para y, k1 k2 k3 son las constantes
            for i in range(0,n):
                k1 = MultiPasos.evalF(tn[i],yn[i],funcion)
                k2 = MultiPasos.evalF((tn[i]+h/2),(yn[i]+k1*(h/2)),funcion)
                k3 = MultiPasos.evalF((tn[i]+h/2),(yn[i]+k2*(h/2)),funcion)
                k4 = MultiPasos.evalF((tn[i]+h),(yn[i]+h*k3),funcion)
                yn.append(yn[i]+(h/6)*(k1+2*k2+2*k3+k4))
                tn.append(tn[i]+h)
        #se evalua en algun metodo predictor de Adams Bashforth
        #metodo de dos pasos
        if indiceP==1:
            n = len(tn)-1
            fi = list()
            for i in range(0,n):
                fi.append(MultiPasos.evalF(tn[i],yn[i],funcion))
            y2 = yn[n]+(h/2)*(3*MultiPasos.evalF(tn[n],yn[n],funcion)-MultiPasos.evalF(tn[n-1],yn[n-1],funcion))
            tn.append(tn[n-1]+h)
            fi.append(MultiPasos.evalF(tn[n],y2,funcion))
        #metodo de tres pasos
        elif indiceP==2:
            n = len(tn)-1
            fi = list()
            for i in range(0,n):
                fi.append(MultiPasos.evalF(tn[i],yn[i],funcion))
            y3 = yn[n]+(h/12)*(23*MultiPasos.evalF(tn[n],yn[n],funcion)-16*MultiPasos.evalF(tn[n-1],yn[n-1],funcion)+5*MultiPasos.evalF(tn[n-2],yn[n-2],funcion))
            tn.append(tn[n-1]+h)
            fi.append(MultiPasos.evalF(tn[n],y3,funcion))
        #metodo de cuatro pasos
        elif indiceP==3:
            n = len(tn)-1
            fi = list()
            for i in range(0,n):
                fi.append(MultiPasos.evalF(tn[i],yn[i],funcion))
            y4 = yn[n]+(h/24)*(55*MultiPasos.evalF(tn[n],yn[n],funcion)-59*MultiPasos.evalF(tn[n-1],yn[n-1],funcion)+37*MultiPasos.evalF(tn[n-2],yn[n-2],funcion)-9*MultiPasos.evalF(tn[n-3],yn[n-3],funcion))
            tn.append(tn[n-1]+h)
            fi.append(MultiPasos.evalF(tn[n],y4,funcion))
        #se evalua en algun metodo corrector de Adams Moulton
        #de un paso
        if indiceC==1:
            i = len(yn)-1
            n = len(fi)-2
            y = yn[i]+(h/2)*(fi[n+1]+fi[n])
        #de tres pasos
        if indiceC==2:
            i = len(yn)-1
            n = len(fi)-2
            y = yn[i]+(h/24)*(9*fi[n+1]+19*fi[n]-5*fi[n-1]+fi[n-2])
        #de cuatro pasos
        elif indiceC==3:
            i = len(yn)-1
            n = len(fi)-2
            y = yn[i]+(h/720)*(251*fi[n+1]+646*fi[n]-254*fi[n-1]+106*fi[n-2]-19*fi[n-3])
        
        k = len(fi)-1
        predictor = fi[k]
        j = len(tn)-1
        tn.pop(j)
        t = {"xi":tn,"yi":yn,"fi":fi}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"tabla":html,"Valor_metodo_predictor":predictor,"Valor_metodo_corrector":y, "metodo":"multipasos"}
        return salida