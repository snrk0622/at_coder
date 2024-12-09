n = 12
S = [input() for _ in range(n)]

ans = 0
for i in range(n):
  if len(S[i]) == i+1:
    ans += 1
print(ans)