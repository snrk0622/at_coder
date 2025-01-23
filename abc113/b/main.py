N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
ans = (0,10**8)
for i in range(N):
  temp = T - 0.006 * H[i]
  diff = abs(A - temp)
  if diff < ans[1]:
    ans = (i+1,diff)
print(ans[0])
