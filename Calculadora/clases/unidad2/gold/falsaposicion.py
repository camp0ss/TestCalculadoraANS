from math import e
from math import cos
from math import sqrt
import pandas as pd

#creando listas
lstieracion = list()
lstx1 = list()
lstx2 = list()
lstxr = list()
lstfx1 = list()
lstfxr = list()
lstfx1Xfxr = list()
lstea= list()

# funcion " f(x) = e^(-x) -x " en notacion python es: " e**(-x2) - x2 "
def fun(z):
    uwu = z**2 -3
    return uwu


salir = False
ejecucion = 1
ea = 0
es = -1

cifras = 3
x1 = 1.5
x2 = 2

ev1 = fun(x1)
#print("Evaluando funcion con el valor inicial =", ev1)
ev2 = fun(x2)
#print("Evaluando funcion con el valor final =", ev2)

if (x1*x2) < 0:
    print("Producto de las evaluaciones menor que 0 entonces si existe raiz...\n\n")

xr = x1 - ((fun(x1)*(x1-x2))/(fun(x1)-fun(x2)))
fx1 = fun(x1)
fxr = fun(xr)
fx1Xfxr = fx1 * fxr

#almacenando primer iteracion
lstieracion.append(ejecucion)
lstx1.append(x1)
lstx2.append(x2)
lstxr.append(xr)
lstfx1.append(fx1)
lstfxr.append(fxr)
lstfx1Xfxr.append(fx1Xfxr)
lstea.append(ea)

# ea = error aproximado o acumulado   //  es = error significato
while ea > es or salir == True:    
    es = (0.5*(10**(2 - cifras)))
    xrprevio = xr

    if fx1Xfxr < 0:
        x1 = x1
    else:
        x1 = xr
    if fx1Xfxr > 0:
        x2 = x2
    else:
        x2 = xr
    if fx1Xfxr == 0:
        salir = True
        print("Encontrado es xr", xr)

    xr = x1 - ((fun(x1)*(x1-x2))/(fun(x1)-fun(x2)))
    
    fx1 = fun(x1)
    fxr = fun(xr)
    fx1Xfxr = fx1 * fxr

    ea = abs((xr - xrprevio)/xr)*100

    ejecucion = ejecucion + 1

    lstieracion.append(ejecucion)
    lstx1.append(x1)
    lstx2.append(x2)
    lstxr.append(xr)
    lstfx1.append(fx1)
    lstfxr.append(fxr)
    lstfx1Xfxr.append(fx1Xfxr)
    lstea.append(ea)

df = pd.DataFrame(list(zip(lstieracion,lstx1,lstx2,lstxr,lstfx1,lstfxr,lstfx1Xfxr,lstea)), 
               columns =["Iteracion","X1","X2","Xr","f(X1)","f(Xr)","f(X1)*f(Xr)","Ea"]) 
print(df)
print("\nRaiz = ",lstxr[-1])