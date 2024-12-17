scores = list(map(int, input().split()))

standings = []
for i in range(1, 32):
  score = 0
  name = ''
  for j in range(len(scores)):
    if i & 1 << j:
      score += scores[j]
      name += 'ABCDE'[j]
  standings.append((score, name))

for _, name in sorted(standings, key=lambda x: (-x[0], x[1])):
  print(name)