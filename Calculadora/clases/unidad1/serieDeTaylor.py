import pandas as pd
from math import exp, factorial

class Error:
    def errors(v):
        cifras = v
        es = 0.5*(10**(2-cifras))
        return es

class EjercicioUno:
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    
    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = 1

        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = 1
            for i in range(1,(n+1)):
                signo = (-1)**(i+1)
                f += signo*round((x**i)/(i*exp(i)),10)
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            n +=1
            ant = f
        
        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida
        
class EjercicioDos:
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    
    def  evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = 1

        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f=1
            for i in range(1,n+1):
                f += round((x**(2*i))/factorial(i),10)
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            ant = f
            n +=1
        
        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida

class EjercicioTres:
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras

    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = x

        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = x
            for i in range(1,(n+1)):
                signo = (-1)**i
                f += signo*round((x**((2*i)+1))/factorial((2*i)+1),10)
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            ant = f
            n +=1

        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida

class EjercicioCuatro:
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras

    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = 1

        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f=1
            for i in range(1,(n+1)):
                signo = (-1)**i
                f += signo*round((x**(2*i))/factorial(2*i),10)
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            ant = f
            n +=1
        
        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida

class EjercicioCinco:
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    
    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = 1

        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = 1
            for i in range(1,(n+1)):
                f += round((x**i)/factorial(i),10)
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            ant = f
            n += 1

        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida

class EjercicioSeis:
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras

    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = x

        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = x
            for i in range(1,(n+1)):
                f += round((x**((2*i)+1))/factorial((2*i)+1),10)
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            ant = f
            n += 1

        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida

class EjercicioSiete:
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras

    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = 1

        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = 1
            for i in range(1,(n+1)):
                f += round((x**(2*i))/factorial(2*i),10)
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            ant = f
            n += 1

        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida

class EjercicioOcho:
    #x debe estar entre los valores de -1 a 1, excluyendo estos valores
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras

    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = x

        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = x
            for i in range(1,(1+n)):
                f += round((factorial(2*i)/((2**i)*factorial(i))**2)*(x**(2*i+1)/(2*i+1)),10)
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)  
            ant = f
            n += 1

        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida

class EjercicioNueve:
    #x debe estar entre los valores de -1 a 1, excluyendo estos valores
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras

    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 2
        ant = x

        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = 0
            for i in range(1,(1+n)):
                f += round((((-1)**(i-1))/i)*(x**i),10)
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n-1)
            xr.append(f)
            err.append(ea)  
            ant = f
            n += 1

        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida

class EjercicioDiez:
    #x debe estar entre los valores de -1 a 1, excluyendo estos valores
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras

    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = 1

        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = 1
            for i in range(1,(1+n)):
                f += round((((-1)**i)*(x**(2*i))),10)
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)  
            ant = f
            n += 1

        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida

class EjercicioOnce:
    #x debe estar entre los valores de -1 a 1, excluyendo estos valores
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras

    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = x

        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = x
            for i in range(1,(1+n)):
                f += round((((-1)**i)*(x**(2*i+1)))/(2*x+1),10)
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)  
            ant = f
            n += 1

        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida