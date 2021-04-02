import numpy as np

def power_method_eigenvector(A,v):
    A = np.array(A)
    v = np.array(v)
    v2 = v
    while True:
        v1 = v2
        v2 = A.dot(v1)
        v2 = v2 / max(v2)
        v1 = v1/max(v1)
        if np.array_equal(v1,v2): break
    return v2/max(v2)

A=[[4,1,0],[0,2,1],[0,0,-1]]
#print(power_method_eigenvector(A,[1,1,1]))

def QR_decomposition(A):
    A = np.array(A)
    N = len(A)
    Q = np.eye(N)
    for i in range(N-1):
        e = np.zeros(shape=N)
        e[i] = 1
        ai = A[:,i].copy()
        for j in range(len(ai)):
            if j < i:
                ai[j] = 0
        v = ai+np.linalg.norm(ai)*e
        H = np.eye(N)-(2.0/(v.T.dot(v)))*(np.outer(v,v.T))
        A = H.dot(A)
        Q = Q.dot(H)

    return A,Q

A=[[1,2,-1],[1,4,5],[1,4,1]]


for k in range(5):
    R,Q=QR_decomposition(A)
    A=R.dot(Q)

print(np.round(A,3))

