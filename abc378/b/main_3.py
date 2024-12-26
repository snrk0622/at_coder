N = int(input())
QR = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())

for _ in range(Q):
  t, d = map(int, input().split())
  t -= 1
  q, r = QR[t]
  a = 0
  while True:
    if a * q + r >= d: break
    a += 1
  print(a * q + r)