import numpy as np
#System of linear equations

#Upper triangular matrix

def solve_upper_traingular_matrix(A,b):
    n=len(b)
    x= [0]*n
    b = b.copy()
    b = np.array(b).astype(np.float64)
    for i in reversed(range(n)):
        if i==n-1:
            x[i]=float(b[i]/A[i][i])
        else:
            for j in reversed(range(i+1,n)):
                b[i]=b[i]-A[i][j]*x[j]
            x[i] = float(b[i] / A[i][i])
    return x

#Lower triangular matrix

def solve_lower_traingular_matrix(A,b):
    n=len(b)
    x= [0]*n
    b = b.copy()
    b = np.array(b).astype(np.float64)
    for i in range(n):
        if i==0:
            x[i]=float(b[i]/A[i][i])
        else:
            for j in range(i):
                b[i]=b[i]-A[i][j]*x[j]
            x[i] = float(b[i] / A[i][i])
    return x

#Dolitlle'a - method



A = np.array([[1,1,-1,4],[0,-2,-3,1],[0,0,2,-3],[0,0,0,2]])
B = A.transpose()

b=np.array([[8],[5],[0],[4]])
print("Lower triangular matrix")
print(solve_lower_traingular_matrix(B,b))
print("Upper traingular matrix")
print(solve_upper_traingular_matrix(A,b))

#Doolitlle'a method

def doolitle_method(A):
    n=len(A)
    L=np.eye(n)
    U=np.zeros(shape=(n,n))
    for i in range(n):
        for j in range(i+1):
            sum = 0
            for k in range(j):
                sum+=L[j][k]*U[k][i]
            U[j][i]=A[j][i]-sum

        for j in range(i+1,n):
            sum = 0
            for k in range(i):
                sum += L[j][k] * U[k][i]
            L[j][i]=float((A[j][i]-sum)/U[i][i])

    return U,L

M=[[4,-2,-3],[-6,7,6.5],[1,7.5,6.25]]
b=[12,-6,16]
U,L=doolitle_method(M)
y=solve_lower_traingular_matrix(L,b)
x=solve_upper_traingular_matrix(U,y)
print("Solution from LU decomposition")
print(x)