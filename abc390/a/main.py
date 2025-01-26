As = list(map(int, input().split()))

diff = [0, 0, 0, 0, 0]
for i in range(5):
  if As[i] != i + 1:
    diff[i] = 1

diffIndexs = [n for n, v in enumerate(diff) if v == 1]
if len(diffIndexs) == 2 and diffIndexs[1] - diffIndexs[0] == 1:
  print('Yes')
else:
  print('No')