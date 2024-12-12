S = input()
sorted = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = 0
pre = S.index('A')
for i in range(len(sorted)):
  idx = S.index(sorted[i])
  ans += abs(idx - pre)
  pre = idx
print(ans)