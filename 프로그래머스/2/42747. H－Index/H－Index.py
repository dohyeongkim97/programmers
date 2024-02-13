def solution(citations):
    answer = 0
        
    sorted_citations = sorted(citations, reverse=True)
    
    for i in range(len(sorted_citations)):
        if sorted_citations[i] >= i+1:
            answer += 1

        else:
            break
            
    return answer