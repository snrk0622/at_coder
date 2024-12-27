# TLE
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

def is_valid(x):
  nb = B[:] # Bコピー
  nb.append(x)
  nb.sort()
  return all(A[i] <= nb[i] for i in range(N))

if not is_valid(1 << 30):
  print(-1)
  exit()

# 二分探索
# 上限は十分に大きい値（1 << 30）
left, right = 0, 1 << 30

while left < right:
  mid = (left + right) // 2
  if is_valid(mid):
    right = mid
  else:
    left = mid + 1
print(left)