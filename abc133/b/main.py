import itertools
import math

N, D = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]

ans = 0
pointsCombinations = list(itertools.combinations(points, 2))
for combi in pointsCombinations:
  squaredAbsSum = 0
  for i in range(D):
    squaredAbsSum += abs(combi[0][i] - combi[1][i])**2
  if math.sqrt(squaredAbsSum)%1 == 0:
    ans += 1
print(ans)