H, W, D =   list(map(int, input().split()))
S = [list(input()) for _ in range(H)]

ans = 0

# 1つ目の加湿器が置かれるマス(i1, j1)
for i1 in range(H):
  for j1 in range(W):
    if S[i1][j1] == '#': continue
    # 2つ目の加湿器が置かれるマス(i2, j2)
    for i2 in range(H):
      for j2 in range(W):
        if S[i2][j2] == '#': continue
        if i1 == i2 and j1 == j2: continue
        cnt = 0
        # 上記の(i1, j1), (i2, j2)の置き方をされた時
        # それぞれのマスについて加湿されているかを調べる
        for i in range(H):
          for j in range(W):
            if S[i][j] == '#': continue
            humid = False
            # 1つ目の加湿器で加湿されるか
            if abs(i - i1) + abs(j - j1) <= D: humid = True
            # 2つ目の加湿器で加湿されるか
            if abs(i - i2) + abs(j - j2) <= D: humid = True
            if humid: cnt += 1
        ans = max(ans, cnt)
print(ans)

