import math
X = int(input())

ans = 2
while True:
  if math.factorial(ans) == X:
    break
  else:
    ans += 1
print(ans)