from sympy import *
import math
import sympy as sym

class Newton_recursivo:
    def __init__(self,tx,ty,p, f = sympify("x")):
        #f = funcion
        #tx = lista con valores de x
        #ty = lista con valores de y
        #p = valor de x que se busca en la funcion
        self.tablax = tx
        self.tablay = ty
        self.punto = p
        self.funcion = f
    
    #esta funcion factorial se usa para el calculo del error teorico.
    def factorial(n):
        if n<=1:
            return 1 
        return n*factorial(n-1) 

    def resultado(self):

        x, y, z = symbols('x y z')
        xn = self.punto
        convertido2 = self.funcion
        valor_real = convertido2.subs(x, xn)
        
        yi = self.tablay #esta variable contiene la entrada de la funcion, vector con los datos de y
        xi = self.tablax #esta variable contiene el vector con los datos de x
        grado = (len(xi)-1) #determina el grado de la interpolacion, 
        fi = list() # esta lista contiene los datos que usa la funcion.

        ''' evaluando si se  '''

        '''evaluando si se proporcio un vector con los valores de y, si no es asi, se generan en base
        a la funcion y los valores de x'''

        if len(yi) == 0:
            #generando valores de fx
            for uwu in xi:
                temp = convertido2.subs(x, uwu)
                fi.append(temp)
        else:
            fi = yi #se nos dio una tabla con valores de y, pasamos la entrada a fi

        #codigo para derivar, esto se usa en el error teorico.
        deri = diff(convertido2,x,len(xi))
        deri.expand()
        derivada = deri.subs(x, xn)

        '''
        print("X = ", xi)
        print("Fx = ", fi)
        '''

        bi = []
        bi.append(fi[0])
        for i in range(1,(grado+1)):
            if i==1:
                bi.append((fi[i]-bi[i-1])/(xi[i]-xi[0]))
            else:
                numer = ((fi[i]-fi[i-1])/(xi[i]-xi[i-1]))-bi[i-1]
                denom = xi[i]-xi[0]
                bi.append(numer/denom)
        poli = bi[0]
        for i in range(1,(grado+1)):
            termino = 1
            for j in range(0,i):
                termino = termino*(x-xi[j])
            poli += bi[i]*termino
        polinomio = sym.expand(poli)
        sinsimpli = polinomio
        Px = sym.lambdify(x,polinomio)

        multi = 1
        for lista in xi: 
            multi = multi * xn-lista
        errorTeorico = (derivada/factorial(len(xi)))*multi

        valor_encontrado = Px(xn)
        er100 = abs(((valor_real-valor_encontrado)/valor_real)*100)

        '''
        print("\nPolinomio simplificado= \n", polinomio)
        print("\nvalor real =  ", valor_real)
        print("\nResultado de evaluar en el punto: ", xn, " = ", valor_encontrado)
        print("\nError porcentual = ", abs(((valor_real-valor_encontrado)/valor_real)*100) , "%")
        print("\nError teorico: ", errorTeorico)
        '''
        if len(yi) != 0:
            #no tenemos informacion para encontrar los errores.
            salida = {"sin_simplificar":sinsimpli,
            "simple":polinomio,
            "evalucion":valor_encontrado,
            "valor_real": 0,
                "errorx100": 0,
            "errorteorico": 0
            } 
        else:
            salida = {"sin_simplificar":sinsimpli,
            "simple":rcode(polinomio),
            "evalucion":valor_encontrado,
            "valor_real": valor_real,
                "errorx100": er100,
            "errorteorico": errorTeorico,
            "funcion":rcode(self.funcion), "metodo":"Newton Recursivo",
            "graficar":"si"
            } 
        return salida