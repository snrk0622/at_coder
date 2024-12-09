A, B = list(map(int, input().split()))

# A, Bが同じ場合
if A == B:
  print(1)
  exit()

# 2つは確定
# x, A, B / A, B, x
ans = 2

# A, x, B
if (A + B) % 2 == 0:
  ans += 1

print(ans)