from finitas import Finitas
from richardson import Richardson
from sympy.parsing.sympy_parser import parse_expr



#ejemplo de richarson
h = float(0.1)
funcion = parse_expr("log(x+1)")
buscandoenx = float(0.5)
metodo = int(1)
nivelrichard = int(3)
cas = Richardson(funcion, h, buscandoenx,metodo, nivelrichard)
print("Richardson \n", cas.resultado(),"\n\n")



## ejemplo primer derivada con primer diferencia hacia adelante
h = 0.1
funcion = parse_expr("log(x+1)")
buscandoenx = 3.51613
cas = Finitas(funcion, h, buscandoenx)
print("Primera derivada - primera diferencia hacia adelante \n", cas.first_forward_diff(),"\n\n")


#todas las demas son iguales, ejemplo
h = 0.001
vas = Finitas(funcion, 0.001, buscandoenx)
print("Cuarta derivada - primera diferencia hacia adelante \n", vas.fourth_derivate_forward(),"\n\n")

'''
first_forward_diff = primera derivada con primer diferencia hacia adelante
first_backward_diff = primera derivada con primer diferencia hacia atras
second_forward_diff = primera derivada con segunda diferencia hacia adelante
second_backward_diff = primera derivada con segunda diferencia hacia atras
central_second_order = primera derivada con central de segundo orden
central_fourth_order = primera derivada con central de cuarto orden
three_points_0 = primera derivada con primera formula 3 puntos
three_points_1 = primera derivada con segunda formula 3 puntos
fourth_derivate_forward = cuarta derivada con primer diferencia hacia adelante
'''