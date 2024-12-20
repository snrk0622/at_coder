N = int(input())
qr = [tuple(map(int, input().split())) for _ in range(N)]

Q = int(input())
for _ in range(Q):
  t, d = list(map(int, input().split()))
  t -= 1
  q, r = qr[t][0], qr[t][1]
  j = 0
  b, c = divmod(d, q)
  a = b if c == r else b + 1
  print(a * q + r)