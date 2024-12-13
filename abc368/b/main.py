N = int(input())
A = list(map(int, input().split()))

ans = 0
while len(list(filter(lambda x: x > 0, A))) > 1:
  list.sort(A, reverse=True)
  A[0], A[1] = A[0] - 1, A[1] - 1
  ans += 1
print(ans)