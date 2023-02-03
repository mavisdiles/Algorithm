import sys
sys.setrecursionlimit(10**5)
n = int(sys.stdin.readline())
row = [0]*n
ans = [0]*n

def move_check(k):
    for i in range(k): #k행 전까지 행과 비교
        if row[k] == row[i] or abs(row[k]-row[i]) == abs(k-i): # 대각선에 있거나 column이 겹치는 경우
            return False
    return True

found = False

def dfs(num):
    global found
    if num == n:
        for i in range(n):
            print(ans[i])
        found = True
    else:
        for j in range(n): # column값 대조
            if found == True:
                break
            row[num] = j
            if move_check(num) == True:
                ans[num]=j
                dfs(num+1)
            
dfs(0) # row 0부터 시작
            


