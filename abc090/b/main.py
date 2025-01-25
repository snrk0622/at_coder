A, B = map(int, input().split())

ans = 0
for num in range(A, B+1):
  numStr = str(num)
  for i in range(len(numStr) // 2):
    if numStr[i] != numStr[-(i+1)]:
      break
  else:
    ans += 1
print(ans)