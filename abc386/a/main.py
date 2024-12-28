cards = list(map(int, input().split()))

cards_set = set(cards)
if len(cards_set) != 2:
  print('No')
else:
  print('Yes')