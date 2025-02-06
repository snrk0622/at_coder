from collections import deque
N = int(input())
nums = deque(map(int, input().split()))

A = nums.popleft()
while len(nums):
  B = nums.popleft()
  divisor, divided = sorted([A, B])
  while True:
    divided, divisor = divisor, divided % divisor
    if divisor == 0: break
  gcd = divided
  A = A // gcd * B
print(A)