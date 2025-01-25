N = int(input())
A = list(map(int, input().split()))
print(sum(sorted(A)[-2::-2][:N]))