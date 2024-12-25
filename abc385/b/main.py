H, W, X, Y = map(int, input().split())
squares = [list(input()) for _ in range(H)]
T = list(input())

home = []
for t in T:
  x, y = X, Y
  if t == 'U':
    x -= 1
  elif t == 'D':
    x += 1
  elif t == 'L':
    y -= 1
  else:
    y += 1
  next = squares[x - 1][y - 1]
  if next != '#':
    X, Y = x, y
    if next == '@' and not (x, y) in home:
      home.append((x, y))
print(X, Y, len(home))