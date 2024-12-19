N = int(input())
S = input()

ans = 1
for i in range(N):
  if S[i] != '/': continue
  for j in range(1, min(i+1, N-i)):
    left = S[i-j]
    right = S[i+j]
    if left == '1' and right == '2':
      ans = max(ans, j * 2 + 1)
    else:
      break
print(ans)