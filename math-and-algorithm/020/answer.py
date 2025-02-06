import math
N = int(input())
cards = list(map(int, input().split()))

ans = 0
cards_len = len(cards)
for a in range(cards_len):
  for b in range(a+1, cards_len):
    for c in range(b+1, cards_len):
      for d in range(c+1, cards_len):
        for e in range(d+1, cards_len):
          if cards[a] + cards[b] + cards[c] + cards[d] + cards[e] == 1000: ans += 1
print(ans)