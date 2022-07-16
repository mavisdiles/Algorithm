from collections import deque

n = int(input())
tree = [[]for i in range(n+1)]
visited = [False]*(n+1)
parents = [[]for i in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)  

def bfs():
    que = deque()
    que.append(1)
    visited[1] = True
    while que:
        parent = que.popleft()
        for i in tree[parent]:
            if not visited[i]:
                parents[i] = parent
                visited[i] = True
                que.append(i)

bfs()

for i in range(2,n+1):
    print(parents[i])