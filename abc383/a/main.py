# AC
# https://atcoder.jp/contests/abc383/submissions/60514787

n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]

hum = 0
for i in range(len(t)):
  if hum > 0:
    diff = t[i][0] - t[i - 1][0] 
    if hum <= diff:
      hum = 0
    else:
      hum -= diff
  
  hum += t[i][1]

print(str(hum))