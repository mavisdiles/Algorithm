line1 = input()
line2 = input()

n = len(line1)
m = len(line2)

table = [[0]*(m+1) for _ in range(n+1)] # (0~m)*(0~n) 테이블 이용

for i in range(1,n+1):
    for j in range(1,m+1):
        if line1[i-1] == line2[j-1]: # 추가 문자가 같을 경우
            table[i][j] = table[i-1][j-1]+1 # 문자 추가전 상태에서 길이 1 증가
        else: # 추가 문자가 서로 다를 경우
            table[i][j] = max(table[i][j-1],table[i-1][j]) # 문자 추가 전 상태 중 최댓값 복사
            
print(table[n][m])