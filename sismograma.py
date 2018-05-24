"""#programa para calcular velocidades de un modelo de 2 capas
Proyecto de Posprocesado sismico
Autor: RESENDIZ AVILES JOSE ANGEL
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean
from matplotlib import style
style.use('classic')

datos = pd.read_csv('sismograma.csv')

tiempo    = datos.iloc[:,0]
distancia = datos.iloc[:,1]


xs = np.array(tiempo,    dtype=np.float64)
ys = np.array(distancia, dtype=np.float64)
#print(xs[:n])

n1 = 0
while ys[n1] < ys[n1+1]:
    n1+=1
#print(n1)

xs1 = xs[:n1]
ys1 = ys[:n1]


def calculo_de_pendiente1(xs1,ys1):
    m1 = (   ( (mean(xs1)*mean(ys1)) - mean(xs1*ys1) ) /
    ((mean(xs1)*mean(xs1)) - mean(xs1*xs1))   )

    b1 = mean(ys1) - m1*mean(xs1)
    return m1, b1

m1, b1 = calculo_de_pendiente1(xs1,ys1)

regresion_linear1 = [(m1*x)+b1 for x in xs1]

#ahora a qui va la segunda pendiente
n2  = len(tiempo) - n1
xs2 = xs[-n2:]
#print(xs2)
ys2 = ys[-n2:]

def calculo_de_pendiente2(xs2,ys2):
    m2 = (   ( (mean(xs2)*mean(ys2)) - mean(xs2*ys2) ) /
    ((mean(xs2)*mean(xs2)) - mean(xs2*xs2))   )

    b2 = mean(ys2) - m2*mean(xs2)
    return m2, b2

m2, b2 = calculo_de_pendiente2(xs2,ys2)

regresion_linear2 = [(m2*x)+b2 for x in xs2]


print(datos)
plt.title("Primeros arrivos del sismograma")
plt.xlim(5,25)
plt.ylim(6,18)
plt.grid(True, which = 'both')
plt.xlabel("Distancia (x)")

plt.ylabel("Tiempo f(x)")
plt.scatter(tiempo,distancia)
plt.plot(xs1, regresion_linear1)
plt.plot(xs2, regresion_linear2)
plt.show()

print("Pendiente1 =",m1)
print("Pendiente2 =",m2)
