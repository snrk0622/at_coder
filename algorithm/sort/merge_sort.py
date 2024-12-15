def merge(left, right):
  result = []
  i, j = 0, 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  
  # 残りをまとめてマージ
  if i < len(left):
    result.extend(left[i:])
  if j < len(right):
    result.extend(right[j:])

  return result

def merge_sort(A, N):
  if N <= 1:
    return A
  
  mid = N // 2
  left = merge_sort(A[:mid])
  right = merge_sort(A[mid:])
  return merge(left, right)