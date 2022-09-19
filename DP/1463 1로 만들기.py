import sys
n = int(sys.stdin.readline())

dp = [-1]*(n+1)
inf = 10**9
for i in range(1,n+1):
    a = dp[i-1]+1
    if i%3 == 0:
        b = dp[i//3]+1
    else:
        b=inf
    if i%2 == 0:
        c = dp[i//2]+1
    else:
        c=inf

    dp[i] = min(a,b,c)

print(dp[n])

