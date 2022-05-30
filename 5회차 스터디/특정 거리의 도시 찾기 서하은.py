from collections import deque
# n : 도시의 개수
# m : 도로의 개수
# k : 거리 정보
# x : 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)] # 0번째 칸은 빈칸

for _ in range(m):
    a, b = map(int, input().split()) # a에서 b로 이동하는 도로
    graph[a].append(b)

# 도시에 대한 최단 거리
distance = [-1] * (n+1) # 최단 거리 초기화
distance[x] = 0 # 출발 도시까지의 거리는 0

q = deque([x])
while q: # q가 빌 때까지
    now = q.popleft()
    for next_node in graph[now]: # 이동할 수 있는 모든 도시 확인
        if distance[next_node] == -1: # 방문하지 않은 도시라면
            distance[next_node] = distance[now] + 1 # 출발 도시에서 현재 도시까지의 거리 + 1, 최단 거리
            q.append(next_node)

check = False # 초기화

for i in range(1, n+1): 
    if distance[i] == k: # 최단거리가 k인 도시 번호
        print(i)
        check = True

if check == False: # 최단 거리가 k인 도시가 없다면
    print(-1)





    '''
from collections import deque
import sys
f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(x)
'''