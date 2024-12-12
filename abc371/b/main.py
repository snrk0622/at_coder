N, M = list(map(int, input().split()))
n = [0] * N

for i in range(M):
  A, B = input().split()
  print('YNeos'[n[int(A)-1] != 0 or B != 'M'::2])
  if B == 'M': n[int(A)-1] += 1
