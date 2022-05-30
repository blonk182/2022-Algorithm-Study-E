import collections
from copy import copy


import copy
import sys
from urllib.parse import parse_qsl

sys.stdin=open("ex1.txt", 'r')

lab = [ [0 for _ in range(8)] for _ in range(8) ]
labcopy = [ [0 for _ in range(8)] for _ in range(8) ]
orginal_virus_index = collections.deque()

answer= 0
clean_cnt=0

def init_lab_copy():            #연구소 복제본 초기화 함수
    global labcopy      
    for r in range(N):
        for c in range(M):
            labcopy[r][c] = lab[r][c]

def spread_virus():
    global answer
    q_virus = copy.deepcopy(orginal_virus_index)
    result_lab = copy.deepcopy(labcopy)
    dr= [1, -1, 0, 0 ]
    dc = [0, 0, 1, 1]
    while q_virus:          #bfs
        r,c = q_virus.popleft()
        for i in range(4):
            nr= r + dr[i]
            nc= c + dr[i]
            if nr<0 or nr>= N or nc<0 or nc>= M:
                continue
            if result_lab[nr][nc] != 0:
                continue
            result_lab[nr][nc] = 1
            virus_cnt +=1
            q_virus.append( (nr,nc))
    res = clean_cnt - virus_cnt - 3
    answer = max(answer, res)

def build_wall(row,col,wall_cnt):
    if wall_cnt == 3:       #벽 3개 세워지면 
        spread_virus()      #확산시작
        return
    for r in range(row, N):
        for c in range(0,M):
            if labcopy[r][c] != 0:
                continue
            labcopy[r][c] = 1
            build_wall(r,c,wall_cnt+1)
            labcopy[r][c] = 0


def solve():
    for r in range(N):
        for c in range(M):
            if lab[r][c] != 0:
                continue
            init_lab_copy() #벽을 세울곳을 찾으면 연구소 복제해서 사용
            labcopy [r][c] = 1     #벽은 첫번 째 벽을 전수로 세우고
            build_wall(r,c,1)            #2,3번째 벽은 재귀로 호출
            labcopy[r][c] =0       #첫번째 벽은 바로 안전상태로 복귀


N,M = map(input().split())

for r in range(N):
    input= list(map(int, input().split()))
    for c in range(M) :
        lab[r][c] = input[c]                    #input값을 2차원배열로 저장(연구소의 형태) 
        if lab[r][c]  == 1:
            clean_cnt+=1
        if lab[r][c]  == 2:
            orginal_virus_index.append( (r,c) ) #행,열 묶어서 원래 바이러스위치 저장
solve()