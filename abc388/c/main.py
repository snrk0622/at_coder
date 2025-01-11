import bisect
N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(len(A)):
  a = A[i]
  b = a*2
  cnt = len(A) - bisect.bisect_left(A, b)
  ans += cnt
print(ans)  