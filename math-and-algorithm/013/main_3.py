import math
N = int(input())
divisors = []
for i in range(1, math.floor(math.sqrt(N)) + 1):
  if N % i == 0:
    divisors.append(i)
    divisors.append(N // i)

for divisor in sorted(divisors):
  print(divisor)