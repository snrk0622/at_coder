Q = int(input())

queue = []
delCnt = 0
delSum = 0
for _ in range(Q):
  inp = input().split()
  type = int(inp[0])
  if type == 1:
    l = int(inp[1])
    if len(queue) != 0:
      last = queue[-1]
      queue.append((last[0] + last[1], l))
    else:
      queue.append((0, l))
  elif type == 2:
    delSum += queue[delCnt][1]
    delCnt += 1
  else:
    k = int(inp[1])
    print(queue[k + delCnt -1][0] - delSum)
