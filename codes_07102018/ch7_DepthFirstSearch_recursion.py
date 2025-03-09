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

def dfs(g):
  results = DFSResult()
  for v in g.adj.keys():
    if v not in results.parent:
      dfs_visit_r(g, v, results)
  return results

def dfs_visit_r(g, v, results, parent=None):
  results.parent[v] = parent
  for u in g.adj[v]:
    if u not in results.parent:     # 节点u还未遍历到
      dfs_visit_r(g, u, results, v) # 递归

if __name__ == "__main__": 
    graph = Graph()
    graph.adj = { "a" : ["b","d"],
          "b" : ["e"],
          "d" : ["b"],
          "e" : ["d"],
          "c" : ["e", "f"],
          "f" : ["f"]
        }
    dfs_result =  dfs(graph)
    print(dfs_result.parent)
