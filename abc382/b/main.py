N, D = list(map(int, input().split()))
S = list(input())

cnt = 0
for n in range(1, N + 1):
  if cnt >= D: break
  if S[-n] == '@':
    S[-n] = '.'
    cnt += 1
print(''.join(S))