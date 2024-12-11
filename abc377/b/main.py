S = [list(input()) for _ in range(8)]

ans = 0
for i in range(len(S)):
  for j in range(len(S[i])):
    if S[i][j] == '#': continue
    if '#' in S[i] or '#' in list(map(lambda x: x[j], S)): continue
    ans += 1
print(ans)
