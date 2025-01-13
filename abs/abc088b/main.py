N = int(input())
A = list(map(int, input().split()))

sortedA = sorted(A, reverse=True)
alice = sortedA[::2]
bob = sortedA[1::2]
print(sum(alice)- sum(bob))