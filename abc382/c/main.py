N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for b in B:
  for i in range(len(A)):
    if A[i] <= b:
      print(i + 1)
      break
  else:
    print(-1)
