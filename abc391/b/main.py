N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(M)]

for sr in range(N):
  for sc in range(N):
    if S[sr][sc] == T[0][0]:
      cell = []
      for a in range(sr, sr + M):
        for b in range(sc, sc + M):
          if a >= N or b >= N: continue
          cell.append(S[a][b])
      if sum(T, []) == cell:
        print(sr+1, sc+1)