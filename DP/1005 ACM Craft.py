import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n,k = map(int,sys.stdin.readline().split())
    cost = [False] + list(map(int,sys.stdin.readline().split()))
    rule = [[] for _ in range(n+1)]
    indegree = [0]*(n+1) #진입차수
    dp = [0]*(n+1) #시간 dp

    for i in range(k): ##위상정렬
        a, b = map(int,sys.stdin.readline().split())
        rule[a].append(b)
        indegree[b] += 1

    w = int(sys.stdin.readline())

    que =deque()

    for i in range(1,n+1): #진입차수 0인 노드를 시작점으로 추가
        if indegree[i] == 0:
            que.append(i)
    
    while que:
        node = que.popleft()

        for next_node in rule[node]:
            indegree[next_node] -= 1 #간선 제거
            dp[next_node] = max(dp[next_node], dp[node] + cost[node])
            if indegree[next_node]==0:
                que.append(next_node)

    print(dp[w]+cost[w])