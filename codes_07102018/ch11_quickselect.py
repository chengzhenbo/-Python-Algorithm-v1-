#coding=utf-8
import random
def partition(a):
  ## 边界条件
  if len(a)==1: 
    return([],a[0],[])
  if len(a)==2: 
    if a[0]<=a[1]:
      return([],a[0],a[1])
    else:
      return([],a[1],a[0])
  ## 随机选择支点数
  p = random.randint(0,len(a)-1)  # 支点数索引
  pivot = a[p]  # 支点数
  right = []    # 右边的划分
  left = []     # 左边的划分
  for i in range(len(a)):
    if not i == p:
      if a[i] > pivot:
        right.append(a[i])
      else:
        left.append(a[i])
  return(left, pivot, right)
  
def quick_select(a,k):
  (left,pivot,right) = partition(a)
  if len(left)==k-1:   # 支点数恰好就是第k大数
    result = pivot
  elif len(left)>k-1:  # 第k大数在左边部分划分，递归求解
    result = quick_select(left,k)
  else:                # 第k大数在右边部分划分，递归求解
    result = quick_select(right,k-len(left)-1)
  return result
  
def main():
  N = 10;
  k = 4;
  a = [random.randint(1,100) for i in range(N)]
  print('Input array: ', a)
  print('k =', k)
  b = quick_select(a,k)
  print('kth smallest element: ', b)
        
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()