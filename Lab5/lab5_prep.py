import numpy as np
import time

def fun(x):
    return np.sin(x)

def trapez(f, a, b, h):
    x = np.arange(a,b+h,h)
    s = np.sum(f(x))-0.5*f(a)-0.5*f(b)
    return h*s

def romeberg(f,a,b,n):
    h=b-a
    I = np.zeros(shape=(n,n))
    for k in range(n):
        for j in range(n):
            if k == 0:
                I[j][k] = trapez(f,a,b,h/2**j)
            else:
                if j < n-k:
                    I[j][k] = ((4**k)*I[j+1][k-1]-I[j][k-1])/(4**k-1)
    return I[0][n-1]


a = 0
b = np.pi
h = (b - a)/20000

t1 = time.perf_counter()
c = trapez(fun,a,b,h)
t2 = time.perf_counter()
dt1 = t2-t1
print('wynik',c,'czas',dt1)

t1 = time.perf_counter()
c = romeberg(fun,a,b,5)
t2 = time.perf_counter()
dt2 = t2-t1
print('wynik',c,'czas',dt2)
print("Metoda Romberga jest szybsza: ",dt1/dt2," razy")


