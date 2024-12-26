N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]

avoids = []
attacks = [
  (2, 1),
  (1, 2),
  (-1, 2),
  (-2, 1),
  (-2, -1),
  (-1, -2),
  (1, -2),
  (2, -1)
]
for i in range(M):
  a, b = AB[i]
  avoids.append((a, b))
  for attack in attacks:
    move_a, move_b = a + attack[0], b + attack[1]
    if move_a <= 0 or move_a > N or move_b <= 0 or move_b > N: continue
    avoids.append((move_a, move_b))
print(N**2 - len(set(avoids)))