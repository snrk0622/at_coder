S = input()
ans = 0
for i in range(len(S)):
  if S[i] != 'A': continue
  x = 1
  while True:
    bi = x + i
    ci = 2 * x + i
    if ci >= len(S): break
    if S[bi] == 'B' and S[ci] == 'C':
      ans += 1
    x += 1
print(ans)