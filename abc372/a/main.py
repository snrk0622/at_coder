S = list(input())

while '.' in S:
  S.remove('.')
print(''.join(S))