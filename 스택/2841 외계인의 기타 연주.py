# Pypy3로 통과, Python3는 시간초과
n,p = map(int,input().split())
melodies = [list(map(int, input().split())) for _ in range(n)]

strings =[[] for _ in range(6)] # 줄 6개 스택
count = 0 

for melody in melodies:
    i = melody[0]-1 #줄 번호 매치
    
    if not strings[i]: #해당 줄 스택이 없는 경우
        strings[i].append(melody)
        count+=1
    else: #해당 줄 스택이 있는 경우
        while strings[i] and melody[1] < strings[i][-1][1]: 
            strings[i].pop() # 현재 프랫보다 작은 프랫 나올때까지 pop, 카운팅
            count+=1
        if not strings[i] or melody[1] != strings[i][-1][1]:
            strings[i].append(melody) # 스택이 비었거나 해당 프랫번호가 없을 때 추가
            count+=1
        # 스택이 비어있지 않고, 해당 프랫 번호가 이미 있으면 건너뜀
                                
print(count)    