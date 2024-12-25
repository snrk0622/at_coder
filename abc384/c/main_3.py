score = list(map(int, input().split()))

scores = []
for bit in range(1, 32):
  name = ''
  sum = 0
  for digit in range(5):
    if bit & 1 << digit:
      name += 'ABCDE'[digit]
      sum += score[digit]
  scores.append({
    'name': name,
    'score': sum
  })

sorted_scores = sorted(
  scores,
  key=lambda x: (-x['score'], x['name'])
)

for score in sorted_scores:
  print(score['name'])