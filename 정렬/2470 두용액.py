import sys

n = int(sys.stdin.readline())
liquid = list(map(int,sys.stdin.readline().split()))

liquid.sort()

i=0
j=n-1
min = 2*10**9

while i<j:
    mix = liquid[i]+liquid[j]

    if abs(mix) < min:
        min = abs(mix)
        answer = [liquid[i],liquid[j]]

    if mix < 0:
        i +=1
    else:
        j -=1

print(answer[0],answer[1])
