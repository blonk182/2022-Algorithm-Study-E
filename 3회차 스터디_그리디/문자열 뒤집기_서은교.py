s = input()
result = [0]*2
now = int(s[0])

for i in s:
  num = int(i)
  if now == num:
    continue
  else:
    result[num] += 1
    now = num

print(min(result[0], result[1]))
