N, S = map(int, input().split())
A = list(map(int, input().split()))

for i in range(2**N):
  num = 0
  for j in range(N):
    if i & (1 << (N - j - 1)):
      num += A[j]
  if num == S:
    print('Yes')
    exit()
print('No')