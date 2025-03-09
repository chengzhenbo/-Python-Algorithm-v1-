#coding=utf-8
def dijkstra_pseudo(G,s):
    S = []                   #用于存储已经求出最短距离的节点
    while S != V:            #V表示图G中所有节点集
        c(v) = find_min(V-S) #按照贪心策略选择节点v
        S.append(v)          #将节点v加入到S 

def dijkstra_pseudo(G,s):
    S = []                            #用于存储已经求出最短距离的节点
    while S != V:                     #V表示图G中所有节点集
        c(v) = extract_min(V-S)       #从V-S中得到距离值最小节点v
        S.append(v)                   #将节点v加入到S 
        for u in v.adj:               #对与v相连接的各个邻居节点u
            if c(u) > d(v) + l(u, v): #只记录当前最小值
                c(u) = d(v) + l(u, v)