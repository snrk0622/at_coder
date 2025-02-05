A, B = map(int, input().split())
divisor, divided = sorted([A, B])
while divisor:
  divided, divisor = divisor, divided % divisor
print(divided)