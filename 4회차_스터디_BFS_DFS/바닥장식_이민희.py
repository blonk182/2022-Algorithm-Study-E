n, m = map(int, input().split())
floor = []
for i in range(n):
    floor.append(input())  # 예) floor = ['----','----','----','----']
visited = [[0 for i in range(m)] for j in range(n)]  # n:세로, m:가로

cnt = 0


def dfs(x, y):  # x: 행, y: 열
    if x <= -1 or x >= n or y <= -1 or y >= m:  # 범위 벗어나면 False
        return False
    if not visited[x][y]:
        visited[x][y] = True

        if floor[x][y] == '-' and (y == m-1 or floor[x][y+1] == '-'):
            dfs(x, y+1)
        if floor[x][y] == '|' and (x == n-1 or floor[x+1][y] == '|'):
            dfs(x+1, y)
        return True  # '-' 타일에서 '|' 타일 옆으로 나타나면 개수 1 증가, '|' 타일에서 '-' 타일 아래로 나타나면 개수 1 증가
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j):  # True 반환할 때마다 개수 1 증가
            cnt += 1

print(cnt)
