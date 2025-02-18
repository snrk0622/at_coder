N = int(input())
nums = list(map(int, input().split()))

ans = 0
for a in range(1, 4):
  cnt = nums.count(a)
  ans += (cnt * (cnt - 1)) // 2
print(ans)