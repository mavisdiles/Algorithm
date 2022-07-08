n,m = map(int,input().split())
inf = float('inf')
edges = []
dist = [inf]*(n+1)

for i in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

def bellmanford(start):
    dist[start] = 0
    for i in range(n):
        for s,d,w in edges:
            if dist[s] != inf and dist[d] > dist[s]+w:
                dist[d] = dist[s]+w
                if i == n-1:
                    return -1
    return dist
            
result = bellmanford(1)

if result == -1:
    print(-1)
else:
    for i in range(2,n+1):
        if result[i]==inf:
            print(-1)
        else:
            print(result[i])