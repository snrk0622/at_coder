Y = int(input())

ans = 365
if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0:
  ans = 366
print(ans)