X = input()

while X[-1] == '0':
  X = X[:-1]
if X[-1] == '.':
  X = X[:-1]
print(X)