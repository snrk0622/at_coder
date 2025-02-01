N, Q = map(int, input().split())
pigeons = [idx for idx in range(N)]
houses = [1] * N
cnt = 0

for _ in range(Q):
  inputs = list(input().split())
  query = inputs[0]
  if query == '1':
    P, H = int(inputs[1]), int(inputs[2])
    if houses[pigeons[P-1]] == 2:
      cnt -= 1
    houses[pigeons[P-1]] -= 1
    pigeons[P-1] = H-1
    houses[H-1] += 1
    if houses[H-1] == 2:
      cnt += 1
  else:
    print(cnt)