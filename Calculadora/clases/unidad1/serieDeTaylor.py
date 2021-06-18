import pandas as pd
from math import exp, factorial
#calculo del error para indicar cuando debe parar de evaluar
class Error:
    def errors(v):
        cifras = v
        es = 0.5*(10**(2-cifras))
        return es

class seriesTaylor:
    #inicializa los datos a ocupar, el valor a evaluar y las cifras significativas
    def __init__(self, valor, cifras):
        self.x = valor
        self.cifras = cifras
    #ln(e+x)
    #realiza la evaluacion en la serie de taylor correspondiente
    def EjercicioUno(self):
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
        salida = {"tabla": html, "raiz": f, "metodo":"ln(e+x)"}
        return salida
#e^(x^2)        
    #realiza la evaluacion en la serie de taylor correspondiente
    def  EjercicioDos(self):
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
        salida = {"tabla": html, "raiz": f, "metodo":"e^(x²)  "}
        return salida
#sen(x)
    #realiza la evaluacion en la serie de taylor correspondiente
    def EjercicioTres(self):
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
        salida = {"tabla": html, "raiz": f, "metodo":"sen(x)"}
        return salida
#cos(x)
    #realiza la evaluacion en la serie de taylor correspondiente
    def EjercicioCuatro(self):
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
        salida = {"tabla": html, "raiz": f, "metodo":"cos(x)"}
        return salida
#e^x
    #realiza la evaluacion en la serie de taylor correspondiente
    def EjercicioCinco(self):
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
        salida = {"tabla": html, "raiz": f, "metodo":"e^x"}
        return salida
#sh(x)
    #realiza la evaluacion en la serie de taylor correspondiente
    def EjercicioSeis(self):
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
        salida = {"tabla": html, "raiz": f, "metodo":"sh(x)"}
        return salida
#ch(x)
    #realiza la evaluacion en la serie de taylor correspondiente
    def EjercicioSiete(self):
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
        salida = {"tabla": html, "raiz": f, "metodo":"ch(x)"}
        return salida
#arcsen(x)
    #x debe estar entre los valores de -1 a 1, excluyendo estos valores
    #realiza la evaluacion en la serie de taylor correspondiente
    def EjercicioOcho(self):
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
        salida = {"tabla": html, "raiz": f, "metodo":"arcsen(x)"}
        return salida
#ln(1+x)
    #x debe estar entre los valores de -1 a 1, excluyendo estos valores
    #realiza la evaluacion en la serie de taylor correspondiente
    def EjercicioNueve(self):
        x = self.x
        es = Error.errors(self.cifras)
        ea = es+1
        n = 2
        ant = x
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
        salida = {"tabla": html, "raiz": f, "metodo":"ln(1+x)"}
        return salida
#1/(1+x^2)
    #x debe estar entre los valores de -1 a 1, excluyendo estos valores
    #realiza la evaluacion en la serie de taylor correspondiente
    def EjercicioDiez(self):
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
        salida = {"tabla": html, "raiz": f, "metodo":"1/(1+x^2)"}
        return salida
#arctg(x)
    #inicializa los datos a ocupar, el valor a evaluar y las cifras significativas
    #x debe estar entre los valores de -1 a 1, excluyendo estos valores
    #realiza la evaluacion en la serie de taylor correspondiente
    def EjercicioOnce(self):
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
        salida = {"tabla": html, "raiz": f, "metodo":"arctg(x)"}
        return salida