import sys

n,m,k = sys.stdin.readline().split()
station = {}
for i in range(k):
    a,b,c = sys.stdin.readline().split()
    if a<b:
        station[a] = (b,c)

