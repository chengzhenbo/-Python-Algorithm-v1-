#coding=utf-8
def next_larger(x):
    if x.right not NIL:
        return minimum(x.right)
    else:
        y = parent(x)
    while y not NIL and x = right(y) #找到第一次发生左转的节点
        x = y; y = parent(y)
    return y;