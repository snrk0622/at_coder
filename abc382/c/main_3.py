import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

minus_A = list(map(lambda x: -x, A))
formatted_A = [0] * N
formatted_A[0] = minus_A[0]
for i in range(1, N):
  if minus_A[i] < formatted_A[i-1]:
    formatted_A[i] = formatted_A[i-1]
  else:
    formatted_A[i] = minus_A[i]

for b in B:
  idx = bisect.bisect_left(formatted_A, -b)
  print(idx + 1 if idx < N else -1)