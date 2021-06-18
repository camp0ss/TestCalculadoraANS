import sympy as sym
import pandas as pd

class Taylor:
    #inicializa datos necesarios, funcion, valores de x,y iniciales, valor de x a llegar, valor de cuantos intervalos y el orden de la derivada
    def __init__(self,f,xo,yo,xlim,intervalo,orden):
        self.funcion = f
        self.xo = xo
        self.yo = yo
        self.x = xlim
        self.n = intervalo
        self.o = orden
    #evalua la funcion en x,y
    def evalF(tn,yn,f):
        x = sym.Symbol("x")
        y = sym.Symbol("y")
        p = sym.lambdify(x,f)
        ev = p(tn)
        p = sym.lambdify(y,ev)
        value = p(yn)
        return value
    #aplicacion del metodo de Taylor para n orden
    def taylor(self):
        f = self.funcion
        funcion = sym.parse_expr(f)
        xo = self.xo
        yo = self.yo
        xfinal = self.x
        n = self.n
        h = (xfinal-xo)/n
        orden = self.o
        x = sym.Symbol("x")
        #calculo de las derivadas de n orden, cada orden almacenada en el vector D
        D = []
        for i in range(1,orden):
            D = D+[sym.Derivative(funcion,x,i).doit()]
        #calculo de las formulas para cada orden de derivada
        yk = []
        yk.append(funcion+D[0])
        for i in range(1,len(D)):
            yk.append(yk[i-1]+D[i])
        
        tn = [xo]
        yn = [yo]
        #aplicacion del metodo,  tn es para x, yn es para y
        for i in range(0,n):
            temp = yn[i]+h*Taylor.evalF(tn[i],yn[i],funcion)
            for j in range(0,len(yk)):
                temp += ((h**(j+2))/sym.factorial(j+2))*Taylor.evalF(tn[i],yn[i],yk[j])
            yn.append(temp)
            aux = tn[i]+h
            tn.append(aux)

        t ={"tn":tn,"yn":yn}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"tabla":html,"respuesta":yn[n], "metodo":"Taylor"}
        return salida

        



