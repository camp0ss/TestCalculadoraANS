import math
import sympy as sp
from sympy import *

x = sp.Symbol('x')

def ff(func, evaluator): 
    solution = func.evalf(subs={"x":evaluator})
    return solution

def error_calculator_fourth(func,estimate_value, searched_value):
    real_value = sp.diff(func,x,4)
    real_value.expand()
    real_value = real_value.subs(x, searched_value)
    e = abs(real_value-estimate_value)
    er = abs(e/real_value)
    er100 = abs((e/real_value)*100)
    errors = {"estimateValue": estimate_value , "realValue": real_value ,"e" : e ,"er" : er , "er100" : er100, "funcion":julia_code(func), "metodo":"Cuarta derivada con primer diferencia hacia adelante"}
    return errors


def error_calculator(func,estimate_value, searched_value, method_name):
    real_value = sp.diff(func,x,1)
    real_value.expand()
    real_value = real_value.subs(x, searched_value)
    e = abs(real_value-estimate_value)
    er = abs(e/real_value)
    er100 = abs((e/real_value)*100)
    errors = {"estimateValue": estimate_value , "realValue": real_value ,"e" : e ,"er" : er , "er100" : er100, "funcion":julia_code(func), "metodo":method_name}
    return errors


class Finitas:
    def __init__(self, f,arg_h,p):
            #f = funcion
            #h = h o espaciado
            #p = punto a evaluar en la derivada uwu

            self.funcion = f
            self.hx1 = arg_h
            self.punto= p


    def first_forward_diff(self):
        h = self.hx1
        point = self.punto
        func = self.funcion
        solution_FDF = (ff(func,(point+h)) - ff(func,(point)))/(h)
        #print("\nSolucion primer diferencia adelante de ",func ," en el punto ",point ," es ", solution_FDF)
        salida = error_calculator(func,solution_FDF, point, "Primera derivada con primer diferencia hacia adelante")
        #print("Errors:", salida ,"\n")
        return salida

    def first_backward_diff(self):
        h = self.hx1
        point = self.punto
        func = self.funcion
        solution_FDB = (-ff(func,(point-h)) + ff(func,(point)))/(h)
        #print("\nSolucion primer diferencia atras de ",func ," en el punto ",point ," es ", solution_FDB)
        #print("Errors:", error_calculator(func,solution_FDB, point))
        salida = error_calculator(func,solution_FDB, point,"Primera derivada con primer diferencia hacia atras")
        return salida

    def second_forward_diff(self):
        h = self.hx1
        point = self.punto
        func = self.funcion
        solution_SDF = (-ff(func,(point+(2*h)))+4*(ff(func,(point+h)))-3*(ff(func,(point))))/(2*h)
        #print("\nSolucion segunda diferencia adelante de ",func ," en el punto ",point ," es ", solution_SDF)
        #print("Errors:", error_calculator(func,solution_SDF, point))
        salida = error_calculator(func,solution_SDF, point,"Primera derivada con segunda diferencia hacia adelante")
        return salida

    def second_backward_diff(self):
        h = self.hx1
        point = self.punto
        func = self.funcion
        solution_SDB = (+ff(func,(point-(2*h)))-4*(ff(func,(point-h)))+3*(ff(func,(point))))/(2*h)
        #print("\nSolucion segunda diferencia atras de ",func ," en el punto ",point ," es ", solution_SDB)
        #print("Errors:", error_calculator(func,solution_SDB, point))
        salida = error_calculator(func,solution_SDB, point,"Primera derivada con segunda diferencia hacia atras")
        return salida

    def central_second_order(self):
        h = self.hx1
        point = self.punto
        func = self.funcion
        solution_CSO = ((ff(func,(point+h)) - ff(func,(point-h))))/(2*h)
        #print("Solucion segunda diferencia central de ",func ," en el punto ",point ," es ", solution_CSO)
        #print("Errors:", error_calculator(func,solution_CSO, point),"\n")   
        salida = error_calculator(func,solution_CSO, point,"Primera derivada con central de segundo orden") 
        return salida

    def central_fourth_order(self):
        h = self.hx1
        point = self.punto
        func = self.funcion
        solution_CFO = (  -(ff(func,(point+(2*h)))) + (8*(ff(func,(point+h)))) - (8*(ff(func,(point-h)))) + (ff(func,(point-(2*h)))) )/(12*h)
        #print("\nSolucion segunda diferencia central de ",func ," en el punto ",point ," es ", solution_CFO)
        #print("Errors:", error_calculator(func,solution_CFO, point))    
        salida = error_calculator(func,solution_CFO, point,"Primera derivada con central de cuarto orden")
        return salida

    def three_points_0(self):
        h = self.hx1
        point = self.punto
        func = self.funcion
        solution_TP0 = ((ff(func,(point+h)) - ff(func,(point-h))))/(2*h)
        #print("\nSolucion formula de 3 puntos version 1 de ",func ," en el punto ",point ," es ", solution_TP0)
        #print("Errors:", error_calculator(func,solution_TP0, point))  
        salida = error_calculator(func,solution_TP0, point,"Primera derivada con primera formula 3 puntos")
        return salida  

    def three_points_1(self):
        h = self.hx1
        point = self.punto
        func = self.funcion
        solution_TP1 = (-ff(func,(point+(2*h)))+4*(ff(func,(point+h)))-3*(ff(func,(point))))/(2*h)
        #print("\nSolucion formula de 3 puntos version 2 de ",func ," en el punto ",point ," es ", solution_TP1)
        #print("Errors:", error_calculator(func,solution_TP1, point))
        salida = error_calculator(func,solution_TP1, point,"Primera derivada con segunda formula 3 puntos")
        return salida

    def fourth_derivate_forward(self):
        h = self.hx1
        point = self.punto
        func = self.funcion
        solution_4DFDF = ((ff(func,(point))) - 4*(ff(func,(point-h))) + 6*(ff(func,(point-(2*h)))) - 4*(ff(func,(point-(3*h)))) + (ff(func,(point-(4*h))))) / (h**4)
        #print("\nSolucion formula de la cuarta derivada usando formula primer diferencia de ",func ," en el punto ",point ," es ", solution_FDF)
        #print("Errors:", error_calculator_fourth(func,solution_FDF, point))
        salida = error_calculator_fourth(func,solution_4DFDF, point)
        return salida
