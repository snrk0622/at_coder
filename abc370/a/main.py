L,R = list(map(int, input().split()))

if L+R == 1:
  print('YNeos'[R::2])
else:
  print('Invalid')
