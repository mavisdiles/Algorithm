import sys

def count(mark):
    if mark == 'X':
        return graph.count('X')
    elif mark == 'O':
        return graph.count('O')

def bingo(mark):
    if graph[0]==mark and graph[0] == graph[1] == graph[2]:
        return True
    if graph[0]==mark and graph[0] == graph[4] == graph[8]:
        return True
    if graph[0]==mark and graph[0] == graph[3] == graph[6]:
        return True
    if graph[3]==mark and graph[3] == graph[4] == graph[5]:
        return True
    if graph[1]==mark and graph[1] == graph[4] == graph[7]:
        return True
    if graph[6]==mark and graph[6] == graph[4] == graph[3]:
        return True
    if graph[6]==mark and graph[6] == graph[7] == graph[8]:
        return True
    if graph[8]==mark and graph[8] == graph[5] == graph[2]:
        return True
    else:
        return False


while True:
    graph = list(sys.stdin.readline().strip())
    
    if graph == ['e','n','d']:
        break
    x_count = count('X')
    o_count = count('O')
    
    if x_count == o_count: ## O가 이기는 경우
        if bingo('O') == True and bingo('X') == False:  # O가 bingo, X가 bingo면 valid
            print('valid')
        else:
            print('invalid')
    elif x_count == o_count +1: ##  X가 이기거나, 가득차서 종료
        if x_count <5: # x가 이기는 경우
            if bingo('O') == False and bingo('X') == True:
                print('valid')
            else:
                print('invalid')
        elif x_count == 5: # 가득차서 종료
            print('valid')
        else:
            print('invalid')
    else:
        print('invalid')