# 年齢順を表すリスト（初期値[a, b, c]）を用意する
# それぞれの入力値を元に上記リストを並び替える

S = list(input().split())
ans = ['A', 'B', 'C']

for i in range(len(S)):
  if i == 0: # ab
    if S[i] == '>':
      ans[0], ans[1] = ans[1], ans[0]
  elif i == 1: # ac
    if S[i] == '>':
      ans[0], ans[2] = ans[2], ans[0]
  else: #bc
    if S[i] == '>':
      ans[1], ans[2] = ans[2], ans[1]
print(ans[1])
