import sys 
#sys.setrecursionlimit(10**9) #너무 크면 오히려 메모리 초과
sys.setrecursionlimit(15000) 

r, c = map(int,sys.stdin.readline().split())
graph = []
for _ in range(r):
    graph.append(list(sys.stdin.readline().strip()))

dxy = [(-1,0),(1,0),(0,-1),(0,1)]
alphabet = set(graph[0][0]) #시간초과나서 리스트에서 set형태로 변환
max_count=0

def dfs(x,y,count):
    global max_count
    max_count = max(max_count, count)
    for dx,dy in dxy:
        nx = x+dx
        ny = y+dy
        if 0<=nx<r and 0<=ny<c and graph[nx][ny] not in alphabet: #지나온 알파벳이면 다시 방문안해도됨  
            alphabet.add(graph[nx][ny])
            dfs(nx,ny,count+1) 
            alphabet.remove(graph[nx][ny]) # 탐색 끝나면 다시 다 삭제

dfs(0,0,1)
print(max_count)

