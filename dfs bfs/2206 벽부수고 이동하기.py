import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())

graph =[]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

visited = [[False]*m for _ in range(n)]

def bfs():
    q = deque()
    q.append([0,0,False])
    visited[0][0] = 1
    while q:
        x,y, chance = q.popleft()
        
        if x==n-1 and y==m-1:
            return visited[x][y]

        for d in [[-1,0],[1,0],[0,-1],[0,1]]:
            dx = x + d[0]
            dy = y + d[1]

            if 0<= dx<=n-1 and 0<=dy<=m-1 and not visited[dx][dy]:
                if graph[dx][dy]==1: # 벽이 있을때
                    if chance == False: # 찬스를 쓴 적 없으면 뿌수고 가기
                        visited[dx][dy] = visited[x][y]+1
                        q.append([dx,dy,True])
                else: # 벽이 없을때
                    visited[dx][dy] = visited[x][y]+1
                    q.append([dx,dy,chance])
    return -1

value = bfs()
print(value)