N, K = list(map(int, input().split()))
S = input()

ans = 0
cnt = 0
for i in range(len(S)):
  if S[i] == 'X':
    cnt = 0
  else:
    cnt += 1
    if cnt == K:
      ans += 1
      cnt = 0
print(ans)