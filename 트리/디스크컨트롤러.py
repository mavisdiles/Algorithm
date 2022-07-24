def solution(jobs):
    time = 0
    consumption =0
    
    jobs.sort(key=lambda x: (x[0], x[1]))
    length = len(jobs)
    time = jobs[0][0]
    while jobs:
        cur =jobs[0]
        jobs.remove(cur)
        time = time + cur[1]
        consumption = consumption + (time - cur[0])
        nominate=[]
        
        if jobs:
            for job in jobs:
                if job[0] <= time:
                    nominate.append(job)
            if nominate:
                nominate.sort(key=lambda x: (x[1], x[0])) # 소요시간 짧은순
                jobs.remove(nominate[0])
                jobs.insert(0,nominate[0])
            else: #하드디스크가 비어있을 때
                jobs.sort(key=lambda x: (x[0], x[1])) #요청시점 빠른순, 소요시간 짧은순
                time = nominate[0][0]
    
    answer = consumption//length
    return answer

print(solution([[0,3],[1,9],[2,6]]))