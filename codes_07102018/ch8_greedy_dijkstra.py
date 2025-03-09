#coding=utf-8
import heapq
def dijkstra(graph,source):
    priority_queue = [] # 优先队列
    # 堆初始化
    heapq.heappush(priority_queue, (0, source))
    visited = {} # 存储输出结果的字典结构
    while priority_queue:
        # 从堆中获取最小距离节点
        (current_distance, current) = heapq.heappop(priority_queue)
        if current not in visited:  # 将距离值添加到visited
              visited[current] = current_distance
        if current not in graph: continue
        # 更新与current相邻各节点neighbour的distance
        for neighbour, distance in graph[current].items():
            if neighbour in visited: continue
            new_distance = current_distance + distance
            heapq.heappush(priority_queue, (new_distance, neighbour))
    return visited


if __name__ == "__main__":
    graph = {'s': {'a': 4, 'c': 16, 'b':8},
            'a': {'b': 3},
            'c': {'d': 2},
            'b': {'c': 7, 'e': 1},
            'e': {'c': 5, 'd': 6},
            'd': {}}

    print(dijkstra(graph,'s'))