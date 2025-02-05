# 双方向キュー
from collections import deque

# 先頭からの削除方法
# listのpop -> O(N)
# dequeのpopleft -> O(1)

N = int(input())
nums = deque(map(int, input().split()))
A = nums.popleft()
while len(nums):
  B = nums.popleft()
  divisor, divided = sorted([A, B])
  while divisor:
    divided, divisor = divisor, divided % divisor
  A = divided
print(A)