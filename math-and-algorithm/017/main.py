from collections import deque
N = int(input())
nums = deque(map(int, input().split()))

A = nums.popleft()
while len(nums):
  B = nums.popleft()
  divisor, divided = sorted([A, B])
  while divisor:
    divided, divisor = divisor, divided % divisor
  A = A // divided * B
print(A)