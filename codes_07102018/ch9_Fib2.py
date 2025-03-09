#coding=utf-8
memo = {}                           
def fib2(n): 
    if n in memo:                     # 查表
        return memo[n]
    else:
        if n <= 2:                    # 边界条件
            f = 1
        else:
            f = fib2(n-1) + fib2(n-2) # 递归调用
        memo[n] = f                   # 将结果存储于表中
        return f
                          
def fib_bottom_up(n): 
    fib = {}                          # 存储结果的字典
    for k in range(n+1):
        if k<=2:                      # 边界条件
            f = 1
        else:
            f = fib[k-1]+fib[k-2]     # 自底向上填表
        fib[k] = f
    return fib[n]
    
if __name__ == '__main__':
    num = 100
    for inum in range(num+1):
        print('{0:5}==>{1:10d}'.format('fib('+str(inum)+')', fib_bottom_up(inum)))
