import heapq
import sys

n = int(sys.stdin.readline())
queue = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if queue:
            print(heapq.heappop(queue)[1])
        else:
            print(0)
    else:
        heapq.heappush(queue,(abs(num),num))