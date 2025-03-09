#coding=utf-8
import math
def closestpair_simple(X, n):
    min_d = distance(X[0], X[1])          #记录当前最小距离     
    for i,(x,y) in enumerate(X):
        for j in range(i+1, n):
            if distance(X[i], X[j]) < min_d:
                min_p = [X[i], X[j]]      #记录哪两个点
                min_d = distance(X[i], X[j])  
    return  min_p,min_d

def distance(a,b):                        #计算两点之间的欧拉距离
    return math.sqrt( math.pow( (a[0]-b[0]), 2) + math.pow((a[1]-b[1]), 2) )


if __name__ == "__main__": 
    points = [(2,3), (10, 1), (3, 25), (23,15),
             (18,3), (8,9), (12,30), (25,30),
             (9,2), (13,10), (3,4), (5,6),
             (22,32), (5,32), (23,9), (19,25),
             (14,1), (11,25), (26,26), (12,9),
             (18,9), (27,13), (32,13)]
    print (closestpair_simple(points, len(points)))