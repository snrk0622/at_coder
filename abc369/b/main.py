N = int(input())

hands = {
  'L': 0,
  'R': 0,
}
ans = 0
for i in range(N):
  A, S = list(input().split())
  A = int(A)
  if hands[S] != 0:
    ans += abs(hands[S] - A)
  hands[S] = A
print(ans)