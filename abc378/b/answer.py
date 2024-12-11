N = int(input())
QR = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())

for _ in range(Q):
  t, d = map(int, input().split())
  t -= 1
  q, r = QR[t][0], QR[t][1]
  b, c = divmod(d, q)
  a = b if c <= r[t] else b + 1
  ans = a * q[t] + r[t]
  print(ans)