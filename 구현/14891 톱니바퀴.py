from collections import deque

gears = [[0]] + [deque(list(map(int, input()))) for _ in range(4)]
n = int(input())
activity = [list(map(int,input().split())) for _ in range(n)]
check = [False]*6

def check_rotate(num, dir):
    global check
    check = [False]*6
    check[num] = dir
    for j in range(4):
        for i in range(1,5):
            if check[i-1]: #왼쪽 체크
                if gears[i-1][2] != gears[i][6]:
                    check[i] = - check[i-1]
            if check[i+1]: #오른쪽 체크
                if gears[i][2] != gears[i+1][6]:
                    check[i] = - check[i+1]

for act in activity:
    check_rotate(act[0], act[1])  
    for i in range(1,5): 
        gears[i].rotate(check[i])

score = 1*gears[1][0] + 2*gears[2][0] + 4*gears[3][0] + 8*gears[4][0]

print(score)