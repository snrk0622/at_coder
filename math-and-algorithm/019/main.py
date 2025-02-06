import math
N = int(input())
cards = list(map(int, input().split()))

ans = 0
for i in range(1, 4):
  n = cards.count(i)
  if n >= 2:
    ans += math.factorial(n) // (math.factorial(2) * math.factorial(n - 2))
print(ans)