import random, copy
def read_input(filename):
    data = open(filename,"r")
    G = {}
    for line in data:
        lst = [int(s) for s in line.split()]
        G[lst[0]] = lst[1:]   
    return G

def choose_random_key(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(list(G[v1]))
    return v1, v2

def karger(G):
    length = []
    while len(G) > 2:
        v1, v2 = choose_random_key(G) # 随机选择两个节点
        G[v1].extend(G[v2])           # 合并v1和v2
        # 根据合并调整边的连接
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1) 
        while v1 in G[v1]:
            G[v1].remove(v1)
        del G[v2]
    for key in G.keys(): # 得到最小割边的数量
        length.append(len(G[key]))
    return length[0]

if __name__ == "__main__":
    n = 100
    i = 0
    count = 10000  
    G = read_input("karger_data.txt")
    while i < n:
        data = copy.deepcopy(G)
        min_cut = karger(data)
        if min_cut < count:
            count = min_cut
        i = i + 1
    print(count)



