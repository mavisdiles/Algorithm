import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
colors = [False] + list(map(int,sys.stdin.readline().split()))
tree = [[] for _ in range(n+1)]

#트리 입력
for i in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    if a<b:
        tree[a].append(b)
    else:
        tree[b].append(a)

count =0

def dfs(root): 
    global count
    for i in tree[root]:
        if colors[i] == colors[root]:
            dfs(i)
        else:
            count +=1
            dfs(i)

dfs(1)

if colors[1]==0:
    print(count)
else:
    print(count+1)