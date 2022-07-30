import sys

n,m,k = map(int,sys.stdin.readline().split())
station = {}
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(k):
    a,b,c = sys.stdin.readline().split()
    if a<b:
        station[a] = (b,c)

for i in range(1,n+1):
    for j in range(1,n+1):
        graph[i][j] = max()