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


#Secant Method

def secant_method(f, x0, x1, N, debug = False):
    xk1 = x0
    xk2 = x1
    for i in range(N):
        if abs(f(xk1)-f(xk2)) != 0.0:
            xk3 = xk2 - (f(xk2) * (xk1 - xk2)) / (f(xk1) - f(xk2))
            if debug:
                if i == 0:
                    print("Step    Approximation       f(xk)")
                print("{:4}  {:12.10f}  {:12.10f}  ".format(i,xk3,f(xk3)))
            if f(xk3) == 0:
                return xk3
            else:
                xk1 = xk2
                xk2 = xk3
    return xk3

i = bisection_method(y, 0.001)
j = regula_falsi_method(y, 0.001)
k = newton_method(f,Df,2,0.01)
l=secant_method(f,1,2,10,False)


print("Bisection Method")
print("x: {:.5f} y: {:.5f} ".format(x[i], y[i]))

print("Regula Falsi Method")
print("x: {:.5f} y: {:.5f} ".format(x[j], y[j]))

print("Newton Method")
print("x: {:.5f} y: {:.5f} ".format(k, f(k)))

print("Secant Method")
print("x: {:.5f} y: {:.5f}".format(l,f(l)))