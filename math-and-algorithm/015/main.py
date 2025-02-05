divisor, divided = sorted(list(map(int, input().split())))
while divisor != 0:
  divided, divisor = divisor, divided % divisor
print(divided)