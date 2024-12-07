# WA
# https://atcoder.jp/contests/abc383/submissions/60540681

h, w, d = list(map(int, input().split()))
s_array = [list(input()) for _ in range(h)]

hum_array = []

for i in range(len(s_array)):
  for j in range(len(s_array[i])):
    if (s_array[i][j] == '#'):
        continue
    target_square = map(lambda row_i: s_array[row_i][max(0, j - d + abs(row_i - i)):min(w, j + d - abs(row_i - i)) + 1], range(len(s_array[max(0, i - d):min(h, i + d) + 1])))
    hum_array.append(sum(target_square, []).count('.'))

print(str(sum(sorted(hum_array)[-2:])))