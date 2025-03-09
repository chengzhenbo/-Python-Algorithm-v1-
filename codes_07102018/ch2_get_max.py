#coding=utf-8
def get_max(A):
    n=len(A)
    max = A[0]
    for i in range(1, n):
        if A[i]>max:
            max=A[i]
    return max
    
if __name__ == "__main__": 
    print(get_max([3, 4, 52, 8]))