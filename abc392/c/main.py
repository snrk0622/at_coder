N = int(input())
persons = list(map(int, input().split()))
zekkens = list(map(int, input().split()))

zekken_index_dict = {zekkens[i]: i for i in range(N)}

ans = []
for i in range(1, N+1):
  person = zekken_index_dict[i]
  looking = persons[person]
  zekken = zekkens[looking-1]
  ans.append(zekken)
print(*ans)