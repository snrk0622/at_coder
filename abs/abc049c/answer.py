# 前から読むと
# dreamとdreamer
# eraseとeraserが被ってしまい判定が複雑になる

# 後ろから読むと被ることがなくなる！！！
# 後ろから考えると難易度が下がる問題は結構出る

S = input()
reversedS = S[::-1]

keys = ['eraser', 'erase', 'dreamer', 'dream']
reversedKeys = list(map(lambda x: x[::-1], keys))

can = True
i = 0
while i < len(reversedS):
  can2 = False # keysのいずれかでdevideできるか
  for key in reversedKeys:
    if reversedS[i:i+len(key)] == key:
      can2 = True
      i += len(key)
      break
  if not can2:
    can = False
    break

print('YES' if can else 'NO')