n, c = list(map(int, input().split()))
T = list(map(int, input().split()))

now = T[0]
candy = 1
for i in range(1, n):
  if T[i] - now >= c:
    candy += 1
    now = T[i]
print(candy)