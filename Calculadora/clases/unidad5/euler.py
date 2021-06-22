import sympy as sym
import pandas as pd
#metodo de euler para EDO de primer grado
class Euler:
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
    #metodo de euler hacia adelante
    def eulerAdelante(self):
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
                #aplicacion del metodo,  tn es para x, yn es para y
                for i in range(0,n):
                    temp = yn[i]+(h*Euler.evalF(tn[i],yn[i],funcion))
                    yn.append(temp)
                    aux = tn[i]+h
                    tn.append(aux)
    
                t ={"tn":tn,"yn":yn}
                tabla = pd.DataFrame(t)
                html = tabla.to_html()
                salida = {"Tabla":html,"Resultado":yn[n],"metodo":"Euler hacia adelante"}
                return salida
            else:
                error = "El valor de intervalo tiene que ser un entero"
                salida = {"Error:":error}
                return salida
        else:
            error = "Datos introducidos de manera erronea"
            salida = {"Error:":error}
            return salida
    #metodo de euler hacia atras
    def eulerAtras(self):
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
                yi = ["---"]
                #aplicacion del metodo, yi es el valor que estará implicito para la funcion, tn es para x, yn es para y
                for i in range(0,n):
                    temp = yn[i]+(h*Euler.evalF(tn[i],yn[i],funcion))
                    aux = tn[i]+h
                    tn.append(aux)
                    yi.append(temp)
                    temp = yn[i]+(h*Euler.evalF(tn[i+1],yi[i+1],funcion))
                    yn.append(temp)
                
                t ={"tn":tn,"yi":yi,"yn":yn}
                tabla = pd.DataFrame(t)
                html = tabla.to_html()
                salida = {"Tabla":html,"Resultado":yn[n],"metodo":"Euler hacia atras"}
                return salida
            else:
                error = "El valor de intervalo tiene que ser un entero"
                salida = {"Error:":error}
                return salida
        else:
            error = "Datos introducidos de manera erronea"
            salida = {"Error:":error}
            return salida
    #metodo de euler centrada
    def eulerCentrada(self):
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
                #aplicacion del metodo,  tn es para x, yn es para y
                for i in range(0,n):
                    temp = yn[i]+(h*Euler.evalF(tn[i],yn[i],funcion))
                    yn.append(temp)
                    aux = tn[i]+h
                    tn.append(aux)
    
                t ={"tn":tn,"yn":yn}
                tabla = pd.DataFrame(t)
                html = tabla.to_html()
                salida = {"Tabla":html,"Resultado":yn[n],"metodo":"Euler centrado"}
                return salida
            else:
                error = "El valor de intervalo tiene que ser un entero"
                salida = {"Error:":error}
                return salida
        else:
            error = "Datos introducidos de manera erronea"
            salida = {"Error:":error}
            return salida
    #metodo de euler modificado
    def eulerModificado(self):
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
                yi = ["---"]
                #aplicacion del metodo,  tn es para x, yn es para y, yi son los valores para el refinamiento del metodo
                for i in range(0,n):
                    temp = yn[i]+(h*Euler.evalF(tn[i],yn[i],funcion))
                    yi.append(temp)
                    aux = tn[i]+h
                    tn.append(aux)
                    temp = yn[i]+h*((Euler.evalF(tn[i],yn[i],funcion)+Euler.evalF(tn[i+1],yi[i+1],funcion))/2)
                    yn.append(temp)
    
                t ={"tn":tn,"yn":yn}
                tabla = pd.DataFrame(t)
                html = tabla.to_html()
                salida = {"Tabla":html,"Resultado":yn[n],"metodo":"Euler modificado"}
                return salida
            else:
                error = "El valor de intervalo tiene que ser un entero"
                salida = {"Error:":error}
                return salida
        else:
            error = "Datos introducidos de manera erronea"
            salida = {"Error:":error}
            return salida