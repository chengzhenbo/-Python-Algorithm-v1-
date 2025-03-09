#coding=utf-8
def sel_sort(seq):
    for i in range(len(seq)-1,0,-1):            # i+1...n是已经排好序的部分
        max_j = i                               # 目前最大值的索引
        for j in range(i):                      # 寻找最大值
            if seq[j] > seq[max_j]: 
                max_j = j                       # 如果找到最大值则更新 max_j
        seq[i], seq[max_j] = seq[max_j], seq[i] # 交换最大值到位置n

import random
if __name__ == "__main__": 
    # 产生100个元素的随机数组
    num = 10
    array = [random.randint(1,1000) for i in range(num)]
    random.shuffle(array)
    random.shuffle(array)
    print(array)
    sel_sort(array)
    print(array)