N = int(input())
QR = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
TD = [list(map(int, input().split())) for _ in range(Q)]

for i in range(Q):
  t, d = TD[i][0], TD[i][1]
  q, r = QR[t-1][0], QR[t-1][1]
  j = 1
  while r + (j - 1) * q < 1000000000:
    if d <= r + (j - 1) * q:
      print(r + (j - 1) * q)
      break
    j += 1