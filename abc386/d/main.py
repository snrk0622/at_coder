# TLE
N, M = map(int, input().split())
squares = [list(input().split()) for _ in range(M)]

whites = list(filter(lambda x: x[2] == 'W', squares))
blacks = list(filter(lambda x: x[2] == 'B', squares))
if len(whites) == 0 or len(blacks) == 0:
  print('Yes')
  exit()

for white in whites:
  for black in blacks:
    if int(white[0]) <= int(black[0]) and int(white[1]) <= int(black[1]):
      print('No')
      exit()
print('Yes')