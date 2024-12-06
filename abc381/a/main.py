n = int(input())
s = input()

if n == 0:
  print('Yes')
elif n % 2 == 0:
  print('No')
elif len(s.split('/')) != 2:
  print('No')
else:
  l, r = s.split('/')
  if len(l) == len(r):
    if '2' in l or '1' in r:
      print('No')
      exit()
    print('Yes')
  else:
    print('No')