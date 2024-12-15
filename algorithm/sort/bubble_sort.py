def bubble_sort(A, N):
  for i in range(N-1):
    for j in range(N-i):
      if A[j] > A[j+1]:
        A[j], A[j+1] = A[j+1], A[j]