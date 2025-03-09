#coding=utf-8
def max_profit_simple(prices):
    best = 0      # 记录当前的最优值
    ind_best = [] # 记录买进和卖出的时间点
    len_prices = len(prices)
    for i in range(len_prices):
        for j in range(i+1, len_prices):
            if prices[j]-prices[i]>best:   
                best = prices[j] - prices[i]
                ind_best = [i, j]
    return ind_best,best

import random
if __name__ == "__main__": 
    # 产生100个元素的随机数组
    num = 10
    prices = [random.randint(1,1000) for i in range(num)]
    random.shuffle(prices)
    random.shuffle(prices)

    print(prices)
    print(max_profit_simple(prices))
