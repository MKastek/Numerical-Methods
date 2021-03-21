import numpy as np
#System of linear equations

#Upper triangular matrices
A = np.array([[1,1,-1,4],[0,-2,-3,1],[0,0,2,-3],[0,0,0,2]])
print(A)
b=np.array([[8],[5],[0],[4]])

def solve_upper_traingular_matrix(A,b):
    n=len(b)
    x= [0]*n
    for i in reversed(range(n)):
        if i==n-1:
            x[i]=float(b[i]/A[i][i])
            print(i)
        else:
            for j in reversed(range(i+1,n)):
                b[i]=b[i]-A[i][j]*x[j]
            x[i] = float(b[i] / A[i][i])

    return x

print(solve_upper_traingular_matrix(A,b))
