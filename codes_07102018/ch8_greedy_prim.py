import heapq
import math
class PriorityQueue:
  def __init__(self):
    self.key = {}    # 记录节点的key值
    self.pqueue = [] # 用于建堆

def prim(graph,source):
    Q = PriorityQueue()
    mst = {}
    parent = {}
    # 将图中节点初始化到堆中
    for v in graph:
        if v == source: 
            Q.key[v] = 0
            heapq.heappush(Q.pqueue, (0, v))
        else:
            Q.key[v] = math.inf
            heapq.heappush(Q.pqueue, (math.inf,v))
    parent[source] = None
    while Q.pqueue:
        (v_key, v) = heapq.heappop(Q.pqueue) # 贪心策略,取出堆中最小元素
        del Q.key[v]
        mst[v] = parent[v]
        for u in graph[v]:
            if u in Q.key and u not in mst:
                if graph[v][u]<Q.key[u]:
                    # 将堆Q.pqueue中节点u的key值更新为graph[v][u]
                    ind_key = Q.pqueue.index((Q.key[u],u))
                    Q.pqueue.pop(ind_key)
                    heapq.heappush(Q.pqueue, (graph[v][u],u))
                    Q.key[u] = graph[v][u]
                    parent[u] = v   
    return mst

if __name__ == "__main__":
    graph = {'a': {'b': 1, 'c': 1},
            'b': {'a': 2, 'c': 2, 'd':1},
            'c': {'a': 1, 'b': 2, 'd': 3},
            'd': {'b': 1, 'c': 3}}
    print(prim(graph,'b'))

