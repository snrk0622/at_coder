N = int(input())
S = input()

ans = 1
for i in range(N):
  if S[i] != '/': continue
  j = 1
  while True:
    if i-j < 0 or i+j >= N: break
    if S[i-j] != '1' or S[i+j] != '2': break
    j += 1
  ans = max(ans, 1 + 2 * (j - 1))
print(ans)