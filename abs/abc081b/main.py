N = int(input())
A = list(map(int, input().split()))

def isAllEven(list):
  for num in list:
    if num % 2 != 0:
      return False
  return True

ans = 0
copiedA = [*A]
while isAllEven(copiedA):
  ans += 1
  copiedA = list(map(lambda x: x // 2, copiedA))
print(ans)