D = input()
ans = ''

for d in D:
  if d == 'N':
    ans += 'S'
  elif d == 'E':
    ans += 'W'
  elif d == 'W':
    ans += 'E'
  else:
    ans += 'N'
print(ans)