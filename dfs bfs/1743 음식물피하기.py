from collections import deque
n,m,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(k)] #음식물 좌표 값들

dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = [[0]*m for _ in range(n)]
graph = [["."]*m for _ in range(n)] #음식물 없는 곳은 "."처리

for i in range(k):
    r,c = arr[i] #음식물 좌표 값들 graph상에서 "#"처리
    graph[r-1][c-1] = "#"

def bfs(r,c):
    queue = deque()
    queue.append((r,c))
    visited[r][c] = True
    count = 0
    
    while queue:
        r,c = queue.popleft()
        if graph[r][c] == "#":
            count+=1 #음식물 크기 1씩 증가
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
            s.append(bfs(i,j)) #음식물 크기 s배열에 저장
print(max(s)) #가장 큰 음식물 크기 출력