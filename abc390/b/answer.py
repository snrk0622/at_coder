n = int(input())
a = list(map(int, input().split()))

r = a[1]/a[0]

for i in range(1, n):
  if a[0]*a[i] == a[1]*a[i-1]:
    continue
  else:
    print('No')
    exit()
print('Yes')