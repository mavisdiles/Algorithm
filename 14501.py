n = int(input())
schedule = []
for i in range(n):
    t, p = map(int,input().split())
    schedule.append([t,p])

dp = [0 for _ in range(n)]

for i in range(n):
    temp = dp[i-1]
    for j in range(i+1):
        if j + schedule[j][0] - 1 <= i:
            temp = max(temp, dp[j-1] + schedule[j][1])
    dp[i] = temp

print(dp[n-1])