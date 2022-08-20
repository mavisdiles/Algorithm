import sys
from itertools import combinations

n = int(sys.stdin.readline())
s=[]
for _ in range(n):
    s.append(list(map(int,sys.stdin.readline().split())))

temp_case = [False]
start_case = []
link_case = []

temp = list(range(n))
for i in range(1,n//2+1): # 가능한 팀 조합 뽑기
    temp_case.append(set(combinations(temp, i)))


team = list(range(n))
for i in range(1,n//2+1): # start, link 조합 분할
    for case in temp_case[i]:
        start_case.append(set(team) -set(case))
        link_case.append(set(case))

answer = 10000000

for i in range(len(start_case)):
    start_score=0
    link_score=0
    for x in start_case[i]:
        for y in start_case[i]:
            start_score += s[x][y]
    for x in link_case[i]:
        for y in link_case[i]:
            link_score += s[x][y]

    answer = min(answer, abs(start_score-link_score))

print(answer)