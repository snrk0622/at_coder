def binary_search(A, N, key):
  left = 0
  right = N
  while left < right:
    mid = (left + right) // 2
    if mid == key:
      return mid
    elif mid > key:
      right = mid
    else:
      left = mid + 1
  return -1