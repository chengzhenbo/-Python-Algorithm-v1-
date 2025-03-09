#coding=utf-8
def sel_sort_rec(seq, n):
    if n==0: 
        return                              # 边界条件
    max_j = n                               # 当前最大元素索引
    for j in range(n):                      # 循环找出当前n个数据中最大的元素
        if seq[j] > seq[max_j]:             # 如果有更大的值，更新 max_j
            ax_j = j                        
    seq[n], seq[max_j] = seq[max_j], seq[n] # 交换最大值到位置n
    sel_sort_rec(seq, n-1)                  # 递归求解子问题

import random
if __name__ == "__main__": 
    # 产生100个元素的随机数组
    num = 10
    array = [random.randint(1,1000) for i in range(num)]
    random.shuffle(array)
    random.shuffle(array)
    print(array)
    sel_sort_rec(array, len(array)-1)
    print(array)