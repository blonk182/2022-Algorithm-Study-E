from contextlib import nullcontext


s = [i for i in input()]
length = len(s)
flag = 0
j = 0
while True:
    if j == length-1:
        break
    if s[j+1] == s[flag]:
        s[j+1] = -1
        j += 1
    else:   # 숫자가 바뀌면 flag 위치 갱신
        flag = j+1
        j += 1
print(min(s.count('0'), s.count('1')))
