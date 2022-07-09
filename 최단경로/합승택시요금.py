import heapq

def solution(n, s, a, b, fares):
    INF = float('inf')
    
    def dijkstra(start,end): # 시작부터 끝점까지 최소 비용 계산
        
        graph =[[]for _ in range(n+1)]
        dist = [INF]*(n+1)
        dist[start]=0
        queue =[]
        heapq.heappush(queue, [dist[start],start])
        
        for a,b,c in fares: # fares 인접 노드 graph로 정리
            graph[a].append((b,c))
            graph[b].append((a,c))
        
        while queue:
            cur_dist,cur_node = heapq.heappop(queue)
            
            if dist[cur_node] < cur_dist:
                continue
                
            for new_node, new_dist in graph[cur_node]:
                distance = cur_dist + new_dist
                if distance < dist[new_node]:
                    dist[new_node] = distance
                    heapq.heappush(queue, [distance, new_node])
        return dist[end] # end까지 가는 최소 비용 반환
    
    list=[INF for _ in range(n+1)]
    # (s에서 i로 dijkstra), (i에서 a,b로 각각로 dijkstra)을 더한값이 최소가 되는 경우를 찾는다.
    for i in range(1,n+1):
        list[i] = dijkstra(s,i) + dijkstra(i,a) + dijkstra(i,b)
    
    return min(list)