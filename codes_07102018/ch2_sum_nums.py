#coding=utf-8
def sum_nums(low, high):
    if high<low:
        print("error")
        return 
    sumnum = 0
    for i in range(low,high+1):
        sumnum += i
    return sumnum

if __name__ == "__main__": 
    print(sum_nums(0,100))