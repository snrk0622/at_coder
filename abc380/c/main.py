import re

N, K = list(map(int, input().split()))
S = input()

partition_s = re.findall(r'0+|1+', S)
if S[0] == '0':
  t = K * 2 - 1
else:
  t = K * 2 - 2
partition_s[t - 1], partition_s[t] = partition_s[t], partition_s[t - 1]
print(''.join(partition_s))