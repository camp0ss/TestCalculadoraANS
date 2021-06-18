import sympy as sym
import pandas as pd
#ocupare para multipasos solo los métodos de euler modificado y runge-kutta de cuarto orden ya que son los mas precisos
#se recomienda que las variables que contengan la ecuacion y el espaciado mantenerlas guardadas sin cambios ya que se solicita en cada metodo
#clase para el metodo de euler modificado
class MEuler:
    #inicializa datos necesarios, funcion, valores de x,y iniciales, valor de x a llegar, valor del espaciado, niveles
    def __init__(self,f,xo,yo,xlim,espaciado,n):
        self.funcion = f
        self.xo = xo
        self.yo = yo
        self.x = xlim
        self.h = espaciado
        self.n = n
    #evalua la funcion en x,y
    def evalF(tn,yn,f):
        x = sym.Symbol("x")
        y = sym.Symbol("y")
        p = sym.lambdify(x,f)
        ev = p(tn)
        p = sym.lambdify(y,ev)
        value = p(yn)
        return value
    #metodo de euler modificado
    def eulerModificado(self):
        f = self.funcion
        funcion = sym.parse_expr(f)
        xo = self.xo
        yo = self.yo
        xfinal = self.x
        h = self.h
        n = self.n

        tn = [xo]
        yn = [yo]
        yi = ["---"]
        #aplicacion del metodo,  tn es para x, yn es para y, yi son los valores para el refinamiento del metodo
        for i in range(0,n):
            temp = yn[i]+(h*MEuler.evalF(tn[i],yn[i],funcion))
            yi.append(temp)
            aux = tn[i]+h
            tn.append(aux)
            temp = yn[i]+h*((MEuler.evalF(tn[i],yn[i],funcion)+MEuler.evalF(tn[i+1],yi[i+1],funcion))/2)
            yn.append(temp)
        #retorna las listas con los valores iniciales para x y, se recomienda guardar el retorno en variables aparte porque se ocupan despues
        return [tn,yn]
#clase para runge-kutta de orden cuatro
class MRunge:
    #inicializa datos necesarios, funcion, valores de x,y iniciales, valor de x a llegar, valor del espaciado, niveles
    def __init__(self,f,xo,yo,xlim,espaciado,n):
        self.funcion = f
        self.xo = xo
        self.yo = yo
        self.x = xlim
        self.h = espaciado
        self.n = n
    #evalua la funcion en x,y
    def evalF(tn,yn,f):
        x = sym.Symbol("x")
        y = sym.Symbol("y")
        p = sym.lambdify(x,f)
        ev = p(tn)
        p = sym.lambdify(y,ev)
        value = p(yn)
        return value
    #metodo de runge-kutta de cuarto orden
    def rungeCuatro(self):
        f = self.funcion
        funcion = sym.parse_expr(f)
        xo = self.xo
        yo = self.yo
        xfinal = self.x
        h = self.h
        n = self.n

        tn = [xo]
        yn = [yo]
        #aplicacion del metodo,  tn es para x, yn es para y, k1 k2 k3 son las constantes
        for i in range(0,n):
            k1 = MRunge.evalF(tn[i],yn[i],funcion)
            k2 = MRunge.evalF((tn[i]+h/2),(yn[i]+k1*(h/2)),funcion)
            k3 = MRunge.evalF((tn[i]+h/2),(yn[i]+k2*(h/2)),funcion)
            k4 = MRunge.evalF((tn[i]+h),(yn[i]+h*k3),funcion)
            yn.append(yn[i]+(h/6)*(k1+2*k2+2*k3+k4))
            tn.append(tn[i]+h)
        #retorna las listas con los valores iniciales para x y, se recomienda guardar el retorno en variables aparte porque se ocupan despues
        return [tn,yn]
#clase para los metodos multipasos predictores
class AdamsBashforth:
    #inicializa los datos necesarios, la lista para los valores de x, la lista para los valores de y, la funcion, espaciado
    def __init__(self,x,y,funcion,espaciado):
        self.funcion = funcion
        self.xi = x
        self.yi = y
        self.h = espaciado
    #evalua la funcion en x,y
    def evalF(tn,yn,f):
        x = sym.Symbol("x")
        y = sym.Symbol("y")
        p = sym.lambdify(x,f)
        ev = p(tn)
        p = sym.lambdify(y,ev)
        value = p(yn)
        return value
    #metodo de adams-barshforth de dos pasos
    def dosPasos(self):
        xi = self.xi
        yi = self.yi
        f = self.funcion
        h = self.h
        funcion = sym.parse_expr(f)
        n = len(xi)-1
        fi = list()
        for i in range(0,n):
            fi.append(AdamsBashforth.evalF(xi[i],yi[i],funcion))
        y2 = yi[n]+(h/2)*(3*AdamsBashforth.evalF(xi[n],yi[n],funcion)-AdamsBashforth.evalF(xi[n-1],yi[n-1],funcion))
        xi.append(xi[n]+h)
        fi.append(AdamsBashforth.evalF(xi[n],y2,funcion))
        #retorno la lista con los valores de la funcion en cada par ordenado antes calculado
        return fi
    #metodo de adams-barshforth de tres pasos
    def tresPasos(self):
        xi = self.xi
        yi = self.yi
        f = self.funcion
        h = self.h
        funcion = sym.parse_expr(f)
        n = len(xi)-1
        fi = list()
        for i in range(0,n):
            fi.append(AdamsBashforth.evalF(xi[i],yi[i],funcion))
        y3 = yi[n]+(h/12)*(23*AdamsBashforth.evalF(xi[n],yi[n],funcion)-16*AdamsBashforth.evalF(xi[n-1],yi[n-1],funcion)+5*AdamsBashforth.evalF(xi[n-2],yi[n-2],funcion))
        xi.append(xi[n]+h)
        fi.append(AdamsBashforth.evalF(xi[n],y3,funcion))
        #retorno la lista con los valores de la funcion en cada par ordenado antes calculado
        return fi
    #metodo de adams-barshforth de cuatro pasos
    def cuatroPasos(self):
        xi = self.xi
        yi = self.yi
        f = self.funcion
        h = self.h
        funcion = sym.parse_expr(f)
        n = len(xi)-1
        fi = list()
        for i in range(0,n):
            fi.append(AdamsBashforth.evalF(xi[i],yi[i],funcion))
        y4 = yi[n]+(h/24)*(55*AdamsBashforth.evalF(xi[n],yi[n],funcion)-59*AdamsBashforth.evalF(xi[n-1],yi[n-1],funcion)+37*AdamsBashforth.evalF(xi[n-2],yi[n-2],funcion)-9*AdamsBashforth.evalF(xi[n-3],yi[n-3],funcion))
        xi.append(xi[n]+h)
        fi.append(AdamsBashforth.evalF(xi[n],y4,funcion))
        #retorno la lista con los valores de la funcion en cada par ordenado antes calculado
        return fi
#clase para los metodos multipasos correctores
class AdamsMoulton:
    #inicializa los datos necesarios, la lista de los valores de las evaluaciones que retorna del metodo predictor, la lista para los valores de y, la funcion, espaciado
    def __init__(self,fi,y,espaciado):
        self.fi = fi
        self.h = espaciado
        self.y = y
    #metodo de adams-moulton de un paso
    def unPaso(self):
        h = self.h
        fi = self.fi
        y = self.y
        i = len(y)-1
        n = len(fi)-2
        y1 = y[i]+(h/2)*(fi[n+1]+fi[n])
        return y1
    #metodo de adams-moulton de tres pasos
    def tresPaso(self):
        h = self.h
        fi = self.fi
        y = self.y
        i = len(y)-1
        n = len(fi)-2
        y3 = y[i]+(h/24)*(9*fi[n+1]+19*fi[n]-5*fi[n-1]+fi[n-2])
        return y3
    #metodo de adams-moulton de cuatro pasos
    def cuatroPaso(self):
        h = self.h
        fi = self.fi
        y = self.y
        i = len(y)-1
        n = len(fi)-2
        y4 = y[i]+(h/720)*(251*fi[n+1]+646*fi[n]-254*fi[n-1]+106*fi[n-2]-19*fi[n-3])
        return y4

