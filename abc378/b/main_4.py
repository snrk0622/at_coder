N = int(input())
QR = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())

for _ in range(Q):
  t, d = map(int, input().split())
  t -= 1
  q, r = QR[t][0], QR[t][1]
  b, c = divmod(d, q)
  a = b if c <= r else b + 1
  print(a * q + r)