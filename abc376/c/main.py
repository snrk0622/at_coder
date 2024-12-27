# TLE
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

desc_a = sorted(A, reverse=True)
desc_b = sorted(B, reverse=True)

left_a = []
while len(left_a) <= 1 and len(desc_a) > 0 and len(desc_b) > 0:
  if desc_a[0] <= desc_b[0]:
    desc_a.pop(0)
    desc_b.pop(0)
  else:
    left_a.append(desc_a.pop(0))

if len(left_a) > 1:
  print(-1)
else:
  print(left_a[0])