N = int(input())
A = list(map(int, input().split()))

dict = {}
ans = []
for i in range(1, N + 1):
  key = str(A[i - 1])
  if key in dict:
    ans.append(dict[key])
  else:
    ans.append(-1)
  dict[key] = i
print(*ans)