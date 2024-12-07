n = int(input())
tv = [tuple(map(int, input().split())) for _ in range(n)]

hum = 0
now = 0
for t, v in tv:
  hum = max(0, hum - t + now)
  hum += v
  now = t
print(hum)