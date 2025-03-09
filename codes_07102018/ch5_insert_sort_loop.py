#coding=utf-8
def ins_sort(seq):
    for i in range(1,len(seq)):                 # 0..i-1 已经排好序
        j = i                                   # 从已经排序好的元素开始
        while j > 0 and seq[j-1] > seq[j]:      # 为当前元素找到合适位置
            seq[j-1], seq[j] = seq[j], seq[j-1] # 移动seq[j]到下一个位置
            j -= 1    

import random
if __name__ == "__main__": 
    # 产生100个元素的随机数组
    num = 10
    array = [random.randint(1,1000) for i in range(num)]
    random.shuffle(array)
    random.shuffle(array)
    print(array)
    ins_sort(array)
    print(array)