# 불통, 다익스트라 이용
import sys
import heapq

n, m, r = map(int,sys.stdin.readline().split())
item = [0] + list(map(int, sys.stdin.readline().split()))
graph =[[] for _ in range(n+1)]

for i in range(r):
    a,b,l = map(int, sys.stdin.readline().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

def dijkstra(start):
    inf = 1000000
    distance = [inf]*(n+1)
    q = []
    heapq.heappush(q, [0,start])
    distance[start] = 0

    while q:
        cur_dist, cur_node = heapq.heappop(q)
        for next_node, next_dist in graph[cur_node]:
            if cur_dist + next_dist < distance[next_node]:
                distance[next_node] = cur_dist + next_dist
                heapq.heappush(q,[cur_dist + next_dist, next_node])
    return distance

item_count =[]

for start in range(1,n+1):
    count = 0
    distance = dijkstra(start)
    for end in range(1,n+1):
        if distance[end] <m:
            count += item[end]
    item_count.append(count)

print(max(item_count))