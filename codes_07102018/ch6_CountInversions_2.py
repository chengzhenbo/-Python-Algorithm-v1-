#coding=utf-8
def count_inversions_dc(A):
    lenA = len(A)
    if lenA <= 1:                                      #边界条件
        return 0, A
    middle = lenA // 2
    leftA = A[:middle]
    rightA = A[middle:]
    countLA, leftA = count_inversions_dc(leftA)        #递归分解
    countRA, rightA = count_inversions_dc(rightA)      #递归分解
    countLRA, mergedA = merge_and_count(leftA, rightA) #合并并计算逆序数
    
    return countLA+countRA+countLRA, mergedA

def merge_and_count(A, B):
    i, j, inv_count =0, 0, 0
    alist = []
    lenA = len(A);lenB = len(B)
    while i<lenA and j<lenB:
        if A[i]<B[j]:
            alist.append(A[i])
            i+=1
        else:                        # b[j]与A当前所有左边元素构成逆序
            inv_count += lenA-i
            alist.append(B[j])
            j+=1
    while i<lenA:                    # 处理A中剩余元素
        alist.append(A[i])
        i+=1
    while j<lenB:                    # 处理B中剩余元素
        alist.append(B[j])
        j+=1
    return inv_count, alist
    
if __name__ == '__main__':
    alist = [5,7,3,8,6]
    print(count_inversions_dc(alist))



