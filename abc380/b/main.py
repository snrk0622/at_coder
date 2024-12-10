S = input()

print(*list(map(lambda a: len(a), S[1:-1].split('|'))))