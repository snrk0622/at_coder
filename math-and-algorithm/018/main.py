N = int(input())
nums = list(map(int, input().split()))

a, b, c, d = nums.count(100), nums.count(200), nums.count(300), nums.count(400)
print(a*d+b*c)