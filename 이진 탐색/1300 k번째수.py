import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

left,right = 1,k
while left <= right:
    mid = (left + right)//2

    count =0
    for i in range(1,n+1):
        count += min(mid//i, n)

    if count >= k:
        right = mid -1
    else:
        left = mid+1

print(left)
