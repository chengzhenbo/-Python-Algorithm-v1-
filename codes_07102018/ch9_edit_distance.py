#-*- coding: utf-8 -*-
def  min_edit_dist(target, source):  
    n = len(target)
    m = len(source)
    # 初始化二维动态规划表
    distance = [[0 for i in range(m+1)] for j in range(n+1)]
    # 边界条件
    for i in range(n):
        distance[i][m-1] = distance[i+1][m] + insertCost(target[i])
    for j in range(m):
        distance[n-1][j] = distance[n][j+1] + deleteCost(source[j])
    distance[n-1][m-1] = substCost(source[m-1],target[n-1])
    # 自底向上求解递归式
    for i in range(n-2,-1, -1):
        for j in range(m-2,-1, -1):
           distance[i][j] = min(distance[i+1][j]+1,
                                distance[i][j+1]+1,
                                distance[i+1][j+1]+substCost(source[j],target[i]))
    return distance

def insertCost(i):
    return 1

def deleteCost(i):
    return 1

def substCost(i, j):
    if i==j:
        return 0
    else:
        return 1

if __name__ == '__main__':
    target = 'sunday'
    source = 'saturday'
    print(min_edit_dist(target, source))