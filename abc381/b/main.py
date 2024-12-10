S = input()

if len(S) % 2 != 0:
  print("No")
  exit()

for s in set(S):
  if S.count(s) != 2:
    print("No")
    exit()

for i in range(1, len(S) // 2 + 1):
  if S[(2*i-1)-1] != S[(2*i)-1]:
    print("No")
    exit()

print("Yes")