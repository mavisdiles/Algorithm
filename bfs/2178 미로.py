from collections import deque

n, m = map(int,input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    x,y = 0,0
    queue = deque()
    queue.append((x,y))
    visited[0][0]=1

    while queue:
        x,y = queue.popleft()
        if x==n-1 and y==m-1:     
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == '1' and not visited[nx][ny] :  
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))          
    
print(bfs())