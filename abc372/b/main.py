M = int(input())

A = []

# Mを3の倍数にする
while (M - sum(list(map(lambda x: 3**x, A)))) % 3 != 0:
  A.append(0)

while sum(list(map(lambda x: 3**x, A))) < M:
  remaining = M - sum(list(map(lambda x: 3**x, A)))
  for i in sorted(range(1, 11), reverse=True):
    if 3**(i) <= remaining:
      A.append(i)
      break
print(len(A))
print(*A)