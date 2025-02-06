N = int(input())
products = list(map(int, input().split()))

a, b, c, d = products.count(100), products.count(200), products.count(300), products.count(400)
print(a * d + b * c)