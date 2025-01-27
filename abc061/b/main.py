N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
flatAB = [city for row in AB for city in row]

for i in range(1, N+1):
  print(flatAB.count(i))