import math
N = int(input())
factors = []

while True:
  for i in range(2, math.floor(math.sqrt(N)) + 1):
    if N % i == 0:
      factors.append(i)
      N = N // i
      break
  else:
    factors.append(N)
    break
print(*factors)