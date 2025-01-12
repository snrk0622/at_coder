N, D = map(int, input().split())
TL = [list(map(int, input().split())) for _ in range(N)]

for k in range(1, D+1):
  ans = 0
  for tl in TL:
    t, l = tl
    l += k
    ans = max(ans, t * l)
  print(ans)