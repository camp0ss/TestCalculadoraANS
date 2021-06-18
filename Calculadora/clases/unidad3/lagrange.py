import decimal
import math
from scipy.interpolate import lagrange
from sympy import *
from math import *
from sympy.parsing import sympy_parser


class Lagrange:
    def __init__(self, f,t,p):
        #f = funcion
        #t = lista con valores de x
        #e = valor de x que se busca en la funcion
        self.tabla = t
        self.punto = p
        self.funcion = f

    def factorial(n):
        if n<=1:
            return 1 
        return n*factorial(n-1) 

    def resultado(self):

        x, y, z = symbols('x y z')
        init_printing(use_unicode=True)
        init_printing()

        convertido2 = self.funcion
        valor_real = convertido2.subs(x, self.punto)
        
        evaluador = self.punto

        listax = self.tabla
        listafx = list()

        #generando valores de fx
        for uwu in listax:
            temp = convertido2.subs(x, uwu)
            listafx.append(temp)

        #codigo para derivar

        deri = diff(convertido2,x,len(listax))
        deri.expand()
        derivada = deri.subs(x, evaluador)

        '''
        print("x = ", listax)
        print("f(x) = ", listafx)
        '''

        sup = ""
        resp = ""

        for exterior in range(0, len(listafx)):
            bloqueado = exterior
            if exterior == bloqueado:
                inf = "*1/("
                resp = resp + "+(" + str(listafx[exterior])+"*"
            for generadorfraccion in range(0, len(listafx)): 
                if generadorfraccion != bloqueado:
                        sup = sup + "*(x-" + str(listax[generadorfraccion])+")"
                        resp = resp + "(x-" + str(listax[generadorfraccion])+")" 
                        inf= inf+"("+str(listax[bloqueado])+"-"+str(listax[generadorfraccion])+")"
            inf = inf +")"
            resp = resp + inf +")"

        resp = resp.replace(")(",")*(")
        '''
        print("\n" , resp, "\n")
        '''
        sinsimplificar = resp
        parseado = parse_expr(resp)

        simple =simplify(parseado)
        evaluacion = parseado.subs(x, evaluador).evalf()
        multi = 1
        for lista in listax: 
            multi = multi * evaluador-lista 
        errorTeorico = (derivada/factorial(len(listax)))*multi 
        er100 = (abs((valor_real-evaluacion)/valor_real))*100

        '''
        print("\nPolinomio simplificado = \n", simple)
        print("\nvalor real =  ", valor_real)
        print("\nResultado de evaluar en el punto: ", evaluador , " = ",evaluacion)
        print("\nError porcentual = ", er100  , "%")
        print("\nError teorico: ", errorTeorico) 
        '''

        salida = {"sin_simplificar":sinsimplificar,
         "simple":rcode(simple),
          "evalucion":evaluacion,
           "valor_real": valor_real,
            "errorx100": er100,
         "errorteorico": errorTeorico,
         "funcion":rcode(self.funcion), "metodo":"Lagrange",
         "graficar":"si"
        } 
        return salida

class Lagrange_tabla:
    def __init__(self, tx,ty,p):
        #f = funcion
        #t = lista con valores de x
        #e = valor de x que se busca en la funcion
        self.tablax = tx
        self.tablay = ty
        self.punto = p

    def factorial(n):
        if n<=1:
            return 1 
        return n*factorial(n-1) 

    def resultado(self):

        x, y, z = symbols('x y z')
        init_printing(use_unicode=True)
        init_printing()

        convertido2 = sympify("x")
        valor_real = convertido2.subs(x, self.punto)
        
        evaluador = self.punto

        listax = self.tablax
        listafx = list()
        listafx = self.tablay
        
        #codigo para derivar
        deri = diff(convertido2,x,len(listax))
        deri.expand()
        derivada = deri.subs(x, evaluador)

        '''
        print("x = ", listax)
        print("f(x) = ", listafx)
        '''

        sup = ""
        resp = ""

        for exterior in range(0, len(listafx)):
            bloqueado = exterior
            if exterior == bloqueado:
                inf = "*1/("
                resp = resp + "+(" + str(listafx[exterior])+"*"
            for generadorfraccion in range(0, len(listafx)): 
                if generadorfraccion != bloqueado:
                        sup = sup + "*(x-" + str(listax[generadorfraccion])+")"
                        resp = resp + "(x-" + str(listax[generadorfraccion])+")" 
                        inf= inf+"("+str(listax[bloqueado])+"-"+str(listax[generadorfraccion])+")"
            inf = inf +")"
            resp = resp + inf +")"

        resp = resp.replace(")(",")*(")
        '''
        print("\n" , resp, "\n")
        '''
        sinsimplificar = resp
        parseado = parse_expr(resp) #polinomio sin simplificar
        simple =simplify(parseado) #simplificando el polinomio
        evaluacion = parseado.subs(x, evaluador).evalf() #evaluando el x dada en el polinimio generad

        multi = 1
        for lista in listax: 
            multi = multi * evaluador-lista 
        errorTeorico = (derivada/factorial(len(listax)))*multi 

        er100 = (abs((valor_real-evaluacion)/valor_real))*100 #calculando error porcentual

        '''
        print("\nPolinomio simplificado = \n", simple)
        print("\nvalor real =  ", valor_real)
        print("\nResultado de evaluar en el punto: ", evaluador , " = ",evaluacion)
        print("\nError porcentual = ", er100  , "%")
        print("\nError teorico: ", errorTeorico) 
        '''

        salida = {"sin_simplificar":sinsimplificar,
         "simple":rcode(simple),
          "evalucion":evaluacion,
           "valor_real": 0,
            "errorx100": 0,
         "errorteorico": 0,
         "funcion":rcode(simple), "metodo":"Lagrange",
         "graficar":"si"
        } 
        return salida