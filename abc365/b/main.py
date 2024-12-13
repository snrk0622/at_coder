N = int(input())
A = list(map(int, input().split()))

sorted_a = sorted(A, reverse=True)
print(A.index(sorted_a[1]) + 1)