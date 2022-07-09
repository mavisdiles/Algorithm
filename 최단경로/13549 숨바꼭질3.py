from collections import deque
n,k = map(int,input().split())

max = 100000
graph = [0]*(max+1)
visited = [False]*(max+1)

def bfs(n,k): # 우선순위 가중치 개수가 더 많았으면 거의 다익스트라
    x=n
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        x = queue.popleft()
        if x == k:
            return graph[x]
        
        for dx in [2*x,x-1,x+1]:
            nx = dx      
            if 0 <= nx <=max and not visited[nx]:
                if nx == 2*x : # x가 1인 경우 2*x와 x+1이 같다.
                    graph[nx] = graph[x]
                    visited[nx] = True
                    queue.appendleft(nx) # 우선순위를 2*x로 먼저 맞춰준다.
                else :
                    graph[nx] = graph[x]+1
                    visited[nx] = True
                    queue.append(nx)
                # 2*x를 먼저 탐색하지 않으면 결과 틀림.
print(bfs(n,k))