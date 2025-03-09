#coding=utf-8

def bottom_up_cont_subseq(alist):
    table = [None] * (len(alist) + 1)
    table[0] = 0
    for i in range(1, len(alist)+1):
        table[i] = max(table[i-1] + alist[i-1], alist[i-1])
    return table

def track_back_subseq(alist, table):
    import numpy as np          # numpy是python中常用的数学库
    select = []
    max_sum = max(table)
    ind_max = np.argmax(table)  # 得到table中最大值索引
    while ind_max >= 1:
        if table[ind_max] == alist[ind_max-1]+table[ind_max-1]:
            select.append(alist[ind_max-1])
            ind_max -= 1
        else:
            select.append(alist[ind_max-1])
            break
    return select


if __name__ == '__main__':  
	# [-2, 3, -16, 100, -4, 5] [-15,-23,-476,-3, -292] [-2,11,-4,13,-5,2]
	alist = [-2,11,-4,13,-5,2]
	print (alist)
	table = bottom_up_cont_subseq(alist)
	print (table)
	track_back_subseq(alist, table)
	print (track_back_subseq(alist, table))

    