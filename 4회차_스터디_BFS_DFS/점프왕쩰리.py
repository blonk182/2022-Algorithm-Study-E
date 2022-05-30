from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 방문 유무 확인
visited = [[False]*3 for _ in range(N)]

# 오른쪽만 가능
dx = [1,0]

# 아래만 가능
dy = [0,1]

def bfs(x, y):
  
  q = deque()
  q.append([x,y])
  

  while q:
    x, y = q.popleft()
    # 쪨리가 현재 밟고 있는 칸의 숫자를 인출
    step = graph[x][y]

    # 끝점이 -1이므로 -1로 도달하면 성공
    if graph[x][y] == -1:
      return True
    for move in range(2):
      # 쩰리가 현재 밟고 있는 숫자를 인출하고 이동수에 곱해서 이동 
      nx = x+dx[move]*step
      ny = y+dy[move]*step
      
       # 주어진 범위를 벗어나는 경우 무시
  	   # x, y의 범위가 0,0보다 작아지거나, 주어진 matrix의 크기를 초과하는 경우
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue

      # 방문하지 않았을경우만
      if not visited[nx][ny]:
      	# 방문으로 수정
        visited[nx][ny] = True
        # 아직 우리가 찾는 조건(graph[x][y] == -1)이 아니므로 q에 담아주고 다시 반복
        q.append([nx, ny])  
        
if bfs(0,0):
    print('HaruHaru')
else:
    print('Hing')