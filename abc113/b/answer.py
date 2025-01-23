N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
t = []
for h in H:
  t.append(abs(A - (T - 0.006 * h)))
print(t.index(min(t))+1)