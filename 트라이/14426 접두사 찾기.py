#pypy 통과, 굳이 트라이?
import sys
n, m = map(int,sys.stdin.readline().split())
s=[]

for i in range(n):
    str = sys.stdin.readline().strip()
    s.append(str)

count =0

for i in range(m):
    prefix = sys.stdin.readline().strip()
    for target in s:
        if prefix == target[:len(prefix)]:
            count +=1
            break

print(count)