import numpy as np
import matplotlib.pyplot as plt

def fun_gen(x):
    return x**2-5*x+3

x = np.linspace(-10,10,500)
y = fun_gen(x)
plt.plot(x,y)

# Metoda bisekcji


def bisection(y,eps):
    min_y = np.where(y==min(y))[0][0]
    max_y = np.where(y==max(y))[0][0]
    a,b = min(max_y, min_y),  max(max_y, min_y)
    if y[a]*[b]>0:
        print("Zły przedział")

    while(b-a>1):
        x0 = int(a + (b-a)/2)
        if abs(y[x0])<eps:
            break
        if y[x0]*y[a]>0:
            a = x0
        else:
            b = x0
    return x0

i = bisection(y,0.1)
print("Indecies: ", i , "\nx: ",x[i], "\ny: ", y[i])

