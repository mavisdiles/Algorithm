import sys

n = int(sys.stdin.readline())
liquid = list(map(int,sys.stdin.readline().split()))

liquid.sort()

temp_sum = 0
answer = [None,None,None]
min = 3000000001 
for k in range(n-2):
    i= k+1
    j = n-1

    while i<j:
        temp_sum = liquid[k]+liquid[i]+liquid[j]

        if abs(temp_sum) < min:
            min = abs(temp_sum)
            answer = [liquid[k],liquid[i],liquid[j]]

        if temp_sum <0:
            i +=1
        if temp_sum >0:
            j -=1
        if temp_sum == 0:
            break
        
print(answer[0],answer[1],answer[2])
















