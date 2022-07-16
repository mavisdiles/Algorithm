def solution(words, queries):
    answer = []
    
    for query in queries:
        count = 0
        str = query.strip("?")
        if query.startswith("?"):
            for word in words:
                if len(word) == len(query) and word.endswith(str):
                    count +=1
        else:
            for word in words:
                if len(word) == len(query) and word.startswith(str):
                    count +=1
                
        answer.append(count) 
    
    return answer