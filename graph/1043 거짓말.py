n,m= map(int,input().split())
known = set(list(map(int,input().split()))[1:]) #처음 진실을 아는 사람
party = [[] for _ in range(m)]
Truth_people = known

for i in range(m): #파티 초기화
    s = list(map(int,input().split()))
    party[i] = set(s[1:])

for i in range(m): # 1단계: 진실을 아는 사람이 있는 파티원 전부 truth처리
    if party[i] & known:
        Truth_people = Truth_people | party[i]

count = 0
for i in range(m): # 2단계: 위에서 진실을 알게된 파티원이 없는 경우 과장파티
    if not party[i] & Truth_people:
        count+=1 

print(count)