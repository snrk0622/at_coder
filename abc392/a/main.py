nums = list(map(int, input().split()))
sorted_nums = sorted(nums)
if sorted_nums[0] * sorted_nums[1] == sorted_nums[2]:
  print('Yes')
else:
  print('No')