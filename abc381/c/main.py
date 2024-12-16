N = int(input())
S = input()

# TLE
ans = 1
for i in range(N):
  if S[i] != '/': continue
  if i == 0 or i == N - 1: continue
  for j in range(1, min(i+1, N-i)):
    left = S[i-j:i]
    right = S[i+1:i+j+1]
    setted_left = set(left)
    setted_right = set(right)
    if '1' not in left or '2' not in right: continue
    setted_left.remove('1')
    setted_right.remove('2')
    if len(setted_left) > 0 or len(setted_right) > 0: continue
    ans = j * 2 + 1
print(ans)

# WA
# ans = 1
# i = 0
# while i < N:
#   if S[i] != '1':
#     i += 1
#   else:
#     one_cnt = 1
#     is_one = True
#     while is_one and i + one_cnt < N:
#       if S[i+one_cnt] == '1':
#         one_cnt += 1
#       else:
#         is_one = False
#     if S[i+one_cnt:i+one_cnt*2+1] == '/' + '2' * one_cnt:
#       ans = max(ans, one_cnt * 2 + 1)
#     i += one_cnt
# print(ans)