D = input()
ans = ''
if D == 'N':
  ans = 'S'
elif D == 'E':
  ans = 'W'
elif D == 'W':
  ans = 'E'
elif D == 'S':
  ans = 'N'
elif D == 'NE':
  ans = 'SW'
elif D == 'NW':
  ans = 'SE'
elif D == 'SE':
  ans = 'NW'
else:
  ans = 'NE'
print(ans)