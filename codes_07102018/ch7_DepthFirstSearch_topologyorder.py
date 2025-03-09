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
    self.order = []

def dfs(g):
  results = DFSResult()
  for v in g.adj.keys():
    if v not in results.parent:
      dfs_visit(g, v, results)
  return results

def dfs_visit(g, v, results, parent=None):
  results.parent[v] = parent
  for n in g.adj[v]:
    if n not in results.parent:
      dfs_visit(g, n, results, v)
  results.order.append(v)

def topological_sort(g):
  dfs_result = dfs(g)
  dfs_result.order.reverse()
  return dfs_result.order

if __name__ == "__main__": 
    graph = Graph()
    graph.adj = { "a" : ["b","d"],
          "b" : ["e"],
          "d" : ["b"],
          "e" : ["d"],
          "c" : ["e", "f"],
          "f" : ["f"]
        }
    print (topological_sort(graph))