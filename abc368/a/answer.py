N, K = list(map(int, input().split()))
A = list(input().split())

top = A[:-K]
bottom = A[-K:]
ans = bottom + top
print(*ans)