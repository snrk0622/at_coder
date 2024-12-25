array = list(map(int, input().split()))

if len(set(array)) <= 1:
  print('Yes')
else:
  sorted = sorted(array)
  print('YNeos'[sorted[0]+sorted[1]!=sorted[2]::2])