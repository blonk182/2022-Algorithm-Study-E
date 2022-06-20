from itertools import permutations
from collections import deque

n = int(input())
num = list(map(int, input().split()))

cal = ['+', '-', '*', '//']

cal_input = list(map(int, input().split()))
cal_list = []

for i in range(4):
  if cal_input[i] == 0: # 특정 연산자가 존재하지 않는다면
    pass
  else: # 특정 연산자가 존재한다면 그 개수만큼 리스트에 추가
    for j in range(cal_input[i]): 
      cal_list.append(cal[i])

# 만들 수 있는 모든 연산자 배열의 경우의 수
num_case = list(permutations(cal_list, len(cal_list))) # 개수만큼 순서를 정해 나열
q = deque(num_case)

mx = -1e9
mn = 1e9

while q: # 큐가 빌 때까지
  now_list = q.popleft()
  result = num[0]
  for i in range(1, len(num)):
    if now_list[i-1] == '+':
      result += num[i]
    elif now_list[i-1] == '-':
      result -= num[i]
    elif now_list[i-1] == '*':
      result *= num[i]
    else:
      if result < 0:
        result = -(abs(result) // num[i])
      else:
        result = result // num[i]    
       
  mx = max(mx, result)
  mn = min(mn, result)

print(mx)
print(mn)