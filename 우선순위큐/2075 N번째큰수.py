import heapq

n = int(input())       
array = []

for i in range(n):
    # 데이터 한꺼번에 다받으면 메모리 초과되서 매 행마다 n개씩 받음.
    numbers = list(map(int,input().split()))
    
    for num in numbers:
        if len(array) < n: # n개 채워질때가지 push
            heapq.heappush(array,num)
        else:
            if num> array[0]: # minheap을 이용한 최솟값 pop, 현재값 push
                heapq.heappop(array)
                heapq.heappush(array,num)
        
print(array[0])