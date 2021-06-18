import math
import pandas as pd
#metodos : 1- trapecio simple, 2- trapecio compuesto
#metodos : 3- simpson 1/3 simple, 4- simpson 1/3 complejo
#metodos : 5- simpson 3/8 simple, 6- simpson 3/8 complejo


def funcion(a, f):
        av = f.evalf(subs={"x":a, "e" : math.e})
        #print("datos a: ",a, "funcion: ",f, "valor: ",av)
        return av

class IntegracionNum:
    def __init__(self, lstX,lstFx, metodo):
        self.lstX = lstX
        self.lstFx = lstFx
        self.metodo = metodo

    def distancia(lstX):
        resu = lstX[0]-lstX[1]
        iguales = False
        n = 1
        for x in range(1, len(lstX)-1):
            resu2 = lstX[x]-lstX[x+1]
            n += 1
            if resu == resu2:
                iguales = True
            else:
                iguales = False
        salida = {"puntos":n,"iguales":iguales}
        return salida

    def resultado(self):
        opcion = IntegracionNum.distancia(self.lstX)
        if self.metodo == 1:
            if opcion["puntos"] < 2:
                print("Simple")
            else:
                print("Compuesto")
                sum = 0
                for datos in range(1, len(self.lstFx)-1):
                    sum = sum + self.lstFx[datos] 
            integral = (self.lstX[-1] - self.lstX[0])*(self.lstFx[0]+2*(sum)+self.lstFx[-1])/(2*opcion["puntos"])
            salida = {"tabla":integral} #grafica
            return salida
        
        elif self.metodo == 3:
            if opcion["puntos"] % 2 == 0: 
                print("Compuesto")
            else:
                integral = list()
                print("1/3 Simple")
                lst = list()
                iteracion = 0
                num = 0
                while num < len(self.lstX):
                    lst.append(self.lstX[num])
                    iteracion+=1
                    if iteracion == 3:
                        integral.append((lst[2] - lst[0])*(self.lstFx[self.lstX.index(lst[0])]+4*(self.lstFx[self.lstX.index(lst[1])])+self.lstFx[self.lstX.index(lst[2])])/6)
                        num -= 1
                        iteracion = 0
                        lst = list()
                        print("")

                    if iteracion == 2 and num == (len(self.lstX)-1):
                        print((float(lst[1]) - float(lst[0])))
                        integral.append((lst[1] - lst[0])*(self.lstFx[self.lstX.index(lst[0])] + self.lstFx[self.lstX.index(lst[1])])/2)
                    num +=1
                sum = 0
                for i in integral:
                    sum += i
                print(sum)

        elif self.metodo == 6:
            if opcion["puntos"] % 3 == 0: 
                print("Compuesto")
            else:
                integral = list()
                print("3/8 Simple")
                lst = list()
                iteracion = 0
                num = 0
                while num < len(self.lstX):
                    lst.append(self.lstX[num])
                    iteracion+=1
                    if iteracion == 4:
                        integral.append((lst[-1] - lst[0])*(self.lstFx[self.lstX.index(lst[0])]+3*(self.lstFx[self.lstX.index(lst[1])])+3*(self.lstFx[self.lstX.index(lst[2])])+self.lstFx[self.lstX.index(lst[3])])/8)
                        num -= 1
                        iteracion = 0
                        lst = list()
                        print("")

                    if iteracion == 3 and num == (len(self.lstX)-1):
                        integral.append((lst[-1] - lst[0])*(self.lstFx[self.lstX.index(lst[0])]+4*(self.lstFx[self.lstX.index(lst[1])])+self.lstFx[self.lstX.index(lst[2])])/6)
                    num +=1
                sum = 0
                for i in integral:
                    sum += i
                print(sum)


