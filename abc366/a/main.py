N, T, A = list(map(int, input().split()))

print('YNeos'[T <= N//2 and A <= N//2::2])