import numpy as np
import matplotlib.pyplot as plt
# Least square method
def values(a,x):

    V = np.vander(x, len(a))
    y = []*len(x)
    for i in range(len(V)):
        y.append(np.dot(V[i, :][::-1], a))
    return y

def least_square_method(x,y,m):
    n = len(x)
    xsum = [0]*(2*m+1)
    for j in range(2*m+1):
        for i in range(n):
            xsum[j] += x[i]**j

    A = np.zeros(shape=(m+1,m+1))
    b = [0]*(m+1)
    for i in range(m+1):
        for j in range(m+1):
            A[i][j] = xsum[i+j]
        for k in range(n):
            b[i] += x[k] ** i * y[k]
    return (np.linalg.solve(A,b))

x0 = [1,2,3,4,5,6]
y0 = [1, 6,8,14,22,33]
x = np.arange(0,10,0.1)
plt.plot(x,x**2)
plt.plot(x0,y0,"xr")

a = least_square_method(x0,y0,2)
plt.plot(x,values(a,x))



# Lagrange'a polynomial

def lagrange_poly_fit(x0,y0,x):
    n = len(x0)
    y = [0]*len(x)
    for k in range(len(x)):
        sum1 = 0
        for i in range(n):
            sum2 = 1
            for j in range(n):
                if i != j:
                    sum2 *= (x[k]-x0[j])/(x0[i]-x0[j])
            sum1 += y0[i]*sum2
        y[k] = sum1
    return y


plt.plot(x,lagrange_poly_fit(x0,y0,x))

print(lagrange_poly_fit([0,2,3],[7,11,28],[1]))

def differential_quotient(x,y):
    a = []
    for i in range(len(x)-1):
        a.append((y[i+1]-y[i])/(x[i+1]-x[i]))
    return a


plt.show()