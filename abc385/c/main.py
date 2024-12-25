N = int(input())
H = list(map(int, input().split()))

count_dict = {}
for h in set(H):
  count_dict[h] = H.count(h)
sorted = sorted(count_dict.items(), key=lambda x: -x[1])

ans = 1
for h in list(map(lambda x: x[0], sorted)):
  idx_list = [i for i, value in enumerate(H) if value == h]
  if len(idx_list) <= ans: continue
  for i in range(len(idx_list) - 1):
    # if len(idx_list) - i <= ans: continue
    for j in range(1, len(idx_list) - i):
      # if len(idx_list) - (i + j) <= ans: continue
      temp = 2
      interval = idx_list[i+j] - idx_list[i]
      last_idx = idx_list[i+j]
      while True:
        if last_idx + interval in idx_list:
          temp += 1
          last_idx = last_idx + interval
        else:
          break
      ans = max(ans, temp)
print(ans)