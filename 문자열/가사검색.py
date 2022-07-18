def solution(words, queries):
    answer = []
    
    for query in queries:
        count = 0
        str = query.strip("?") # ?를 전부뺀 문자열
        if query.startswith("?"): #?로 시작하는 문자열은 str로 끝난다.
            for word in words:
                if len(word) == len(query) and word.endswith(str):
                    count +=1
        else: #?로 끝나는 문자열은 str로 시작한다.
            for word in words:
                if len(word) == len(query) and word.startswith(str):
                    count +=1
                
        answer.append(count) 
    
    return answer