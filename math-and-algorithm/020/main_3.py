N = int(input())
nums = list(map(int, input().split()))
ans = 0
for a in range(N):
  for b in range(a+1, N):
    for c in range(b+1, N):
      for d in range(c+1, N):
        for e in range(d+1, N):
          if nums[a] + nums[b] + nums[c] + nums[d] + nums[e] == 1000:
            ans += 1
print(ans)