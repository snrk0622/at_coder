import bisect

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 単調増加に変換
fmt_a = [0] * N
fmt_a[0] = -A[0]
for i in range(1, N):
  fmt_a[i] = max(fmt_a[i-1], -A[i])

# 二分探索
for b in B:
  idx = bisect.bisect_left(fmt_a, -b)
  print(idx + 1 if idx < N else -1)
