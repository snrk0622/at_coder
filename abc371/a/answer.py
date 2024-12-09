ab, ac, bc = list(input().split())

# 1. abとacが違う場合：aが次男
# 2. 1を満たさずabとbcが同じ場合：bが次男
# 3. 1/2を満たさない場合：cが次男

if ab != ac:
  print('A')
elif ab == bc:
  print('B')
else:
  print('C')