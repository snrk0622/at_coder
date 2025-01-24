N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]

# N 種類のドーナツそれぞれを少なくとも1個は作る
ans = len(M)
X -= sum(M)

# 残りは最も少ない材料で作れるドーナツを作れるだけ作る
ans += X // min(M)

print(ans)