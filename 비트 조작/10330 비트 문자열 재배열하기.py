#### 시간초과
import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
code = list(map(int,sys.stdin.readline().split()))
sequence = list(map(int,sys.stdin.readline().split()))

def bfs():
    que = deque()
    que.append((code,0)) 
    visited =[]
    while que:
        temp_code, count = que.popleft()
        if check(temp_code,sequence) == True:
            print(count)
            break
        for i in range(0,n-1):
            new_code = temp_code.copy()
            new_code[i], new_code[i+1] = new_code[i+1], new_code[i]
            if new_code not in visited:
                que.append((new_code,count+1))
                visited.append(new_code)
"""
def check(code,answer):
    temp = 1
    result = []

    if n==1:
        return True

    for i in range(1,n):      
        if code[i] == code[i-1]:
            temp +=1
        else:
            result.append(temp)
            temp = 1
        if i == n-1:
            result.append(temp)

    if result == answer:
        return True
    else:
        return False
"""
def check(code,answer):
    temp = 1

    if n==1:
        return True

    for i in range(1,n):  
        print(answer)  
        if not answer:
            break  
        if code[i] == code[i-1]:
            temp +=1
        else:
            if temp != answer.pop(0):
                return False
            temp = 1

    return True

bfs()