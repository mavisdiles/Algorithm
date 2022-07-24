#dfs로 하려다 시간초과 실패 => 이분검색으로 bfs돌리기
import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

point1, point2 = map(int,sys.stdin.readline().split())

def bfs(weight): #해당 중량이 통과되는 루트가 하나라도 있는지 bfs로 검색
    stack = deque()
    visited = [False]*(n+1)
    stack.append(point1)
    visited[point1] = True
    while stack:  
        start = stack.popleft()
        if start == point2:
            return True
        for island in graph[start]:
            if visited[island[0]] == False and island[1] >= weight:
                stack.append(island[0])
                visited[island[0]] = True
    return False
    
start=1
end=10**9
max =0
# 범위(1~10**9)내에서 이분검색
while start <= end:
    mid = (start+end)//2
    flag = bfs(mid) #특정 중량으로 bfs
    if flag:
        max = mid
        start = mid + 1
    else:
        end = mid-1

print(max)
