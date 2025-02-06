N = int(input())
cards = list(map(int, input().split()))

cnt = 0
for i in range(1, 4):
  n = cards.count(i)
  if n < 2: continue
  cnt += n * (n - 1) // 2
print(cnt)