N, A, B = map(int, input().split())

ans = 0
for num in range(1, N+1):
  sumNum = sum(map(int, str(num)))
  if A <= sumNum and sumNum <= B: ans += num
print(ans)