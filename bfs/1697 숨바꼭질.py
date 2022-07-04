from collections import deque

n, k = map(int,input().split())
max = 100000
time = [0]*(max+1) #0~10000 지정

def bfs(n,k):
    queue = deque()
    queue.append(n) # 출발지점 
    while queue:
        x = queue.popleft()
        if x == k: # 동생 위치 찾으면 종료
            return time[x]
        for nx in (x-1, x+1, 2*x): # 3가지 경우 추적       
            if 0 <= nx <= max and not time[nx]: # 방문하지 않았고, 범위 안에 해당 될 때만 계산수행
                time[nx] = time[x] + 1 #이동좌표마다 전 좌표 타임스탬프+1로 처리
                queue.append(nx)          
                
time = bfs(n,k)
print(time)