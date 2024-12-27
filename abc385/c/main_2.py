N = int(input())
H = list(map(int, input().split()))

ans = 0
for i in range(N):
  for step in range(1, N - i):
    cnt = 1
    while i + step * cnt < N:
      if H[i] != H[i + step * cnt]: break
      ans = max(ans, cnt)
      cnt += 1
print(ans + 1)