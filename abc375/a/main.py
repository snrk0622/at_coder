N = int(input())
S = input()

ans = 0
for i in range(0, N - 2):
  if S[i:i+3] == '#.#':
    ans += 1
print(ans)