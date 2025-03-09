#coding=utf-8
def ins_sort_rec(seq, n):
    if n==0:
        return                              # 边界条件
    ins_sort_rec(seq, n-1)                  # 递归求解子问题
    j = n                                   # 最后一个元素找到合适位置
    while j > 0 and seq[j-1] > seq[j]:      # 移动seq[j]到下一个位置
        seq[j-1], seq[j] = seq[j], seq[j-1] # 交换位置 
        j -= 1

import random
if __name__ == "__main__": 
    # 产生100个元素的随机数组
    num = 10
    array = [random.randint(1,1000) for i in range(num)]
    random.shuffle(array)
    random.shuffle(array)
    print(array)
    ins_sort_rec(array, len(array)-1)
    print(array)