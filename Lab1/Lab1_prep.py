import numpy as np

x = np.linspace(-10, 10, 1000)
y = x ** 2 - 5 * x + 3


# Bisection Method

def bisection_method(y, eps):
    min_y = np.where(y == min(y))[0][0]
    max_y = np.where(y == max(y))[0][0]
    a, b = min(max_y, min_y), max(max_y, min_y)
    if float(y[a]) * float(y[b]) > 0:
        print("Wrong choice of interval")
        x0 = 0
    else:
        while (b - a > 1):
            x0 = int(a + (b - a) / 2)
            if abs(y[x0]) < eps:
                break
            if y[x0] * y[a] > 0:
                a = x0
            else:
                b = x0
    return x0


# Regula Falsi Method

def regula_falsi_method(y, eps):
    min_y = np.where(y == min(y))[0][0]
    max_y = np.where(y == max(y))[0][0]
    a, b = min(max_y, min_y), max(max_y, min_y)
    if float(y[a]) * float(y[b]) > 0:
        print("Wrong choice of interval")
        xapp = 0
    else:
        while (b - a > 1):
            xapp = int((a * y[b] - b * y[a]) / (y[b] - y[a]))
            if abs(y[xapp]) < eps:
                break
            if y[xapp] * y[a] > 0:
                a = xapp
            else:
                b = xapp
    return xapp


# Newton Method
f = lambda x: x ** 2 - 5 * x + 3
Df = lambda x: 2 * x -5
def newton_method(f,Df,xk,eps):
    while(abs(f(xk))>eps):
        if(Df(xk)==0):
            print("Division by zero")
        else:
            xk=xk-f(xk)/Df(xk)
    return xk

i = bisection_method(y, 0.001)
j = regula_falsi_method(y, 0.001)
k = newton_method(f,Df,2,0.01)

print("Bisection Method")
print("x: {:.5f} y: {:.5f} ".format(x[i], y[i]))

print("Regula Falsi Method")
print("x: {:.5f} y: {:.5f} ".format(x[j], y[j]))

print("Newton Method")
print("x: {:.5f} y: {:.5f} ".format(k, f(k)))