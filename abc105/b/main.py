N = int(input())

cake = 4
donut = 7

for c in range(N // cake + 1):
  for d in range(N // donut + 1):
    if c * cake + d * donut == N:
      print('Yes')
      exit()
print('No')