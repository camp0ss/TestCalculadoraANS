import sympy as sym
import pandas as pd

class Runge:
    #inicializa datos necesarios, funcion, valores de x,y iniciales, valor de x a llegar, valor de cuantos intervalos
    def __init__(self,f,xo,yo,xlim,intervalo):
        self.funcion = f
        self.xo = xo
        self.yo = yo
        self.x = xlim
        self.n = intervalo
    #evalua la funcion en x,y
    def evalF(tn,yn,f):
        x = sym.Symbol("x")
        y = sym.Symbol("y")
        p = sym.lambdify(x,f)
        ev = p(tn)
        p = sym.lambdify(y,ev)
        value = p(yn)
        return value
    #metodo de runge-kutta de segundo orden
    def rungeDos(self):
        f = self.funcion
        funcion = sym.parse_expr(f)
        xo = self.xo
        yo = self.yo
        xfinal = self.x
        n = self.n
        if n>0 and xo<xfinal:
            if type(n)==int:
                h = (xfinal-xo)/n

                tn = [xo]
                yn = [yo]
                #aplicacion del metodo,  tn es para x, yn es para y, k1 k2 son las constantes
                for i in range(0,n):
                    k1 = Runge.evalF(tn[i],yn[i],funcion)
                    k2 = Runge.evalF((tn[i]+h),(yn[i]+k1*h),funcion)
                    yn.append(yn[i]+(1/2)*h*(k1+k2))
                    tn.append(tn[i]+h)
        
                t ={"tn":tn,"yn":yn}
                tabla = pd.DataFrame(t)
                html = tabla.to_html()
                salida = {"tabla":html,"respuesta":yn[n],"metodo":"Runge-kutta de segundo orden"}
                return salida
            else:
                error = "El valor de intervalo tiene que ser un entero"
                salida = {"Error":error,"metodo":"Runge-kutta de segundo orden"}
                return salida
        else:
            error = "Datos introducidos de manera erronea"
            salida = {"Error":error,"metodo":"Runge-kutta de segundo orden"}
            return salida
    #metodo de runge-kutta de tercer orden
    def rungeTres(self):
        f = self.funcion
        funcion = sym.parse_expr(f)
        xo = self.xo
        yo = self.yo
        xfinal = self.x
        n = self.n
        if n>0 and xo<xfinal:
            if type(n)==int:
                h = (xfinal-xo)/n

                tn = [xo]
                yn = [yo]
                #aplicacion del metodo,  tn es para x, yn es para y, k1 k2 k3 son las constantes
                for i in range(0,n):
                    k1 = Runge.evalF(tn[i],yn[i],funcion)
                    k2 = Runge.evalF((tn[i]+h/2),(yn[i]+k1*(h/2)),funcion)
                    k3 = Runge.evalF((tn[i]+h),(yn[i]-k1*h+2*k2*h),funcion)
                    yn.append(yn[i]+(h/6)*(k1+4*k2+k3))
                    tn.append(tn[i]+h)
        
                t ={"tn":tn,"yn":yn}
                tabla = pd.DataFrame(t)
                html = tabla.to_html()
                salida = {"tabla":html,"respuesta":yn[n],"metodo":"Runge-kutta de tercer orden"}
                return salida
            else:
                error = "El valor de intervalo tiene que ser un entero"
                salida = {"Error":error,"metodo":"Runge-kutta de tercer orden"}
                return salida
        else:
            error = "Datos introducidos de manera erronea"
            salida = {"Error":error,"metodo":"Runge-kutta de tercer orden"}
            return salida
    #metodo de runge-kutta de cuarto orden
    def rungeCuatro(self):
        f = self.funcion
        funcion = sym.parse_expr(f)
        xo = self.xo
        yo = self.yo
        xfinal = self.x
        n = self.n
        if n>0 and xo<xfinal:
            if type(n)==int:
                h = (xfinal-xo)/n

                tn = [xo]
                yn = [yo]
                #aplicacion del metodo,  tn es para x, yn es para y, k1 k2 k3 son las constantes
                for i in range(0,n):
                    k1 = Runge.evalF(tn[i],yn[i],funcion)
                    k2 = Runge.evalF((tn[i]+h/2),(yn[i]+k1*(h/2)),funcion)
                    k3 = Runge.evalF((tn[i]+h/2),(yn[i]+k2*(h/2)),funcion)
                    k4 = Runge.evalF((tn[i]+h),(yn[i]+h*k3),funcion)
                    yn.append(yn[i]+(h/6)*(k1+2*k2+2*k3+k4))
                    tn.append(tn[i]+h)
        
                t ={"tn":tn,"yn":yn}
                tabla = pd.DataFrame(t)
                html = tabla.to_html()
                salida = {"tabla":html,"respuesta":yn[n],"metodo":"Runge-kutta de cuarto orden"}
                return salida
            else:
                error = "El valor de intervalo tiene que ser un entero"
                salida = {"Error":error,"metodo":"Runge-kutta de cuarto orden"}
                return salida
        else:
            error = "Datos introducidos de manera erronea"
            salida = {"Error":error,"metodo":"Runge-kutta de cuarto orden"}
            return salida