import sys

n = int(sys.stdin.readlline())
ratio = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,p,q = map(int,sys.stdin.readline().split())
    ratio[a].append([b,p,q]) 
    ratio[b].append([a,q,p]) 

