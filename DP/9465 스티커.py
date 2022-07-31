import sys
t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    dp =[]
    for j in range(2):
        dp.append(list(map(int,sys.stdin.readline().split())))

    for k in range(1,n):
        if k==1:
            dp[0][k] = dp[0][k] + dp[1][k-1]
            dp[1][k] = dp[1][k] + dp[0][k-1]
            continue

        dp[0][k] = dp[0][k] + max(dp[1][k-2],dp[1][k-1])
        dp[1][k] = dp[1][k] + max(dp[0][k-2],dp[0][k-1])

    print(max(dp[0][n-1], dp[1][n-1]))