A, B, C = list(map(int, input().split()))

# 起きる時間を基準にする
A = (A - C) % 24
B = (B - C) % 24

print('YNeos'[A > B::2])