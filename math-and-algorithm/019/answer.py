N = int(input())
cards = list(map(int, input().split()))

ans = 0
for i in range(1, 4):
  n = cards.count(i)
  if n >= 2:
    ans += n*(n-1) // 2 # nC2ならmath.factorial使わないでできる（その方が高速）
print(ans)