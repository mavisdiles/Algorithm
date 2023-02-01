from collections import deque

n,m,k = map(int,input().split())
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))

def score(cur_xy, current_num):
    count = bfs(cur_xy,current_num)
    score = current_num *count
    return score

def rotate(dice,cur_xy,cur_dir):
    x,y = cur_xy
    
    if cur_dir == 0: #북쪽
        if x !=0:
            temp = dice[0]
            dice[0]= dice[2]
            dice[2]= dice[4]
            dice[4]= dice[5]
            dice[5]= temp
            cur_xy = [x-1,y]
        else:
            temp = dice[5]
            dice[5]= dice[4]
            dice[4]= dice[2]
            dice[2]= dice[0]
            dice[0]= temp
            cur_xy = [x+1,y]
            cur_dir = 2
    elif cur_dir == 1: #동쪽
        if y !=m-1:
            temp = dice[5]
            dice[5]= dice[3]
            dice[3]= dice[2]
            dice[2]= dice[1]
            dice[1]= temp
            cur_xy = [x,y+1]
        else:
            temp = dice[1]
            dice[1]= dice[2]
            dice[2]= dice[3]
            dice[3]= dice[5]
            dice[5]= temp
            cur_xy = [x,y-1]
            cur_dir = 3
    elif cur_dir ==2: #남쪽
        if x != n-1:
            temp = dice[5]
            dice[5]= dice[4]
            dice[4]= dice[2]
            dice[2]= dice[0]
            dice[0]= temp
            cur_xy = [x+1,y]
        else:
            temp = dice[0]
            dice[0]= dice[2]
            dice[2]= dice[4]
            dice[4]= dice[5]
            dice[5]= temp
            cur_xy = [x-1,y]
            cur_dir = 0
    elif cur_dir ==3: #서쪽
        if y !=0:
            temp = dice[1]
            dice[1]= dice[2]
            dice[2]= dice[3]
            dice[3]= dice[5]
            dice[5]= temp
            cur_xy = [x,y-1]
        else:
            temp = dice[5]
            dice[5]= dice[3]
            dice[3]= dice[2]
            dice[2]= dice[1]
            dice[1]= temp
            cur_xy = [x,y+1]
            cur_dir = 1
    return dice, cur_xy, cur_dir


def direction(bottom, current_num, cur_dir):
    if bottom> current_num: #시계방향 90도 회전
        if cur_dir !=3:
            cur_dir += 1
        else:
            cur_dir = 0
    elif bottom< current_num: #반시계방향 90도 회전
        if cur_dir !=0:
            cur_dir -= 1
        else:
            cur_dir = 3
    return cur_dir

def bfs(cur_xy,current_num):
    count = 1
    dxy = [[1,0],[-1,0],[0,1],[0,-1]]
    visited = [[False]*m for _ in range(n)]
    
    q = deque()
    q.append(cur_xy)
    visited[cur_xy[0]][cur_xy[1]] = True

    while(q):
        xy = q.popleft()
        for i in dxy:
            nx,ny = xy[0]+i[0],xy[1]+i[1]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False:
                if board[nx][ny] == current_num: 
                    q.append([nx,ny])
                    visited[nx][ny] = True
                    count +=1
    return count

score_sum =0 
xy = [0,0]
dice = [2,4,1,3,5,6]
dir = 1 # [n,e,s,w] = [0,1,2,3]

for i in range(k):  
    dice,xy,dir = rotate(dice,xy,dir)
    score_sum += score(xy,board[xy[0]][xy[1]])
    dir = direction(dice[5], board[xy[0]][xy[1]], dir)

print(score_sum)