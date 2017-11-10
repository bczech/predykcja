import numpy as np
import pandas as pd

data=pd.read_csv('pedigree2.txt', sep='\t') #wczytanie danych pedigree
data=data.as_matrix()

def RelMatrixA(s,d):
    n = len(s)
    N = n + 1
    A = np.zeros((N,N))
    s = ( s == 0 ) * N + s
    d = ( d == 0 ) * N + d
    for i in range(n):
        A[i,i] = 1 + A[s[i]-1, d[i]-1] * 0.5
        for j in range(i+1,n):
            if j > n:
                break
            A[i,j] = (A[i,s[j]-1] + A[i,d[j]-1]) * 0.5
            A[j,i] = A[i,j]
    return A
n = len(data[:,0])
wynik = RelMatrixA(data[:,1],data[:,2])[0:n,0:n]
print(wynik)