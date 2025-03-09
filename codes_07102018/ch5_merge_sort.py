#coding=utf-8
def merge_sort(A):
	if len(A) <= 1:                          #边界条件
		return A
	middle = len(A) // 2
	leftA = A[:middle]
	rightA = A[middle:]
	leftA_Sorted = merge_sort(leftA)          #递归分解
	rightA_Sorted = merge_sort(rightA)        #递归分解
	return merge(leftA_Sorted, rightA_Sorted) #合并子问题的解

def merge(leftS, rightR):
	i, j=0, 0
	alist = []
	while i<len(leftS) and j<len(rightR):
		if leftS[i]<rightR[j]:
			alist.append(leftS[i]) # 将元素leftS[i]加入到序列alist中
			i+=1
		else:
			alist.append(rightR[j])# 将元素rightR[i]加入到序列alist中
			j+=1
	while i<len(leftS): #左边剩余数据处理
		alist.append(leftS[i])
		i+=1
	while j<len(rightR):#右边剩余数据处理
		alist.append(rightR[j])
		j+=1
	return alist
	
if __name__ == '__main__':
	alist = [54,26,93,17,77,31,44,55,20]
	sortedlist = merge_sort(alist)
	print(sortedlist)
