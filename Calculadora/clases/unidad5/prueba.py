from euler import Euler
from taylor import Taylor
from runge import Runge
from multipasos import MRunge, AdamsBashforth, AdamsMoulton,MEuler

#pru = Euler("y+2*x*exp(2*x)",0,1,3,3)
#print(pru.eulerAtras())

#prue = Taylor("cos(x)+y",0,1,3,6,4)
#print(prue.taylor())

#prue = Runge("2*x*y",0,1,0.5,5)
#print(prue.rungeCuatro())
#ejemplo del uso del metodo de multipasos, primero se elige un metodo inicial ya sea Euler o runge-katta

funcion = "x+y-1"
xo = 0
yo = 1
h = 0.2
xlim = 0.8
n = 4
prue = MRunge(funcion,xo,yo,xlim,h,n)
[x,y] = prue.rungeCuatro()
#luego se escoge el metodo predictor, se le pasa la lista de x, la lista de y, la funcion, el espaciado y cuantos niveles o divisiones
predictor = AdamsBashforth(x,y,funcion,h)
salida1 = predictor.cuatroPasos()
#y por ultimo se escoge el metodo corrector, se le para la salida del metodo predictor, la lista de y, el espaciado y cuantos niveles o divisiones
corrector = AdamsMoulton(salida1,y,h)
salida2 = corrector.tresPaso()
#salida2 es la respuesta final, el penultimo valor del array salida1 es el resultado del metodo predictor, el ultimo valor del array salida1 es la respuesta final
print(salida2)
for i in range(0,len(salida1)):
    print(salida1[i])