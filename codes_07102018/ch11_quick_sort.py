#coding=utf-8
from random import randint
def inPlaceQuickSort(A,start,end):
    if start<end:
        pivot=randint(start,end)     # 随机选择一个支点数
        temp=A[end]
        A[end]=A[pivot]
        A[pivot]=temp
        
        p=partition(A,start,end)      # 按照支点数划分A
        inPlaceQuickSort(A,start,p-1) # 递归处理左边部分元素
        inPlaceQuickSort(A,p+1,end)   # 递归处理右边部分元素

def partition(A,start,end):
    pivot=randint(start,end)
    temp=A[end]
    A[end]=A[pivot]
    A[pivot]=temp
    newPivotIndex=start-1
    for index in range(start,end):
        if A[index]<A[end]:
            newPivotIndex=newPivotIndex+1
            temp=A[newPivotIndex]
            A[newPivotIndex]=A[index]
            A[index]=temp
    temp=A[newPivotIndex+1]
    A[newPivotIndex+1]=A[end]
    A[end]=temp
    return newPivotIndex+1

if __name__ == "__main__": 
    alist = [54,26,93,17,77,31,44,55,20]
    inPlaceQuickSort(alist,0,len(alist)-1)
    print(alist)