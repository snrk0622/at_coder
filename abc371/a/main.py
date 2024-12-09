AB, AC, BC = list(input().split())

if AB == AC == BC:
  print('B')
elif AB == AC:
  print('C')
else:
  print('A')