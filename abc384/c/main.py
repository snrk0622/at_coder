import itertools

keys = ['A', 'B', 'C', 'D', 'E']
values = list(map(int, input().split()))
problems = dict(zip(keys, values))

combinations = []
for n in range(len(problems.keys())):
  combinations.append(itertools.combinations(problems.keys(), n + 1))
combinations = list(itertools.chain.from_iterable(combinations))

scores = []
for combi in combinations:
  score = 0
  for i in list(combi):
    score += problems[i]
  scores.append({
    'key': ''.join(combi),
    'score': score
  })

sorted_scores = sorted(
  scores,
  key = lambda x: (-x['score'], x['key']),
)

for score in sorted_scores:
  print(score['key'])