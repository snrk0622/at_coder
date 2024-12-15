N, c1, c2 = list(input().split())
S = input()

print(''.join(list(map(lambda x: c1 if x == c1 else c2, S))))