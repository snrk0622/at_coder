# 1つWA

import math

N = int(input())
AList = list(map(int, input().split()))
genAList = []

a1 = AList[0]
r = AList[1] / a1
for i in range(N):
  if i == 0: continue
  if not math.isclose(AList[i] / AList[i-1], r):
    print('No')
    exit()
print('Yes')