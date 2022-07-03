from collections import deque

m,n,h = map(int,input().split())
graph=[]
for i in range(h):
    temp = [list(map(int,input().split())) for _ in range(n)]
    graph.append(temp)

d=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
def bfs():
    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    queue.append((i,j,k))
    while queue:    
        z,y,x = queue.popleft()
        for i in range(6):
            nz = z + d[i][0]
            ny = y + d[i][1]
            nx = x + d[i][2]         
            if 0<=nz<h and 0<=ny<n and 0<=nx<m:
                if graph[nz][ny][nx] == 0: 
                    graph[nz][ny][nx] = graph[z][y][x]+1
                    queue.append((nz,ny,nx))

bfs()
date=0
flag = False
for z in graph:
    for y in z:
        for x in y:
            if x == 0:
                flag = True
                break
            date = max(date,x)
            
if flag == True:
    print(-1)
elif date == 1:
    print(0)
else:
    print(date-1)