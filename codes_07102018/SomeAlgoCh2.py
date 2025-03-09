#coding=utf-8
def some_algo(i, j):
    k = 3
    if i > j:
        return i
    else: 
        return k

def maxA(A):
    n=len(A)
    max = A[0]
    for i in range(1, n):
        if A[i]>max:
            max=A[i]
    return max

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def subset_sum(lst, target):
    for i in xrange(1,2**len(lst)):        #穷举所有的子集合
        pick = mask(lst, bin(i)[2:])       #通过二进制数表示元素是否在集合内
        if sum(pick) == target:
            yield pick
def mask(lst, m): 
    m = m.zfill(len(lst))
    return map(lambda x: x[0], filter(lambda x: x[1] != '0', zip(lst, m)))

def numVerify(num):
    if num < 0:
        num = 0
        print('非负数转换为0!')
    elif num == 0:
        print('零')
    elif num == 1:
        print('等于1')
    else:
        print('大于1')
    return num

def sumNums(low, high):
    if high<low:
        print("error")
        return 
    sumnum = 0
    for i in range(low,high+1):
        print(i)
        sumnum += i
    return sumnum
# #list examples
# >>> a = [66.25, 333, 333, 1, 1234.5]
# >>> print(a.count(333), a.count(66.25), a.count('x')) # 计算链表中元素个数
# 2 1 0
# >>> a.insert(2, -1)                                   # 在a中2号位插入元素-1
# >>> a.append(333)                                     # 将333插入到a的末尾
# >>> a
# [66.25, 333, -1, 333, 1, 1234.5, 333]
# >>> a.index(333)                                      # 获得元素的索引
# 1
# >>> a.remove(333)                                     # 移除指定元素333
# >>> a
# [66.25, -1, 333, 1, 1234.5, 333]
# >>> a.reverse()                                       # 将a中元素反向
# >>> a
# [333, 1234.5, 1, 333, -1, 66.25]
# >>> a.sort()                                          # 对a中元素排序
# >>> a
# [-1, 1, 66.25, 333, 333, 1234.5]
# >>> a.pop()                                           # 移除a中最后一个元素
# 1234.5
# >>> a
# [-1, 1, 66.25, 333, 333]

# import random
# def generate_rand_array(num=10, maxnum=1000):
#     array = [random.randint(1,maxnum) for i in range(num)]
#     random.shuffle(array)
#     random.shuffle(array)
#     return array

# #将字符串按字符输出
# word_list = ['cat','dog','rabbit']
# letter_list = [ ]
# for a_word in word_list:
#     for a_letter in a_word:
#         if a_letter not in letter_list:
#             letter_list.append(a_letter)
# print(letter_list)

# # 字典使用示例
# >>> tel = {'jack': 4098, 'sape': 4139}        #构造字典
# >>> tel['guido'] = 4127                       #添加新的键值对
# >>> tel
# {'sape': 4139, 'guido': 4127, 'jack': 4098}
# >>> tel['jack']                               #根据键得到对应的值
# 4098
# >>> del tel['sape']                           #删除一个键值对
# >>> tel['irv'] = 4127
# >>> tel
# {'guido': 4127, 'irv': 4127, 'jack': 4098}
# >>> list(tel.keys())                          #列出所有的键
# ['irv', 'guido', 'jack']
# >>> sorted(tel.keys())                        #按键进行排序
# ['guido', 'irv', 'jack']
# >>> 'guido' in tel                            #某个键是否在字典中
# True
# >>> 'jack' not in tel
# False



if __name__ == "__main__": 
    # testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    # print(binarySearch(testlist, 32))
    # print(binarySearch(testlist, 13))

    # print list(subset_sum ([-7, -3, -2, 5, 8], 0))
    # m = mask([2, 3, 7], bin(3)[2:])
    # print m
    A = [2,3, 4,8]
    
    print(maxA(A))

