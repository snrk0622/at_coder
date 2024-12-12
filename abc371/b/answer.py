N, M = list(map(int, input().split()))
taro_exist = [False] * N

for i in range(M):
  A, B = input().split()
  if B == 'M' and not taro_exist[int(A) - 1]:
    taro_exist[int(A) - 1] = True
    print('Yes')
  else:
    print('No')
