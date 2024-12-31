N, M = map(int, input().split())

avoids = []
moves = [
  { 'a': 2, 'b': 1, },
  { 'a': 1, 'b': 2, },
  { 'a': -1, 'b': 2, },
  { 'a': -2, 'b': 1, },
  { 'a': -2, 'b': -1, },
  { 'a': -1, 'b': -2, },
  { 'a': 1, 'b': -2, },
  { 'a': 2, 'b': -1, },
]
for _ in range(M):
  a, b = map(int, input().split())
  avoids.append((a, b))
  for move in moves:
    to = (a + move['a'], b + move['b'])
    if to[0] < 1 or to[0] > N or to[1] < 1 or to[1] > N: continue
    avoids.append(to)
print(N**2 - len(set(avoids)))