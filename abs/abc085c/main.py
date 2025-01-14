N, Y = map(int, input().split())
for x in range(N+1):
  for y in range(N+1):
    for z in range(N+1):
      if x + y + z != N: break
      otoshidama = 10000 * x + 5000 * y + 1000 * z
      if otoshidama == Y:
        print(x, y, z)
        exit()
print(-1, -1, -1)