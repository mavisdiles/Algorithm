import sys
from itertools import combinations

n = int(sys.stdin.readline())
s=[]
for _ in range(n):
    s.append(list(sys.stdin.readline().split()))

team_case = [False]

def select_team():
    temp = list(range(n))
    for i in range(1,n//2+1):
        team_case.append(list(combinations(temp, i)))

select_team()
print(team_case)

for i in range(1,n//2+1):
    team_case.