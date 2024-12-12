N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

i = 1
for j in range(N):
  i -= 1
  if i >= j:
    i = A[i][min(j, len(A[i]) - 1)]
  else:
    i = A[j][min(i, len(A[j]) - 1)]
print(i)