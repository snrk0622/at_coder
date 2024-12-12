S = input()
T = input()

for i in range(max(len(S), len(T))):
  if len(S) <= i or len(T) <= i:
    print(i + 1)
    exit()
  if S[i] != T[i]:
    print(i + 1)
    exit()
print(0)