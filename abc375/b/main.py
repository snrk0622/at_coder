from decimal import *

N = int(input())

ans = 0
now = [0, 0]
for i in range(N):
  next = list(map(int, input().split()))
  ans += ((now[0]-next[0])**2 + (now[1]-next[1])**2)**Decimal('0.5')
  now = next
ans += (next[0]**2 + next[1]**2)**Decimal('0.5')
print(ans)