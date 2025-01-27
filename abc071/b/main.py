S = input()

for ascii in range(97, 123):
  if not chr(ascii) in S:
    print(chr(ascii))
    exit()
print('None')