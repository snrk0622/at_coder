N, X = map(int, input().split())
A = list(map(int, input().split()))

sortedA = sorted(A)

ans = 0
x = X
# 求めている個数が少ない方から
for a in sortedA:
  # お菓子が残っているうちは
  afterX = x - a
  if afterX >= 0:
    # 「配る」
    ans += 1
    x = afterX
  # 足りなくなったら終わり
  else:
    break
print(ans if x == 0 or ans < N else max(0, ans - 1))