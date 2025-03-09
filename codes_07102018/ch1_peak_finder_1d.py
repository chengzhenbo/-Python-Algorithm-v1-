#coding=utf-8
def geneRandomNum(num, maxnum):
    array = [random.randint(1,maxnum) for i in range(num)]
    random.shuffle(array)
    random.shuffle(array)
    return array

def peakFinder_1(array):
    array.append( float('-inf') )
    i = 0
    while i<len(array)-1:
        if array[i]>=array[i-1] and array[i]>=array[i+1]:
            return array[i]
        i+=1

def peakFinder_2(alist):
    alist.append( float('-inf') )
    first = 0
    last = len(alist)-1
    while first<=last:
        midpoint = (first + last)//2
        if alist[midpoint] < alist[midpoint-1]:
            last = midpoint-1
        elif alist[midpoint] < alist[midpoint+1]:
            first = midpoint+1
        else:
            return alist[midpoint]


import random
import time
if __name__ == "__main__": 
    # 产生100个元素的随机数组
    array = geneRandomNum(1000000, 10000)
    # print(array)
    
    start = time.time()
    print(peakFinder_1(array))
    end = time.time()
    print("time = ", end-start)