#coding=utf-8
import numpy as np 
def check_equal(A, B, C):
    size_matrix = A.shape
    x = np.random.randint(2, size=size_matrix[0]) # 随机生成0/1向量x
    x.shape = (size_matrix[0],1) # 将x变成列向量
    D = A.dot(B.dot(x))          # D=A*(B*x)
    C = C.dot(x)                 # C=C*x

    for d,c in zip(D,C):         # 索引D和C中每一个元素
        if d != c:
            return False
    return True

if __name__ == "__main__": 
    num = 10 # 矩阵大小
    A = np.random.rand(num,num)
    B = np.random.rand(num,num)
    C = np.random.rand(num,num)
    k = 20  # 重复次数

    if check_equal(A, B, C):
        print("AB is equal to C")
    else: # 如果AB 不等于 C，则再重复k次，判断它们是否相等
        num_false = 0
        for ik in range(k):
            if not check_equal(A, B, C):
                num_false += 1
        if num_false == k:
            print("AB is not equal to C")
        else:
            print("uncertain")
    