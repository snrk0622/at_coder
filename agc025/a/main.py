from functools import reduce

N = int(input())

def calcDigitSum(num):
  digits = [int(i) for i in str(num)]
  sum = reduce(lambda acc, num: acc + num, digits, 0)
  return sum

minSum = N
for i in range(1, N // 2 + 1):
  minSum = min(calcDigitSum(i) + calcDigitSum(N - i), minSum)

print(minSum)