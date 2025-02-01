N = int(input())
ans = []
for i in range(2, N+1):
  isPrimeNumber = True
  for j in range(2, i):
    if i % j == 0:
      isPrimeNumber = False
  if isPrimeNumber:
    ans.append(i)
print(*ans)