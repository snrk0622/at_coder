def selection_sort(A, N):
  for i in range(N-1):
    minj = i
    for j in range(i+1, N):
      if A[j] < minj:
        minj = j
    A[i], A[minj] = A[minj], A[i]