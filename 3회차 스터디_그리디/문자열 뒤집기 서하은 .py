n = input() # 문자얼 입력받음

s = n[0] # s,t에 0,1 담기
if s == 1: t = 0
else: t = 1

sn = 0 # 0 or 1을 뒤집을 떄 행동 횟수
tn = 0 # 0 or 1을 뒤집을 때 행동 횟수

for i in range(len(n)-1): # 마지막 문자 제외
    if n[i] == n[i+1]: pass
    else: # 연속된 숫자가 다를 경우
        if n[i] == s: sn += 1
        else: tn += 1

if n[-1] == s: sn += 1 # 마지막 문자
else: tn += 1

print(min(sn, tn)) # 최소 횟수