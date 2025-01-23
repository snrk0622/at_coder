s = input()
reversedS = s[::-1]
firstA = s.index('A')
lastZ = len(s) - reversedS.index('Z')
print(lastZ - firstA)