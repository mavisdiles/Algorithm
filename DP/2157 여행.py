import sys

n,m,k = map(int,sys.stdin.readline().split())
station = {}
graph = [[False]*(n+1) for _ in range(n+1)]
print(graph)
for i in range(k):
    a,b,c = sys.stdin.readline().split()
    if a<b:
        station[a] = (b,c)

