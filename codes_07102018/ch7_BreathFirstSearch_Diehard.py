#coding=utf-8
class BFSDieHardResult:
  def __init__(self):
    self.level = {}
    self.parent = {}

def bfs_diehard(start, end, jug):
	r = BFSDieHardResult()
	r.parent = {start:None}
	r.level = {start:0}

	i = 1
	frontier = [start]
	while frontier:
		next = []
		for u in frontier:
			for v in find_next_state(u, jug):
				if v not in r.level:
					r.level[v]=i
					r.parent[v]=u
					next.append(v)
					if v == end:
						print('Done')
						return r, True
		frontier = next
		i += 1
	print('Fail!')
	return r, False

def find_next_state(u, jug):
	next_state = []
	if u[0] < jug[0]: #注满第一个杯子
		next_state.append((jug[0], u[1]))
	if u[1] < jug[1]: #注满第二个杯子 
		next_state.append((u[0], jug[1]))
	if u[0]>0: #倒掉第一杯子里面的东西	
		next_state.append((0, u[1]))
	if u[1] > 0: #倒掉第二杯子里面的东西
		next_state.append((u[0], 0))
	if u[0]<jug[0]: #第一杯有空余
		if u[1] >= jug[0]- u[0]:
			next_state.append((jug[0], u[1]-(jug[0]- u[0])))
		if jug[0]- u[0] > u[1] and u[1] > 0:
			next_state.append((u[0]+u[1], 0))
	if u[1]<jug[1]: #第二杯有空余
		if u[0] >= jug[1]- u[1]:
			next_state.append((u[0]-(jug[1]- u[1]), jug[1]))
		if jug[1]- u[1] > u[0] and u[0] > 0:
			next_state.append((0, jug[1]))
	return next_state

def get_parent_state(diehard, start_state, end_state):
  v_parent_list = []
  if end_state != start_state:
    v_parent = diehard.parent[end_state]
    v_parent_list.append(v_parent)
    while v_parent != start_state and v_parent != None:
      v_parent = diehard.parent[v_parent]
      v_parent_list.append(v_parent)
  return v_parent_list

if __name__ == "__main__": 
	start_state = (0, 0)
	end_state = (4, 3)
	jug = (5, 3)
	diehard = bfs_diehard(start_state, end_state, jug)
	if diehard[1]:
		print(get_parent_state(diehard[0],start_state, end_state))

