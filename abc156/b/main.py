N, K = map(int, input().split())

# K進数に変換した時の桁数
# = 「NをKで何回割れるか」と読み替え可能
ans = 0
quotient = N
while quotient != 0:
  quotient = quotient // K
  ans += 1
print(ans)