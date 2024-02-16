def solution(k, score):
    answer = []
    lists = []
    
    for i in range(len(score)):
        lists = sorted(score[:i+1])
        
        if i < k:
            answer.append(lists[0])
        else:
            answer.append(lists[i-k+1])
    
    
    return answer