from collections import deque

m,n,h = map(int,input().split())
graph=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
#3차원 배열 입력

d=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]

def bfs():
    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    queue.append((i,j,k)) #익은 토마토 좌표값들 큐로 정리
    while queue: #다 익을 때 까지 진행
        z,y,x = queue.popleft()
        for i in range(6):
            nz = z + d[i][0]
            ny = y + d[i][1]
            nx = x + d[i][2]         
            if 0<=nz<h and 0<=ny<n and 0<=nx<m:
                if graph[nz][ny][nx] == 0: 
                    graph[nz][ny][nx] = graph[z][y][x]+1 #새로 익을 때마다 날짜 증가 스탬프
                    queue.append((nz,ny,nx))

bfs()
date=0
flag = False #모두 익지는 못하는 상황 판단 flag
for z in graph:
    for y in z:
        for x in y:
            if x == 0: #안 익은 토마토 있으면 즉시 탈출
                flag = True
                break
            date = max(date,x) #최대 날짜 갱신

date = date -1         
if flag == True: #모두 익지는 못함
    print(-1)
elif date == 0: #처음 하루에 다 익음
    print(0)
else:
    print(date) #다 익는 날짜 출력