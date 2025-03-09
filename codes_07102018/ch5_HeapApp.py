#coding=utf-8
from heapq import heappop, heapify
def heapsort(alist):
	sortedh = []
	#为alist构造堆
	heapify(alist)
	while alist:
		#提取堆根节点元素
		sortedh.append(heappop(alist))
	return sortedh

import random
if __name__ == "__main__": 
	# 产生10个元素的随机数组
    num = 10
    array = [random.randint(1,1000) for i in range(num)]
    random.shuffle(array)
    random.shuffle(array)
    print( array)
    K = heapsort(array)
    print( K)