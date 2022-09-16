### 시간 초과 ???
import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
station = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    station[a].append((b,c))
start,end = map(int,sys.stdin.readline().split())

#다익스트라
def dijkst(start,end):
    distance = [100000]*(n+1)
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        cur_dist, cur_node = heapq.heappop(q)

        if distance[cur_node] < cur_dist:
            continue
        
        for next_node, next_dist in station[cur_node]:
            if cur_dist + next_dist < distance[next_node]:
                distance[next_node] = cur_dist + next_dist   
                heapq.heappush(q,[cur_dist + next_dist, next_node])
    return distance[end]
    
cost = dijkst(start,end)

print(cost)