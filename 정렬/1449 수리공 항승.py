import sys

n,l = map(int,sys.stdin.readline().split())
flaw = list(map(int,sys.stdin.readline().split()))

flaw.sort()

start,end =0,0
count =0

for i in flaw:
    if end < i:
        start = i-0.5
        end = start +l
        count+=1
    else:
        continue

print(count)