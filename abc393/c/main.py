N, M = map(int, input().split())
simple_graph = set()
for _ in range(M):
  edge = tuple(sorted(map(int, input().split())))
  if edge[0] == edge[1]: continue
  simple_graph.add(edge)

print(M - len(simple_graph))