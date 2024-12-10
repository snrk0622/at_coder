A, B, C = list(map(int, input().split()))

# 日付を跨ぐ場合
if B > C:
  A, C = A+24, C+24
  
print('YNeos'[A in range(B, C)::2])