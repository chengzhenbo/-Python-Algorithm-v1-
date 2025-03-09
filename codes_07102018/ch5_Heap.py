#coding=utf-8
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def max_heapify_rec(self,i):
      if (i * 2) <= self.currentSize:      #存在子节点
          mc = self.maxChild(i)            #找到当前节点与子节点中最大的节点
          if self.heapList[i] < self.heapList[mc]: #将当前节点与最大值节点交换
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
              self.max_heapify_rec(mc)     #递归调用,继续处理最大节点mc

    def maxChild(self,i):
      leftchild = i*2
      rightchild = i*2+1
      if leftchild <= self.currentSize and self.heapList[leftchild]>self.heapList[i]:
        largest = leftchild
      else:
        largest = i
      if rightchild <= self.currentSize and self.heapList[rightchild]>self.heapList[largest]:
        largest = rightchild
      return largest

    def max_heapify(self,i):
      while (i * 2) <= self.currentSize:            #直到叶子节点
          mc = self.maxChild(i)                     #找到当前节点与子节点中最大
          if self.heapList[i] < self.heapList[mc]:  #将当前节点与最大值节点交换
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc
          
    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1
    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      mid = len(alist) // 2            # 得到第一个有叶子节点的索引
      self.currentSize = len(alist)    # 初始化堆大小
      self.heapList = [0] + alist[:]   # 初始化堆元素
      while (mid > 0):
          self.max_heapify_rec(mid)    # 调用堆化函数
          mid = mid - 1
          
A = [2,3,5,6,9]
bh = BinHeap()
bh.buildHeap(A)
print (bh.heapList)


# Build_Max_Heap(A):
# for i=n/2 downto 1
# do Max_Heapify(A, i)
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())