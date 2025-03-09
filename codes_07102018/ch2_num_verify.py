#coding=utf-8
def num_verify(num):
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

if __name__ == "__main__": 
    print(num_verify(4))