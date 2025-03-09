#coding=utf-8

class Graph:
	def __init__(self):
		self.adj = {}
	def add_edge(self, u, v):
		if self.adj[u] is None:
		 	 self.adj[u] = []
		self.adj[u].append(v)

class DFSResult:
  def __init__(self):
    self.parent = {}
    self.visited = []

def dfs_iterative(graph):
  results = DFSResult()

  for v in graph.adj.keys():
    if v not in results.parent:
      results.parent[v] = None
      if v not in results.visited:
        stack = [v]
        while stack:
          u = stack.pop()
          if u not in results.visited:
            results.visited.append(u)
          for n in graph.adj[u]:
            if n not in results.visited:
              results.parent[n]=results.visited[-1]
              stack.extend(n)
  return results

if __name__ == "__main__": 
    graph = Graph()
    graph.adj = { "a" : ["b","d"],
          "b" : ["e"],
          "d" : ["b"],
          "e" : ["d"],
          "c" : ["e", "f"],
          "f" : ["f"]
        }
    print(dfs_iterative(graph).parent)
