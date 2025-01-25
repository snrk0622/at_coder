import itertools

N = int(input())
lengths = list(map(int, input().split()))

ans = 0
sticksCombinations = itertools.combinations(lengths, 3)
for sticks in sticksCombinations:
  if len(set(sticks)) != len(sticks): continue
  sortedSticks = sorted(sticks)
  # 三角形が成立条件：1辺の長さが他の2辺の和よりも小さい
  if sortedSticks[0] + sortedSticks[1] > sortedSticks[2]:
    ans += 1
print(ans)