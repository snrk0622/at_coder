N = int(input())
H = list(map(int, input().split()))

ans = 1

for i in range(N):
  for w in range(1, N-1):
    cnt = 1
    while i + cnt * w < N and H[i] == H[i + cnt * w]:
      cnt += 1
    ans = max(ans, cnt)
print(ans)