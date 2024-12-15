import bisect
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Aを単調増加のリストにする（二分探索するため）
# bisectで降順のリストを扱うためには、各要素を負に反転する必要がある
reversed_a = [0] * N
reversed_a[0] = -A[0]
for i in range(1, N):
  reversed_a[i] = max(reversed_a[i - 1], -A[i])

# それぞれの寿司に対して二分探索
for b in B:
  idx = bisect.bisect_left(reversed_a, -b)
  print(idx + 1 if idx < N else -1)