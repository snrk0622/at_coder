N, K = map(int, input().split())
L = list(map(int, input().split()))
print(sum(sorted(L, reverse=True)[0:K]))