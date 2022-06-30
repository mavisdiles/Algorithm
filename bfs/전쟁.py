from collections import deque

n, m  = map(int,input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
w, b = 0,0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,color):
    queue = deque()
    queue.append((x,y))
    count = 0
    visited[x][y] == True
    
    while queue:
        x, y = queue.popleft()     
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<m and 0<=yy<n:
                if visited[xx][yy] != True and graph[xx][yy] == color:
                    queue.append((xx,yy))
                    visited[xx][yy] = True
                    count += 1                        
    return count if count>0 else 1

for i in range(n):
    for j in range(m):
        if visited[i][j] != True:
            if graph[i][j] == 'W':
                w += bfs(i,j,'W')**2
            else:
                b += bfs(i,j,'B')**2

print(w, b)