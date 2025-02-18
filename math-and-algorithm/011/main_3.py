import math
N = int(input())
ans = []
for i in range(2,N+1):
  for j in range(2, i):
    if i % j == 0: break
  else:
    ans.append(i)
print(*ans)