H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

blackSeq = []
for h in range(H):
  blackSeq.append([])
  seq = []
  for w in range(W):
    cell = S[h][w]
    if cell != '.':
      seq.append(w)
    else:
      if len(seq) != 0:
        blackSeq[h].append(seq)
        seq = []

# このやり方ダメだ
# そもそも要件間違えてた