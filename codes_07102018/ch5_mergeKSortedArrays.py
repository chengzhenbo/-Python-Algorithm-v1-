#coding=utf-8
from collections import namedtuple
import heapq

def mergeKSortedArrays(alist):
    h = list()  # 最小堆
    res= list() # 合并后的输出
    heapContent = namedtuple('contents', ('elem', 'array_idx', 'array_elem_idx'))
    # 每一个序列k的第一个元素按照堆结构组织
    for i, k in enumerate(alist):
        heapq.heappush(h, heapContent(k[0],i,1))
    total_elems = len(alist)* len(alist[0])
    for _ in range(0, total_elems):
        popped = heapq.heappop(h)
        if popped.elem == float("inf"):
            continue
        res.append(popped.elem)   # 将堆中最小元素弹出并加入到res中
        next_array = popped.array_idx
        next_elem_idx = popped.array_elem_idx
        if next_elem_idx < len(alist[next_array]):
            # 将被移除出堆所属的序列的下一个元素插入到当前堆中
            heapq.heappush(h, heapContent(alist[next_array][next_elem_idx], \
                next_array, next_elem_idx+1))
        else:
            # 如果没有元素在当前序列中,则插入一个最大整数
            heapq.heappush(h, heapContent(float("inf"),next_array, float("inf"))) 
    return res
if __name__ == "__main__": 
    A = [ [1, 3, 5, 7],
           [2, 4, 6, 8],
           [0, 9, 10, 11],]
    print(A)
    print(mergeKSortedArrays(A))

