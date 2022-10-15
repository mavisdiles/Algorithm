def solution(commands):
    matrix = [[]*50 for _ in range(50)]
    merge_list =[[0]]

    def is_merge(r,c):
        """
        for l in merge_list:
            if (r,c) in l:
                return True
            else:
                continue
                """
        return False
    """
    for i in commands:
        command = list(i.split(" "))
    """
    _, x, y = commands[-1].split(" ")
    
    answer=[]
    if is_merge(x,y):
        answer = ["EMTY",matrix(x,y)]
    else:
        answer = [matrix(x,y)]
    
    return answer