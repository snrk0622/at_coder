N = int(input())
chars = sorted([ input() for _ in range(N)], key=len)
print(''.join(chars))