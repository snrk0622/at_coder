N = int(input())

can = True
now = {
  't': 0,
  'x': 0,
  'y': 0,
}
for _ in range(N):
  t, x, y = map(int, input().split())
  diff = t - now['t']
  manhattanDistance = abs(x - now['x']) + abs(y - now['y'])
  if manhattanDistance > diff:
    can = False
    break
  elif diff % 2 == 0 and manhattanDistance % 2 != 0:
    can = False
    break
  elif diff % 2 != 0 and manhattanDistance % 2 == 0:
    can = False
    break
  now = {
    't': t,
    'x': x,
    'y': y,
  }

print('Yes' if can else 'No')