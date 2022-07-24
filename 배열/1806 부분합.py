import sys
### 투포인터 알고리즘
n,s = map(int,sys.stdin.readline().split())
sequence = list(map(int,sys.stdin.readline().split()))

length = len(sequence)
min=10**5
i,j =0,0
sum = sequence[0]

while True:
    if sum >= s:
        sum -= sequence[i]
        if min > j-i+1:
            min = j-i+1
        i+=1
    else:
        j+=1
        if j == length:
            break
        else:      
            sum += sequence[j]       

if min != 10**5:
    print(min)
else:
    print(0)
