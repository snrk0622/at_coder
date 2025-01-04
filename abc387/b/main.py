X = int(input())

ans = []
for i in range(1, 10):
  for j in range(1, 10):
    if X != i*j:
      ans.append(i*j)
print(sum(ans))