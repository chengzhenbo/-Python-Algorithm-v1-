#coding=utf-8
def subset_sum(lst, target):
    for i in range(1,2**len(lst)):        
        pick = list(mask(lst, bin(i)[2:]))      
        if sum(pick) == target:
            yield pick
def mask(lst, m): 
    m = m.zfill(len(lst))     #按照lst的位数扩展m
    return map(lambda x: x[0], filter(lambda x: x[1] != '0', zip(lst, m)))


if __name__ == "__main__": 
    k=list(subset_sum([-7, -3, -2, 5, 8], 0))
    print(k)

