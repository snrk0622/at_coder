H, W, D = list(map(int, input().split()))
S = [list(input()) for _ in range(H)]

ans = 0
# 加湿器１(i1, j1)
for i1 in range(H):
  for j1 in range(W):
    # 加湿器２(i2, j2)
    for i2 in range(H):
      for j2 in range(W):
        if i1 == i2 and j1 == j2: continue
        if S[i1][j1] == '#' or S[i2][j2] == '#': continue
        # それぞれのマス(i, j)が加湿対象かチェック
        h = 0
        for i in range(H):
          for j in range(W):
            if S[i][j] == '#': continue
            if (i == i1 and j == j1) or (i == i2 and j == j2): 
              h += 1
              continue
            if abs(i - i1) + abs(j - j1) <= D:
              h += 1
              continue
            if abs(i - i2) + abs(j - j2) <= D:
              h += 1
              continue
        ans = max(ans, h)
print(ans)
