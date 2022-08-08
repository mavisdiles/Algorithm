# 시간초과
import sys
n, l = map(int,sys.stdin.readline().split())
max = 10**9

flag =False
s=[]
if l <=100:
    start = 0
    end = start + l-1
    s_sum =0
    while len(s)<=100 :
        s = []
        for i in range(start,end+1):
            s.append(i)
        s_sum = sum(s)

        if s_sum == n:
            flag = True
            break

        start = start+1
        end = start + l-1
        
        if s_sum >n :
            l = l+1
            start = 0
            end = start + l-1

if flag == True:
    for i in s:
        print(i, end=' ')
else:
    print(-1)