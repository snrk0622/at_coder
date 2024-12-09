N, K = list(map(int, input().split()))
A = list(input().split())

ans = A[-K:]
ans.extend(A[:N-K])
print(' '.join(ans))