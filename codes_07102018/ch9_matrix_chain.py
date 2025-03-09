#-*- coding: utf-8 -*-
import time

gk = lambda i,j:str(i)+','+str(j)
def memoized_matrix_chain(p):
    n = len(p)-1
    m = {}
    for i in range(1, n+1):
        for j in range (i, n+1):
            m[gk(i, j)] = float("inf") # 初始化矩阵m
    return lookup_chain(m, p, 1, n)

def lookup_chain(m, p, i, j):
    if m[gk(i, j)] < float("inf"):
        return m[gk(i, j)]
    if i == j:
        m[gk(i, j)] = 0 # 矩阵对角置为0
    else:
        for k in range(i, j):
            q = lookup_chain(m, p, i, k) + lookup_chain(m, p, k+1, j) + p[i-1]*p[k]*p[j]
            if q < m[gk(i, j)]:
                m[gk(i, j)] = q
    return m[gk(i, j)]

def main():
    p = [30,35,15,10]
    print (memoized_matrix_chain(p))

if __name__ == '__main__':
    b = time.time()
    main()
    print ('total run time is:', time.time()-b)