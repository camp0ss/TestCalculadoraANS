import pandas as pd
from math import exp, factorial
#calculo del error para indicar cuando debe parar de evaluar
class Error:
    def errors(v):
        cifras = v
        es = 0.5*(10**(2-cifras))
        return es
#ln(e+x)
class EjercicioUno:
    #inicializa los datos a ocupar, el valor a evaluar y las cifras significativas
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    #realiza la evaluacion en la serie de taylor correspondiente
    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = 1
        #los datos iterados se guardaran en una lista
        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = 1
            for i in range(1,(n+1)):
                signo = (-1)**(i+1)
                f += signo*round((x**i)/(i*exp(i)),10)
            #se evalua que no se realice una division entre cero, sino sale del bucle
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            n +=1
            ant = f
        #los datos guardados en las listas se pasan a una tabla para generar la salida
        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida
#e^(x^2)        
class EjercicioDos:
    #inicializa los datos a ocupar, el valor a evaluar y las cifras significativas
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    #realiza la evaluacion en la serie de taylor correspondiente
    def  evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = 1
        #los datos iterados se guardaran en una lista
        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f=1
            for i in range(1,n+1):
                f += round((x**(2*i))/factorial(i),10)
            #se evalua que no se realice una division entre cero, sino sale del bucle
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            ant = f
            n +=1
        #los datos guardados en las listas se pasan a una tabla para generar la salida
        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida
#sen(x)
class EjercicioTres:
    #inicializa los datos a ocupar, el valor a evaluar y las cifras significativas
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    #realiza la evaluacion en la serie de taylor correspondiente
    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = x
        #los datos iterados se guardaran en una lista
        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = x
            for i in range(1,(n+1)):
                signo = (-1)**i
                f += signo*round((x**((2*i)+1))/factorial((2*i)+1),10)
            #se evalua que no se realice una division entre cero, sino sale del bucle
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            ant = f
            n +=1
        #los datos guardados en las listas se pasan a una tabla para generar la salida
        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida
#cos(x)
class EjercicioCuatro:
    #inicializa los datos a ocupar, el valor a evaluar y las cifras significativas
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    #realiza la evaluacion en la serie de taylor correspondiente
    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = 1
        #los datos iterados se guardaran en una lista
        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f=1
            for i in range(1,(n+1)):
                signo = (-1)**i
                f += signo*round((x**(2*i))/factorial(2*i),10)
            #se evalua que no se realice una division entre cero, sino sale del bucle
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            ant = f
            n +=1
        #los datos guardados en las listas se pasan a una tabla para generar la salida
        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida
#e^x
class EjercicioCinco:
    #inicializa los datos a ocupar, el valor a evaluar y las cifras significativas
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    #realiza la evaluacion en la serie de taylor correspondiente
    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = 1
        #los datos iterados se guardaran en una lista
        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = 1
            for i in range(1,(n+1)):
                f += round((x**i)/factorial(i),10)
            #se evalua que no se realice una division entre cero, sino sale del bucle
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            ant = f
            n += 1
        #los datos guardados en las listas se pasan a una tabla para generar la salida
        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida
#sh(x)
class EjercicioSeis:
    #inicializa los datos a ocupar, el valor a evaluar y las cifras significativas
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    #realiza la evaluacion en la serie de taylor correspondiente
    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = x
        #los datos iterados se guardaran en una lista
        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = x
            for i in range(1,(n+1)):
                f += round((x**((2*i)+1))/factorial((2*i)+1),10)
            #se evalua que no se realice una division entre cero, sino sale del bucle
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            ant = f
            n += 1
        #los datos guardados en las listas se pasan a una tabla para generar la salida
        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida
#ch(x)
class EjercicioSiete:
    #inicializa los datos a ocupar, el valor a evaluar y las cifras significativas
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    #realiza la evaluacion en la serie de taylor correspondiente
    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = 1
        #los datos iterados se guardaran en una lista
        itera = list()
        xr = list()
        err = list()
        while ea>es:
            f = 1
            for i in range(1,(n+1)):
                f += round((x**(2*i))/factorial(2*i),10)
            #se evalua que no se realice una division entre cero, sino sale del bucle
            try:
                ea = round(abs((f-ant)/f)*100,10)
            except ZeroDivisionError:
                break
            itera.append(n)
            xr.append(f)
            err.append(ea)
            ant = f
            n += 1
        #los datos guardados en las listas se pasan a una tabla para generar la salida
        t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
        tabla = pd.DataFrame(t)
        html = tabla.to_html()
        salida = {"grafica": html, "raiz": f}
        return salida
#arcsen(x)
class EjercicioOcho:
    #inicializa los datos a ocupar, el valor a evaluar y las cifras significativas
    #x debe estar entre los valores de -1 a 1, excluyendo estos valores
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    #realiza la evaluacion en la serie de taylor correspondiente
    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = x
        if x>(-1) and x<1:
            #los datos iterados se guardaran en una lista
            itera = list()
            xr = list()
            err = list()
            while ea>es:
                f = x
                for i in range(1,(1+n)):
                    f += round((factorial(2*i)/((2**i)*factorial(i))**2)*(x**(2*i+1)/(2*i+1)),10)
                #se evalua que no se realice una division entre cero, sino sale del bucle
                try:
                    ea = round(abs((f-ant)/f)*100,10)
                except ZeroDivisionError:
                    break
                itera.append(n)
                xr.append(f)
                err.append(ea)  
                ant = f
                n += 1
            #los datos guardados en las listas se pasan a una tabla para generar la salida
            t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
            tabla = pd.DataFrame(t)
            html = tabla.to_html()
            salida = {"grafica": html, "raiz": f}
            return salida
        else:
            s = "Dato a evaluar fuera del rango, se permite en el rango ]-1,1["
            salida = {"Error":s}
            return salida
#ln(1+x)
class EjercicioNueve:
    #inicializa los datos a ocupar, el valor a evaluar y las cifras significativas
    #x debe estar entre los valores de -1 a 1, excluyendo estos valores
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    #realiza la evaluacion en la serie de taylor correspondiente
    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 2
        ant = x
        if x>(-1) and x<1:
            #los datos iterados se guardaran en una lista
            itera = list()
            xr = list()
            err = list()
            while ea>es:
                f = 0
                for i in range(1,(1+n)):
                    f += round((((-1)**(i-1))/i)*(x**i),10)
                #se evalua que no se realice una division entre cero, sino sale del bucle
                try:
                    ea = round(abs((f-ant)/f)*100,10)
                except ZeroDivisionError:
                    break
                itera.append(n-1)
                xr.append(f)
                err.append(ea)  
                ant = f
                n += 1
            #los datos guardados en las listas se pasan a una tabla para generar la salida
            t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
            tabla = pd.DataFrame(t)
            html = tabla.to_html()
            salida = {"grafica": html, "raiz": f}
            return salida
        else:
            s = "Dato a evaluar fuera del rango, se permite en el rango ]-1,1["
            salida = {"Error":s}
            return salida
#1/(1+x^2)
class EjercicioDiez:
    #inicializa los datos a ocupar, el valor a evaluar y las cifras significativas
    #x debe estar entre los valores de -1 a 1, excluyendo estos valores
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    #realiza la evaluacion en la serie de taylor correspondiente
    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = 1
        if x>(-1) and x<1:
            #los datos iterados se guardaran en una lista
            itera = list()
            xr = list()
            err = list()
            while ea>es:
                f = 1
                for i in range(1,(1+n)):
                    f += round((((-1)**i)*(x**(2*i))),10)
                #se evalua que no se realice una division entre cero, sino sale del bucle
                try:
                    ea = round(abs((f-ant)/f)*100,10)
                except ZeroDivisionError:
                    break
                itera.append(n)
                xr.append(f)
                err.append(ea)  
                ant = f
                n += 1
            #los datos guardados en las listas se pasan a una tabla para generar la salida
            t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
            tabla = pd.DataFrame(t)
            html = tabla.to_html()
            salida = {"grafica": html, "raiz": f}
            return salida
        else:
            s = "Dato a evaluar fuera del rango, se permite en el rango ]-1,1["
            salida = {"Error":s}
            return salida
#arctg(x)
class EjercicioOnce:
    #inicializa los datos a ocupar, el valor a evaluar y las cifras significativas
    #x debe estar entre los valores de -1 a 1, excluyendo estos valores
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    #realiza la evaluacion en la serie de taylor correspondiente
    def evaluacion(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 1
        ant = x
        if x>(-1) and x<1:
            #los datos iterados se guardaran en una lista
            itera = list()
            xr = list()
            err = list()
            while ea>es:
                f = x
                for i in range(1,(1+n)):
                    f += round((((-1)**i)*(x**(2*i+1)))/(2*x+1),10)
                #se evalua que no se realice una division entre cero, sino sale del bucle
                try:
                    ea = round(abs((f-ant)/f)*100,10)
                except ZeroDivisionError:
                    break
                itera.append(n)
                xr.append(f)
                err.append(ea)  
                ant = f
                n += 1
            #los datos guardados en las listas se pasan a una tabla para generar la salida
            t = {"Iteracion": itera, "Valor aproximado": xr, "Error aproximado": err}
            tabla = pd.DataFrame(t)
            html = tabla.to_html()
            salida = {"grafica": html, "raiz": f}
            return salida
        else:
            s = "Dato a evaluar fuera del rango, se permite en el rango ]-1,1["
            salida = {"Error":s}
            return salida