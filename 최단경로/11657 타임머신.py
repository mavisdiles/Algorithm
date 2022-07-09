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
                if i == n-1: # 계속 갱신되면 무한반복
                    return -1
    return dist
            
result = bellmanford(1) # 1번 도시 출발

if result == -1: #무한히 오래전으로 가는 경우
    print(-1)
else:
    for i in range(2,n+1): # 도시 별 시간 출력
        if result[i]==inf:
            print(-1)
        else:
            print(result[i])