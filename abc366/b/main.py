N = int(input())
S = [list(input()) for _ in range(N)]
max_len = max(list(map(lambda x: len(x), S)))

ans = []
for i in range(max_len):
  ans.append([])
  for j in range(N):
    if len(S[N-j-1]) > i:
      ans[i].append(S[N-j-1][i])
    else:
      ans[i].append('*')
  while ans[i][-1] == '*':
    ans[i] = ans[i][:-1]
  print(''.join(ans[i]))