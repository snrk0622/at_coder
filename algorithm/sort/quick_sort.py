def quick_sort(A):
  # 分割できなくなるまで
  if len(A) <= 1:
    return A
  
  # pivot（基準値）は計算量を左右する重要な要素
  # 今回は単純にリストの先頭をpivotと設定
  pivot = A.pop(0)

  # pivotより小さいものでリスト
  left = [i for i in A if i <= pivot]
  # pivotより大きいものでリスト
  right = [i for i in A if i > pivot]

  left = quick_sort(left)
  right = quick_sort(right)

  return left + [pivot] + right