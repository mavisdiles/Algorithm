from collections import defaultdict
def solution(id_list, report, k):

    target = defaultdict(set)
    user_dic = defaultdict(list)
    
    for i in report:
        a,b = i.split()
        target[b].add(a)
        user_dic[a].append(b) 
        
    banned_id_list =[]
    for i in id_list:
        if len(target[i]) >= k:
            banned_id_list.append(i)
        
    report_count = defaultdict(int)
    for i in id_list:
        report_count[i]=0
        for j in banned_id_list:
            if j in user_dic[i]:
                report_count[i] += 1
            
    answer = list(report_count.values())
    
    return answer