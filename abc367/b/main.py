X = input()

integer_part = X.split('.')[0]
fractional_part = X.split('.')[1]

print(float(X) if int(fractional_part) != 0 else integer_part)