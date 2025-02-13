divisor, divided = sorted(list(map(int, input().split())))
while divisor:
  divisor, divided = divided % divisor, divisor
print(divided)