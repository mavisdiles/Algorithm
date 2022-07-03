from collections import deque
n,m,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(k)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = [[0]*m for _ in range(n)]
graph = [["."]*m for _ in range(n)]

for i in range(k):
    r,c = arr[i]
    graph[r-1][c-1] = "#"

def bfs(r,c):
    queue = deque()
    queue.append((r,c))
    visited[r][c] = True
    count = 0
    
    while queue:
        r,c = queue.popleft()
        if graph[r][c] == "#":
            count+=1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<n and 0<=nc<m:
                    if not visited[nr][nc] and graph[nr][nc] == "#":
                        queue.append((nr,nc))
                        visited[nr][nc] = True
    return count

s =[]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            s.append(bfs(i,j))
print(max(s))