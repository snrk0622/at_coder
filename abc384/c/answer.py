points = list(map(int, input().split()))

standings = []
for bit in range(1, 32):
  solved_point = 0
  name = ''
  for digit in range(5):
    # それぞれの桁ビットが立っている（1かどうか）か調べる
    if bit & (1 << digit):
      solved_point += points[digit]
      name += 'ABCDE'[digit]
  standings.append({
    'name': name,
    'solved_point': solved_point
  })

sorted_standings = sorted(
  standings,
  key = lambda x: (-x['solved_point'], x['name'])
)

for standing in sorted_standings:
  print(standing['name'])
