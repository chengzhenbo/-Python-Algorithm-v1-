#coding=utf-8
import random
def generate_rand_array(num=10, maxnum=1000):
    array = [random.randint(1,maxnum) for i in range(num)]
    random.shuffle(array)  # 随机打乱array中元素
    random.shuffle(array)
    return array

if __name__ == "__main__": 
    print(generate_rand_array(23,100))