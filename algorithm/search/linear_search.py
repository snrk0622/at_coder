def linear_search(A, N, key):
  i = 0
  A[N] = key # 番兵
  while A[i] != key: i += 1
  if i == N:
    return -1
  else:
    return i