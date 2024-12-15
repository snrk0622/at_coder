N, R = list(map(int, input().split()))

ans = R
for i in range(N):
  D, A = list(map(int, input().split()))
  if D == 1:
    if 1600 <= ans and ans <= 2799:
      ans += A
    else:
      continue
  elif D ==2:
    if 1200 <= ans and ans <= 2399:
      ans += A
    else:
      continue
print(ans)