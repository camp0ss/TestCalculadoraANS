import pandas as pd
from math import sin
from math import exp

class Biseccion:
    def __init__(self, a,b,c,d):
        self.a = a
        self.b = b
        self.funcion = c
        self.cifras = d
    
    def func(a, f):
        av = f.evalf(subs={"x":a})
        print("datos a: ",a, "funcion: ",f, "valor: ",av)
        return av

    def resultado(self):
        a = self.a
        b = self.b
        print("x1 = ", self.a ," x2 = ", self.b,"\n")
        tol = (0.5*(10**(2 - self.cifras)))
        error = 1
        X_anterior = 0
        n = 1

        #Listas
        N = list()
        Xa = list()
        Xb = list()
        Xm = list()
        Fa = list()
        Fb = list()
        Fm = list()
        E = list()
        while error > tol:
            m = (a + b) / 2
            X_actual = m
            error = abs((X_actual-X_anterior )/X_actual)*100
            N.append(n)
            Xa.append(a)
            Xb.append(b)
            Xm.append(m)
            Fa.append(Biseccion.func(a,self.funcion))
            Fb.append(Biseccion.func(b,self.funcion))
            Fm.append(Biseccion.func(m,self.funcion))
            E.append(error)
            if Biseccion.func(a,self.funcion) * Biseccion.func(m,self.funcion) < 0:
                b = m
            else:
                a = m
            X_anterior = X_actual
            n += 1

        d = {"Iteracion": N,"Xa": Xa,"Xb": Xb,"Xm": Xm,"Fa": Fa,"Fb": Fb,"Fm": Fm,"E": E}
        resu = pd.DataFrame(d)
        print(resu)
        html = resu.to_html() #pasar a tabla HTML
        print("\nRaíz es: ", m)
        salida = {"tabla":html, "raiz":m, "error":error} #grafica
        return salida
