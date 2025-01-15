S = input()
keys = ['eraser', 'erase', 'dreamer', 'dream']

T = ''
while len(T) < len(S):
  found = False
  for key in keys:
    if S[len(T):len(T)+len(key)] == key:
      T += key
      found = True
  if not found: break
  

print('YNEOS'[S != T::2])