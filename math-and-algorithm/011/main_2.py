import math
N = int(input())
prime_numbers = []
for i in range(2, N+1):
  is_prime_number = True
  for j in range(2, math.floor(math.sqrt(i)) + 1):
    if i % j == 0:
      is_prime_number = False
      break
  if is_prime_number: prime_numbers.append(i)
print(*prime_numbers)