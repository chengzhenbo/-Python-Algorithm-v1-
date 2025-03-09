from collections import defaultdict 
  
class Graph(): 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def isCyclicUtil(self, v, visited, recStack): 

        visited[v] = True    #节点是否遍历
        recStack[v] = True   #递归栈

        for neighbour in self.graph[v]: 
            if visited[neighbour] == False: 
                # 递归调用
                if self.isCyclicUtil(neighbour, visited, recStack) == True: 
                    return True
            elif recStack[neighbour] == True: 
                return True

        recStack[v] = False
        return False
  
    def isCyclic(self): 
        visited = [False] * self.V 
        recStack = [False] * self.V 
        for node in range(self.V): 
            if visited[node] == False: 
                if self.isCyclicUtil(node,visited,recStack) == True: 
                    return True
        return False
if __name__ == "__main__":   
    g = Graph(4) 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
    if g.isCyclic() == 1: 
        print ("Graph has a cycle")
    else: 
        print ("Graph has no cycle")