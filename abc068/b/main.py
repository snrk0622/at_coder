N = int(input())
ans = 0
max = 0
for i in range(1, N+1):
  num = i
  cnt = 0
  while num % 2 == 0:
    cnt += 1
    num /= 2
  if cnt >= max:
    ans = i
    max = cnt
print(ans)