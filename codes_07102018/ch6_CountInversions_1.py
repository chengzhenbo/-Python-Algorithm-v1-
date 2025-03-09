#coding=utf-8
def count_inversions_simple(A):
    inv_count = 0
    inv_list = []
    lenA = len(A)
    for i in range(lenA):            #索引A中各个元素
        for j in range(i, lenA):     #得到A中某个元素所有右边的元素
            if A[i] > A[j]:          #判断是否存在逆序
                inv_count += 1
                inv_list.append([A[i],A[j]])
    return inv_count, inv_list

if __name__ == '__main__':
    alist = [2, 4, 1, 3, 5]
    print(count_inversions_simple(alist))
