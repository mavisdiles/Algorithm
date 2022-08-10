import sys
from xml.dom import minidom

n,m = map(int,sys.stdin.readline().split())
jewel = [int(sys.stdin.readline()) for _ in range(m)]

low =1
high = max(jewel)
answer = high
while low <= high:
    mid = (low+high)//2
    children = 0
    for i in jewel:
        if i%mid == 0:
            children += (i//mid)
        else:
            children += (i//mid)+1

    if children >n:
        low = mid + 1
    else:
        answer = min(answer,mid)
        high = mid - 1 

print(answer)