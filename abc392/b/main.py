N, M = map(int, input().split())
nums = list(map(int, input().split()))

ans = []
for i in range(1, N+1):
  if i not in nums:
    ans.append(i)
print(len(ans))
print(*ans)