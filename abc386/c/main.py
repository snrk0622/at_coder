K = int(input())
S = input()
T = input()

if S == T:
  print('Yes')
  exit()

if len(T) - len(S) >= 2:
  print('No')
  exit()

elif len(T) - len(S) == 1: # 中の文字を1つ選び、削除する
  s, t = 0, 0
  diff = 0
  while s < len(S) and t < len(T):
    if S[s] != T[t]:
      diff += 1
      if diff > 1:
        print('No')
        exit()
      t += 1
    else:
      s += 1
      t += 1
  print('Yes')
elif len(T) - len(S) == 0: # S中の文字を1つ選び、別の1つの文字に変更する
  diff = 0
  for i in range(len(S)):
    if S[i] != T[i]: diff += 1
  print('YNeos'[diff > 1::2])
elif len(T) - len(S) == -1: # S中の(先頭や末尾を含む)任意の位置に、任意の文字を1つ挿入する
  s, t = 0, 0
  diff = 0
  while s < len(S) and t < len(T):
    if S[s] != T[t]:
      diff += 1
      if diff > 1:
        print('No')
        exit()
      s += 1
    else:
      s += 1
      t += 1
  print('Yes')
else:
  print('No')