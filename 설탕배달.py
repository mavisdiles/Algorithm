n = int(input())

answer =0
remain = n

while remain >= 3:
    if remain % 5 == 0:
        answer += remain //5
        remain =0
        break

    remain -= 3
    answer +=1    

if remain == 0:
    print(answer)
else:
    print(-1)