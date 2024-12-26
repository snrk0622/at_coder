N, Q = map(int, input().split())

ans = 0
left, right = 1, 2
for _ in range(Q):
  h, t = input().split()
  t = int(t)
  if h == 'R':
    if right < left:
      if left < t:
        ans += right + (N - t)
      else:
        ans += abs(right - t)
    else:
      if left > t:
        ans += (N - right) + t
      else:
        ans += abs(right - t)
    right = t
  else:
    if left < right:
      if right < t:
        ans += left + (N - t)
      else:
        ans += abs(left - t)
    else:
      if right > t:
        ans += (N - left) + t
      else:
        ans += abs(left - t)
    left = t
print(ans)