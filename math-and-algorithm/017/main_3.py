from collections import deque
N = int(input())
nums = deque(map(int, input().split()))
A = nums.popleft()
while len(nums):
  B = nums.popleft()
  divisor, divided = sorted([A, B])
  while divisor:
    divisor, divided = divided % divisor, divisor
  A = (A * B) // divided
print(A)