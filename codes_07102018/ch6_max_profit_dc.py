#coding=utf-8
def max_profit_dc(prices):
    len_prices = len(prices)
    if len_prices <= 1:                               #边界条件
        return 0
    mid = len_prices//2
    prices_left = prices[:mid]     
    prices_right = prices[mid:]
    maxProfit_left = max_profit_dc(prices_left)      #递归求解左边序列
    maxProfit_right = max_profit_dc(prices_right)    #递归求解右边序列
    maxprofit_left_right = max(prices_right)-min(prices_left) #可能跨界
    return max(maxProfit_left, maxProfit_right, maxprofit_left_right)

import random
if __name__ == "__main__": 
    # 产生100个元素的随机数组
    num = 10
    prices = [random.randint(1,1000) for i in range(num)]
    random.shuffle(prices)
    random.shuffle(prices)

    print(prices)
    print(max_profit_dc(prices))