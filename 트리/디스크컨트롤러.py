def solution(jobs):
    time = 0
    consumption =0
    length = len(jobs)
    
    jobs.sort() #요청시점 빠른순, 소요시간 짧은순
    time = jobs[0][0] # 첫 프로세스 시각
    while jobs:
        cur =jobs[0]
        jobs.remove(cur)
        time = time + cur[1] # 작업 후 시각
        consumption = consumption + (time - cur[0]) # 총 소요 시간량 추가
        nominate=[]
        
        if jobs:
            for job in jobs:
                if job[0] <= time: #작업중에 요청된 프로세스들 후보 처리
                    nominate.append(job)
            if nominate: # 대기중인 후보 작업이 있을 때
                nominate.sort(key=lambda x: (x[1], x[0])) # 소요시간 짧은순
                jobs.remove(nominate[0])
                jobs.insert(0,nominate[0])
            else: # 대기중인 후보 작업이 없을 때
                jobs.sort() #요청시점 빠른순, 소요시간 짧은순
                time = jobs[0][0]
    
    answer = consumption//length
    return answer

print(solution([[0,3],[1,9],[2,6]]))