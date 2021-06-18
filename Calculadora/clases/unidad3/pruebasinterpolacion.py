from sympy.parsing.sympy_parser import parse_expr
from hermite import Hermite

#hermite
#emulando la siguiente entrada:
#matrix = np.array([[1.3,1.6,1.9], [0.68,0.73,0.49], [0.77, 0.27, 0.41], ["-", 0.33,0.18], ["-","-",0.03]])
lstx = [1.3,1.6,1.9]
lsty = [0.68,0.73,0.49]
lst1 = [0.77, 0.27, 0.41]
lst2 = ["-", 0.33,0.18]
lst3 = ["-","-",0.03]
punto = 2.3
cas = Hermite(lstx, lsty, punto, lst1,lst2,lst3)
print("Hermite \n", cas.resultado(),"\n\n")
