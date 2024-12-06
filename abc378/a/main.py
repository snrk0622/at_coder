from collections import Counter

a = list(map(int, input().split()))
print(sum(list(map(lambda x: x // 2, list(dict(Counter(a)).values())))))